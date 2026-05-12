%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
Cl         0.0000000000        0.0000000000       -0.9564841886
C          0.0000000000        0.0000000000        0.6845061795
C          0.0000000000        0.0000000000        1.8908995350
H          0.0000000000        0.0000000000        2.9535844400

