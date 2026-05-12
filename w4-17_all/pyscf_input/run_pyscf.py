import os
import glob
import numpy as np
from pyscf import gto, scf, cc

xyz_dir = "../w4_17_xyz/closed_shell"
results_file = "../result/closed_shell_rhf.dat"
out_dir = "../result/molout/closed_shell"
os.makedirs(out_dir, exist_ok=True)

# Set to a list of molecule names to run only those, e.g. ["acetaldehyde", "benzene"]
# Set to None to run all molecules in xyz_dir
# select_molecules = None
select_molecules = ["ch4", "h2o", "c2", "bn"]
symmetry = False

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
              f"{'E_RHF (Eh)':>20s} {'E_CCSD (Eh)':>20s} {'E_CCSD(T) (Eh)':>20s}\n")
    out.write("-" * 100 + "\n")

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

    print(f"\n{'='*60}")
    print(f"Running: {mol_name}  charge={charge}  spin={spin}")
    print(f"{'='*60}")

    mol = gto.M(
        atom=atoms,
        basis="ccpvdz",
        verbose=4,
        output=os.path.join(out_dir, f"{mol_name}.out"),
        unit="angstrom",
        symmetry=symmetry,
        charge=charge,
        spin=spin,
        max_memory=40000,
    )

    mf = scf.RHF(mol)
    mf.max_cycle = 100
    mf = mf.newton()
    mf.kernel()

    # Stability check loop
    stable = False
    while not stable:
        mo_i, _, stable, _ = mf.stability(return_status=True)
        #if not stable:
        dm = mf.make_rdm1(mo_i, mf.mo_occ)
        mf.kernel(dm0=dm)

    energy = mf.e_tot

    mycc = cc.CCSD(mf)
    mycc.set_frozen()
    mycc.kernel()
    e_ccsd = mycc.e_tot
    et = mycc.ccsd_t()
    e_ccsdt = e_ccsd + et
    frozen = mycc.frozen

    with open(results_file, "a") as out:
        out.write(f"{mol_name:<16s} {charge:>6d} {spin:>6d} {frozen:>6d} "
                  f"{energy:>20.10f} {e_ccsd:>20.10f} {e_ccsdt:>20.10f}\n")

    print(f"  => E_RHF({mol_name})     = {energy:.10f} Eh")
    print(f"  => E_CCSD({mol_name})    = {e_ccsd:.10f} Eh")
    print(f"  => E_CCSD(T)({mol_name}) = {e_ccsdt:.10f} Eh")

print(f"\nAll calculations complete. Results saved to {results_file}")
