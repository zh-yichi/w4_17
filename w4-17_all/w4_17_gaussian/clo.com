%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
Cl       0.000000    0.000000    0.503953 
O        0.000000    0.000000   -1.070901 

