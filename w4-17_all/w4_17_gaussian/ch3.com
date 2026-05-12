%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
C        0.000000    0.000000    0.000000 
H        0.000000    1.077700    0.000000 
H        0.933316   -0.538850    0.000000 
H       -0.933316   -0.538850    0.000000 

