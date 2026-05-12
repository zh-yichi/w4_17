import numpy as np
from pyscf import gto, scf

xyzfile = "../w4_17_xyz/mol/acetaldehyde.xyz"
with open(xyzfile, 'r') as file:
    atoms = file.read()

charge = # charge from xyzfile
spin = # spin from xyzfile

mol = gto.M(atom = atoms,
            basis = "ccpvdz",
            verbose=4,
            unit='angstrom',
            symmetry=0,
            charge=charge,
            spin=spin,
            max_memory=40000)


mf = scf.RHF(mol)
# mf.chkfile = '../mf.chk'
# mf.init_guess = 'chk'
mf.max_cycle = 100
mf.kernel()

stable = False
while not stable:
    mo_i, _, stable,_ = mf.stability(return_status=True)
    dm = mf.make_rdm1(mo_i,mf.mo_occ)
    mf.kernel(dm0=dm)
