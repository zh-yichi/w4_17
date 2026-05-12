%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C          0.0030519039        0.5051306554        0.0000000000
O         -0.7959430261        1.3672029009        0.0000000000
F          1.3116501168        0.7061565175        0.0000000000
Cl        -0.3206169946       -1.1912890738        0.0000000000

