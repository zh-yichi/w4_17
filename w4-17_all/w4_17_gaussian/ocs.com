%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
O        0.000000    0.000000   -1.685171 
C        0.000000    0.000000   -0.526739 
S        0.000000    0.000000    1.040112 

