%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
O        0.036173    1.099619    0.000000 
H       -0.904317    1.310761    0.000000 
Cl       0.036173   -0.594571    0.000000 

