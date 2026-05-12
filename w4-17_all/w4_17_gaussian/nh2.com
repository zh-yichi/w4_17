%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
N        0.000000    0.000000    0.142235 
H        0.000000    0.800646   -0.497821 
H        0.000000   -0.800646   -0.497821 

