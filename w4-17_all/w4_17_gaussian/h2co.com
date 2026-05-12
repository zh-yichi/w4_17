%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
O        0.000000    0.000000    0.675860 
C        0.000000    0.000000   -0.530740 
H        0.000000    0.936954   -1.111223 
H        0.000000   -0.936954   -1.111223 

