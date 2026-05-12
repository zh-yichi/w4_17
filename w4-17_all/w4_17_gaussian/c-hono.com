%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
O        1.083192    0.071129    0.000000 
N        0.000000    0.549439    0.000000 
O       -1.014443   -0.395320    0.000000 
H       -0.549996   -1.252549    0.000000 

