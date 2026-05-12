%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
N        0.062619    0.584988    0.000000 
H       -0.939290    0.910719    0.000000 
O        0.062619   -0.625704    0.000000 

