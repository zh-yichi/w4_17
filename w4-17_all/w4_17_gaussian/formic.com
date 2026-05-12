%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C        0.000000    0.421944    0.000000 
H       -0.374304    1.449673    0.000000 
O        1.157954    0.108822    0.000000 
O       -1.030349   -0.440495    0.000000 
H       -0.646531   -1.327950    0.000000 

