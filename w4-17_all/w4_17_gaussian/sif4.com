%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
F        0.900915    0.900915    0.900915 
Si       0.000000    0.000000    0.000000 
F       -0.900915   -0.900915    0.900915 
F       -0.900915    0.900915   -0.900915 
F        0.900915   -0.900915   -0.900915 

