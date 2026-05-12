%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
C        0.000000    0.000000   -0.507513 
H        0.000000    0.936731   -1.073924 
H        0.000000   -0.936731   -1.073924 
N        0.000000    0.000000    0.741847 

