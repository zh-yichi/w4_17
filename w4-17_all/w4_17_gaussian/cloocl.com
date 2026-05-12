%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
Cl       0.619701    1.545371   -0.387503 
O        0.619701    0.328769    0.823444 
O       -0.619701   -0.328769    0.823444 
Cl      -0.619701   -1.545371   -0.387503 

