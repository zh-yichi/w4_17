from pyscf import gto

def vdzds(elem):
    """
    cc-pVDZ with upto d-functions for non-H atoms 
    and s-functions for H atoms [vdz(d,s) basis].
    """
    if elem not in ('H', 'He'):
        nh_basis = gto.basis.load('ccpvdz', elem)
        return [b for b in nh_basis if b[0] < 3] # upto d for non-H
    else: 
        h_basis = gto.basis.load('ccpvdz', elem)
        return [b for b in h_basis if b[0] < 1] # upto s for H

def get_vdzds_basis(atoms):
    """Return a per-element vdzds basis dict for a block of atom coordinates."""
    elems = {line.split()[0] for line in atoms.strip().splitlines() if line.strip()}
    return {el: vdzds(el) for el in elems}


def vtzfp(elem):
    """
    cc-pVTZ with upto f-functions for non-H atoms 
    and p-functions for H atoms [vtz(f,p) basis].
    """
    if elem not in ('H', 'He'):
        nh_basis = gto.basis.load('ccpvtz', elem)
        return [b for b in nh_basis if b[0] < 4] # upto f for non-H
    else: 
        h_basis = gto.basis.load('ccpvtz', elem)
        return [b for b in h_basis if b[0] < 2] # upto p for H

def get_vtzfp_basis(atoms):
    """Return a per-element vtz(f,p) basis dict for a block of atom coordinates."""
    elems = {line.split()[0] for line in atoms.strip().splitlines() if line.strip()}
    return {el: vtzfp(el) for el in elems}


def vqzfd(elem):
    """
    cc-pVQZ with upto f-functions for non-H atoms 
    and d-functions for H atoms [vqz(f,d) basis].
    """
    if elem not in ('H', 'He'):
        nh_basis = gto.basis.load('ccpvqz', elem)
        return [b for b in nh_basis if b[0] < 4] # upto f for non-H
    else: 
        h_basis = gto.basis.load('ccpvqz', elem)
        return [b for b in h_basis if b[0] < 3] # upto d for H

def get_vqzfd_basis(atoms):
    """Return a per-element vqz(f,d) basis dict for a block of atom coordinates."""
    elems = {line.split()[0] for line in atoms.strip().splitlines() if line.strip()}
    return {el: vqzfd(el) for el in elems}

def get_basis(atoms, basis_name):
    if basis_name == "vdzds":
        return get_vdzds_basis(atoms)
    elif basis_name == "vtzfp":
        return get_vtzfp_basis(atoms)
    elif basis_name == "vqzfd":
        return get_vqzfd_basis(atoms)