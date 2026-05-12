%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
H        0.000000    1.008140    0.840315 
N        0.000000    0.624028   -0.120045 
N        0.000000   -0.624028   -0.120045 
H        0.000000   -1.008140    0.840315 

