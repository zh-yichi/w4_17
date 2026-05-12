%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
S        0.000000    0.000000    0.362207 
O        0.000000    1.239318   -0.362207 
O        0.000000   -1.239318   -0.362207 

