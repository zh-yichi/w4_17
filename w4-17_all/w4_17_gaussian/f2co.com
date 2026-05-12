%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
O        0.000000    0.000000    1.312207 
C        0.000000    0.000000    0.140770 
F        0.000000    1.058663   -0.630126 
F        0.000000   -1.058663   -0.630126 

