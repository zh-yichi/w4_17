%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
H       -0.989366    0.909480    0.000000 
N        0.000000    0.624690    0.000000 
N        0.000000   -0.624690    0.000000 
H        0.989366   -0.909480    0.000000 

