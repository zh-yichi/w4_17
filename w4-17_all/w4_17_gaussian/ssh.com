%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
S        0.040128   -0.950243    0.000000 
H       -1.284084   -1.214398    0.000000 
S        0.040128    1.026143    0.000000 

