%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
C        0.000391    0.650313    0.000000 
H        0.897827    1.274311    0.000000 
N        0.000391   -0.588278    0.000000 
H       -0.902908   -1.058244    0.000000 

