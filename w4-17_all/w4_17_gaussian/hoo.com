%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
O        0.055329    0.718293    0.000000 
O        0.055329   -0.611983    0.000000 
H       -0.885259   -0.850475    0.000000 

