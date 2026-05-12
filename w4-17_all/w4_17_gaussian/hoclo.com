%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
H        1.549461    0.644167    0.773792 
O        1.369289    0.318684   -0.119210 
Cl      -0.137557   -0.443711    0.017415 
O       -1.270663    0.543681   -0.014522 

