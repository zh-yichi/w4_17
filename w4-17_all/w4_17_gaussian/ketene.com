%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C        0.000000    0.000000   -1.212911 
H        0.000000    0.941658   -1.736011 
H        0.000000   -0.941658   -1.736011 
C        0.000000    0.000000    0.103124 
O        0.000000    0.000000    1.266343 

