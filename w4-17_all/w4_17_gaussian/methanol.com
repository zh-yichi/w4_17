%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C       -0.046573    0.662925    0.000000 
H       -1.087867    0.977315    0.000000 
H        0.437742    1.073831    0.889854 
H        0.437742    1.073831   -0.889854 
O       -0.046573   -0.756341    0.000000 
H        0.864403   -1.051800    0.000000 

