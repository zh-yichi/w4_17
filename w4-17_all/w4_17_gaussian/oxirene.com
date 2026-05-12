%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C        0.000000    0.635515   -0.462952 
C        0.000000   -0.635515   -0.462952 
H        0.000000   -1.652256   -0.793740 
H        0.000000    1.652256   -0.793740 
O        0.000000    0.000000    0.892862 

