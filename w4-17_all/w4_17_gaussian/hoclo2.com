%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
H        1.738675    0.159202   -0.584163 
O        1.347986   -0.576413   -0.086822 
Cl      -0.169548    0.032768    0.336138 
O       -1.073915   -0.867672   -0.310144 
O       -0.131116    1.354553   -0.244308 

