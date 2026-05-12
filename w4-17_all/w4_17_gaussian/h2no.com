%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
O         -0.0028254588       -0.7318919999        0.0000000000
N         -0.0449006547        0.5427187816        0.0000000000
H          0.1017220568        1.0348341092        0.8712108022
H          0.1017220568        1.0348341092       -0.8712108022

