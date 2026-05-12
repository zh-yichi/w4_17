%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
S        0.000000    0.000000    0.000000 
O        0.000000    1.422790    0.000000 
O        1.232172   -0.711395    0.000000 
O       -1.232172   -0.711395    0.000000 

