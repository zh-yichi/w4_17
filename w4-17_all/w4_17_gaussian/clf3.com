%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
Cl         0.0000000000        0.0000000000       -0.3702953502
F          0.0000000000        0.0000000000        1.2281947837
F          0.0000000000        1.6940358443       -0.2862224368
F          0.0000000000       -1.6940358443       -0.2862224368


