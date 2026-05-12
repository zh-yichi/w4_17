%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C        0.122314    0.743301    0.000000 
H       -0.950472    1.063696    0.000000 
O        0.122314   -0.569682    0.000000 
H       -0.761926   -0.966045    0.000000 

