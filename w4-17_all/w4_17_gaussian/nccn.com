%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
N        0.000000    0.000000    1.855199 
C        0.000000    0.000000    0.693922 
C        0.000000    0.000000   -0.693922 
N        0.000000    0.000000   -1.855199 

