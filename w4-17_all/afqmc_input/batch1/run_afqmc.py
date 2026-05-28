import os
import sys
import re
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'script'))
sys.path.insert(0, '/u/yzhang65/mywork/yzhang65/w4_17/w4-17_all/script')

os.environ.setdefault("XLA_PYTHON_CLIENT_ALLOCATOR", "platform")
import jax
jax.config.update("jax_enable_x64", True)

from pyscf import gto, scf, cc
from afqmc import integral, launch_afqmc
from mol_select import get_xyz_files
import truncate_basis

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
shell            = "closed"  # "closed" or "open"
symmetry         = False
select_molecules = None  # e.g. ["acetaldehyde", "benzene"], or None for all
index            = "1-20"          # e.g. "1-10", "5", "1,3,5-8", or None for all
basis            = "vtzfp"

xyz_dir      = f"../../w4_17_xyz/{shell}_shell"
results_file = f"./{shell}_afqmc_{basis}.dat"
out_dir      = f"../../result/molout/{shell}_shell"
os.makedirs(out_dir, exist_ok=True)

xyz_files = get_xyz_files(xyz_dir, select_molecules=select_molecules, index=index)

# ---------------------------------------------------------------------------
# Write results header
# ---------------------------------------------------------------------------
with open(results_file, "w") as out:
    out.write(f"{'Molecule':<16s} {'E_HF (Eh)':>20s} {'E_CCSD (Eh)':>20s} "
              f"{'E_AFQMC (Eh)':>15s} {'E_AFQMC ERR (Eh)':>15s}\n")

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------
_afqmc_energy_re = re.compile(
    r"Final AFQMC/pt2CCSD energy:\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
    r"\s*(?:±|\+/-)\s*([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
)

def extract_afqmc_energy(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                m = _afqmc_energy_re.search(line)
                if m:
                    return float(m.group(1)), float(m.group(2))
    except (OSError, IOError):
        pass
    return 0, 0

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
for xyz_path in xyz_files:
    with open(xyz_path) as f:
        lines = f.readlines()

    second_line = lines[1]
    charge   = int(second_line.split("charge=")[1].split()[0])
    spin     = int(second_line.split("mult=")[1].split()[0]) - 1
    mol_name = second_line.split()[0]
    atoms    = "".join(lines[2:])

    print(f"\n{'='*60}\nRunning: {mol_name}  charge={charge}  spin={spin}\n{'='*60}")

    mol = gto.M(
        atom=atoms,
        basis=truncate_basis.get_basis(atoms, basis),
        verbose=4,
        output=os.path.join(out_dir, f"{mol_name}_{basis}.out"),
        unit="angstrom",
        symmetry=symmetry,
        charge=charge,
        spin=spin,
        max_memory=40000,
    )

    mf = scf.UHF(mol)
    mf.max_cycle = 200
    mf = mf.newton()
    mf.kernel()

    if mol_name == "h":
        with open(results_file, "a") as out:
            out.write(f"{mol_name:<16s} {mf.e_tot:>20.10f} {mf.e_tot:>20.10f} "
                      f"{mf.e_tot:>15.5f} {0.0:>15.5f}\n")
        continue

    stable = False
    for _ in range(10):
        mo_i, _, stable, _ = mf.stability(return_status=True)
        if stable:
            break
        dm = mf.make_rdm1(mo_i, mf.mo_occ)
        mf.kernel(dm0=dm)

    if not stable or not mf.converged:
        print(f"  !! SCF did not converge for {mol_name} — skipping.")
        with open(results_file, "a") as out:
            out.write(f"{mol_name:<16s} {'UNCONVERGED':>20s} {'UNCONVERGED':>20s} {'UNCONVERGED':>20s}\n")
        continue

    mycc = cc.CCSD(mf)
    mycc.set_frozen()
    mycc.kernel()

    integral.prep_integral(mycc, chol_cut=1e-5)
    options = {
        'eql_time':      50,
        'n_blocks':      1000,
        'n_walkers':     300,
        'max_error':     0.0,
        'seed':          17,
        'walker_type':   'uhf',
        'trial':         'upt2ccsd',
        'mix_precision': True,
        'max_memory':    20000, #MB
    }
    launch_afqmc.ph_afqmc(options)

    afqmc_out = os.path.join(out_dir, f"{mol_name}_afqmc_{basis}.out")
    os.system(f"mv afqmc.out {afqmc_out}")
    eqmc, eqmc_err = extract_afqmc_energy(afqmc_out)

    with open(results_file, "a") as out:
        out.write(f"{mol_name:<16s} {mf.e_tot:>20.10f} {mycc.e_tot:>20.10f} "
                  f"{eqmc:>15.5f} {eqmc_err:>15.5f}\n")

    print(f"  => E_HF({mol_name})      = {mf.e_tot:.10f} Eh")
    print(f"  => E_CCSD({mol_name})    = {mycc.e_tot:.10f} Eh")
    print(f"  => E_AFQMC({mol_name})   = {eqmc:.5f} +/- {eqmc_err:.5f} Eh")

print(f"\nAll calculations complete. Results saved to {results_file}")
