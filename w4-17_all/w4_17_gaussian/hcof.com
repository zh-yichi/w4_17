%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C        0.000000    0.397532    0.000000 
O        1.147071    0.120481    0.000000 
H       -0.445830    1.393761    0.000000 
F       -0.970082   -0.526978    0.000000 

