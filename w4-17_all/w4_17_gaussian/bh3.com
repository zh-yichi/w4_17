%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
B        0.000000    0.000000    0.000000 
H        0.000000    1.189900    0.000000 
H        1.030484   -0.594950    0.000000 
H       -1.030484   -0.594950    0.000000 

