%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
H        0.788278    0.891936    0.468613 
O        0.000000    0.726241   -0.058577 
O        0.000000   -0.726241   -0.058577 
H       -0.788278   -0.891936    0.468613 

