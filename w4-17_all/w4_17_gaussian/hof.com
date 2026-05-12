%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
H       -0.904390    0.840938    0.000000 
O        0.053199    0.710109    0.000000 
F        0.053199   -0.724645    0.000000 

