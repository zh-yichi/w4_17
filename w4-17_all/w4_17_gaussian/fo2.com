%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
F       -1.011195   -0.706276    0.000000 
O        0.000000    0.575215    0.000000 
O        1.137595    0.219345    0.000000 

