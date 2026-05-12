%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
C          0.0000000000        0.0000000000        0.5089253380
O          0.0000000000        0.0000000000        1.6876021361
Cl         0.0000000000        1.4441099963       -0.4670031288
Cl         0.0000000000       -1.4441099963       -0.4670031288

