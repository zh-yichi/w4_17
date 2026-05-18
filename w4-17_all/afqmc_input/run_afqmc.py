import os
os.environ.setdefault("XLA_PYTHON_CLIENT_ALLOCATOR", "platform")

import jax
jax.config.update("jax_enable_x64", True)

import glob
import numpy as np
from pyscf import gto, scf, cc
from afqmc import prep, launch_afqmc
import re

def extract_afqmc_energy(filename):
    """Extract the final AFQMC/pt2CCSD energy and its uncertainty from an afqmc.out file.
    
    Returns (0, 0) if the value cannot be found or the file cannot be read.
    """
    pattern = re.compile(
        r"Final AFQMC/pt2CCSD energy:\s*"
        r"([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"   # energy
        r"\s*(?:±|\+/-)\s*"
        r"([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"   # error
    )
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                m = pattern.search(line)
                if m:
                    return float(m.group(1)), float(m.group(2))
    except (OSError, IOError):
        pass
    return 0, 0

# basis = "ccpvdz"
xyz_dir = "../w4_17_xyz/open_shell"
results_file = f"./open_shell_uhf_vdzsd.dat"
out_dir = "../result/molout/open_shell"
os.makedirs(out_dir, exist_ok=True)

# Set to a list of molecule names to run only those, e.g. ["acetaldehyde", "benzene"]
# Set to None to run all molecules in xyz_dir
select_molecules = None
symmetry = False

def vdzsd(elem):
    if elem in ('H', 'He'):
        raw_basis = gto.basis.load('ccpvdz', elem)
        return [b for b in raw_basis if b[0] != 1]
    else:
        return gto.basis.load('ccpvdz', elem)

def get_vdzsd_basis(atoms):
    elems = {line.split()[0] for line in atoms.strip().splitlines() if line.strip()}
    basis_dict = {el: vdzsd(el) for el in elems}
    return basis_dict

all_xyz = sorted(glob.glob(os.path.join(xyz_dir, "*.xyz")))
if select_molecules is not None:
    select_set = set(select_molecules)
    xyz_files = [p for p in all_xyz if os.path.splitext(os.path.basename(p))[0] in select_set]
    missing = select_set - {os.path.splitext(os.path.basename(p))[0] for p in xyz_files}
    if missing:
        print(f"Warning: no .xyz file found for: {', '.join(sorted(missing))} in {xyz_dir}")
else:
    xyz_files = all_xyz

with open(results_file, "w") as out:
    out.write(f"{'Molecule':<16s} {'Charge':>6s} {'2S':>6s} {'frozen':>6s} "
              f"{'E_HF (Eh)':>20s} {'E_CCSD (Eh)':>20s} {'E_CCSD(T) (Eh)':>20s} "
              f"{'E_AFQMC (Eh)':>15s} {'E_AFQMC ERR (Eh)':>15s} \n")
    #out.write("-" * 100 + "\n")

for xyz_path in xyz_files:
    with open(xyz_path, "r") as f:
        lines = f.readlines()

    # Parse charge and multiplicity from second line: "name charge=X mult=Y"
    second_line = lines[1]
    charge = int(second_line.split("charge=")[1].split()[0])
    mult   = int(second_line.split("mult=")[1].split()[0])
    spin   = mult - 1   # PySCF spin input is 2S = mult - 1
    mol_name = second_line.split()[0]

    # Coordinates only (skip the atom count and comment lines)
    atoms = "".join(lines[2:])
    basis_dict = get_vdzsd_basis(atoms)

    print(f"\n{'='*60}")
    print(f"Running: {mol_name}  charge={charge}  spin={spin}")
    print(f"{'='*60}")

    mol = gto.M(
        atom=atoms,
        basis=basis_dict,
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

    # Stability check loop — at most 10 attempts
    max_stability_cycles = 10
    stable = False
    for stability_iter in range(max_stability_cycles):
        mo_i, _, stable, _ = mf.stability(return_status=True)
        if stable:
            break
        dm = mf.make_rdm1(mo_i, mf.mo_occ)
        mf.kernel(dm0=dm)

    if not stable or not mf.converged:
        print(f"  !! SCF did not converge for {mol_name} — skipping.")
        with open(results_file, "a") as out:
            out.write(f"{mol_name:<16s} {charge:>6d} {spin:>6d} {'N/A':>6s} "
                      f"{'UNCONVERGED':>20s} {'UNCONVERGED':>20s} {'UNCONVERGED':>20s}\n")
        continue

    energy = mf.e_tot

    mycc = cc.CCSD(mf)
    mycc.set_frozen()
    mycc.kernel()
    e_ccsd = mycc.e_tot
    et = mycc.ccsd_t()
    e_ccsdt = e_ccsd + et
    frozen = mycc.frozen

    prep.prep_afqmc(mycc, chol_cut=1e-5)
    options = {'n_eql': 120,
               'n_blocks': 1000,
               'n_walkers': 300,
               'dt':0.005,
               'max_error': 0.0,
               #'nchol_chunk': 200,
               'seed': 17,
               'walker_type': 'uhf',
               'trial': 'uccsd_pt2',
               'free_projection': False,
               'use_gpu': True,
               }
    launch_afqmc.run_afqmc(options)
    afqmc_file = os.path.join(out_dir, f'{mol_name}_afqmc_vdzsd.out')
    os.system(f"mv afqmc.out {afqmc_file}")
    eqmc, eqmc_err = extract_afqmc_energy(f"{afqmc_file}")

    with open(results_file, "a") as out:
        out.write(f"{mol_name:<16s} {charge:>6d} {spin:>6d} {frozen:>6d} "
                  f"{energy:>20.10f} {e_ccsd:>20.10f} {e_ccsdt:>20.10f}"
                  f"{eqmc:>15.5f} {eqmc_err:>15.5f} \n")

    print(f"  => E_HF({mol_name})      = {energy:.10f} Eh")
    print(f"  => E_CCSD({mol_name})    = {e_ccsd:.10f} Eh")
    print(f"  => E_CCSD(T)({mol_name}) = {e_ccsdt:.10f} Eh")
    print(f"  => E_AFQMC({mol_name})   = {eqmc:.5f} +/- {eqmc_err:.5f} Eh")

print(f"\nAll calculations complete. Results saved to {results_file}")
