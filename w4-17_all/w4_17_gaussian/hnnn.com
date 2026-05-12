%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
H        1.078972   -1.381810    0.000000 
N        0.093770   -1.129880    0.000000 
N        0.000000    0.111098    0.000000 
N       -0.247909    1.216183    0.000000 

