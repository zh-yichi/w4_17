%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
O        1.174393    0.194313    0.000000 
O        0.000000    0.553180    0.000000 
O       -0.950471   -0.717715    0.000000 
H       -1.791374   -0.238229    0.000000 

