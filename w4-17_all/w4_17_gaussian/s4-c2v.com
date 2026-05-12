%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
S        0.000000    1.552343    0.921961 
S        0.000000    1.068508   -0.921961 
S        0.000000   -1.068508   -0.921961 
S        0.000000   -1.552343    0.921961 

