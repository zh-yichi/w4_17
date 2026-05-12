%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
F        0.000000    0.000000    0.750386 
C        0.000000    0.000000   -0.629363 
H        0.000000    1.026909   -0.992430 
H        0.889329   -0.513454   -0.992430 
H       -0.889329   -0.513454   -0.992430 

