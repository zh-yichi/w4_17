%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
Al       0.000000    0.000000    0.000000 
Cl       0.000000    2.070971    0.000000 
Cl       1.793513   -1.035485    0.000000 
Cl      -1.793513   -1.035485    0.000000 

