%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
S       -0.726771   -1.075032    0.000000 
S        0.000000    0.671244    0.000000 
O        1.453541    0.807576    0.000000 

