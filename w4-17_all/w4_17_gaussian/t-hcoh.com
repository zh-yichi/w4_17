%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C        0.010522    0.742943    0.000000 
H       -1.077050    0.977417    0.000000 
O        0.010522   -0.571411    0.000000 
H        0.929743   -0.863789    0.000000 

