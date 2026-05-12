%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 2
H        0.876819   -0.987844    0.000000 
N       -0.062630   -0.519017    0.000000 
N       -0.062630    0.660138    0.000000 

