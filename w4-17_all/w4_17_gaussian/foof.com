%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
F        0.555710    1.384434   -0.493986 
O        0.555710    0.268181    0.555734 
O       -0.555710   -0.268181    0.555734 
F       -0.555710   -1.384434   -0.493986 

