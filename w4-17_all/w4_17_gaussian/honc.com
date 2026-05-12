%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
H        0.931463   -1.340471    0.000000 
O       -0.002788   -1.095226    0.000000 
N        0.000000    0.238268    0.000000 
C       -0.151527    1.405734    0.000000 

