%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C       -0.329185    0.684597    0.000000 
C        0.329185   -0.684597    0.000000 
H       -1.431662    0.674507    0.000000 
H        1.431662   -0.674507    0.000000 
O        0.329185    1.696714    0.000000 
O       -0.329185   -1.696714    0.000000 

