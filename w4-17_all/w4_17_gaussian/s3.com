%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
S        0.000000    0.000000    0.665312 
S        0.000000    1.640064   -0.332656 
S        0.000000   -1.640064   -0.332656 

