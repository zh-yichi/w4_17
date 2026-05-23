import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'script'))

from pyscf import gto, scf, cc
from mol_select import get_xyz_files
from basis import get_vdzsd_basis

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
shell            = "open"    # "closed" or "open"
symmetry         = False
select_molecules = None      # e.g. ["acetaldehyde", "benzene"], or None for all
index            = "1,2,3,8"      # e.g. "1-10", "5", "1,3,5-8", or None for all

xyz_dir      = f"../w4_17_xyz/{shell}_shell"
results_file = f"../test/{shell}_shell_uhf_vdzsd.dat"
out_dir      = f"../test/molout/{shell}_shell"
os.makedirs(out_dir, exist_ok=True)

xyz_files = get_xyz_files(xyz_dir, select_molecules=select_molecules, index=index)

# ---------------------------------------------------------------------------
# Write results header
# ---------------------------------------------------------------------------
with open(results_file, "w") as out:
    out.write(f"{'Molecule':<16s} {'E_HF (Eh)':>20s} {'E_CCSD (Eh)':>20s} {'E_CCSD(T) (Eh)':>20s}\n")
    out.write("-" * 80 + "\n")

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
        basis=get_vdzsd_basis(atoms),
        verbose=4,
        output=os.path.join(out_dir, f"{mol_name}_vdzsd.out"),
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
    e_ccsdt = mycc.e_tot + mycc.ccsd_t()

    with open(results_file, "a") as out:
        out.write(f"{mol_name:<16s} {mf.e_tot:>20.10f} {mycc.e_tot:>20.10f} {e_ccsdt:>20.10f}\n")

    print(f"  => E_HF({mol_name})      = {mf.e_tot:.10f} Eh")
    print(f"  => E_CCSD({mol_name})    = {mycc.e_tot:.10f} Eh")
    print(f"  => E_CCSD(T)({mol_name}) = {e_ccsdt:.10f} Eh")

print(f"\nAll calculations complete. Results saved to {results_file}")
