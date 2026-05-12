%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
P        0.777375    0.777375    0.777375 
P       -0.777375   -0.777375    0.777375 
P       -0.777375    0.777375   -0.777375 
P        0.777375   -0.777375   -0.777375 

