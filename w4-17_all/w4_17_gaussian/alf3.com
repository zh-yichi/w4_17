%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
Al       0.000000    0.000000    0.000000 
F        0.000000    1.631766    0.000000 
F        1.413150   -0.815883    0.000000 
F       -1.413150   -0.815883    0.000000 

