%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
N       -0.043583    1.126132    0.000000 
H        0.522994    1.365749    0.808624 
H        0.522994    1.365749   -0.808624 
Cl      -0.043583   -0.624378    0.000000 

