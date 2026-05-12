%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C        0.000000    0.000000   -1.292877 
C        0.000000    0.000000   -0.093379 
H        0.000000    0.000000   -2.354022 
F        0.000000    0.000000    1.185729 

