%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C        1.186000   -0.155452    0.000000 
C        0.000000    0.435875    0.000000 
H        1.277837   -1.231598    0.000000 
H        2.074598    0.456585    0.000000 
H       -0.175306    1.502406    0.000000 
F       -1.143681   -0.267771    0.000000 

