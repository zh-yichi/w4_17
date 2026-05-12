%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
O        0.061552   -0.592186    0.000000 
C        0.061552    0.586301    0.000000 
H       -0.861727    1.219685    0.000000 

