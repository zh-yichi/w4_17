%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
Cl      -0.560974   -0.994637    0.000000 
O        0.000000    0.958712    0.000000 
O        1.192069    1.154892    0.000000 

