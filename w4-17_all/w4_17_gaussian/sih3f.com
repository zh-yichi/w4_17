%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
F        0.000000    0.000000   -1.099839 
Si       0.000000    0.000000    0.495525 
H        0.000000    1.390293    0.987068 
H       -1.204029   -0.695146    0.987068 
H        1.204029   -0.695146    0.987068 

