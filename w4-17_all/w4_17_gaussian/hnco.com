%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C        0.000000    0.050807    0.000000 
O       -0.567947    1.069462    0.000000 
N        0.444803   -1.083005    0.000000 
H        1.429958   -1.279500    0.000000 

