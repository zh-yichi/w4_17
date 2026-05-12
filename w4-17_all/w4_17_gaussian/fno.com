%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
F          0.0000000000        0.1416613496       -1.0954204878
N          0.0000000000       -0.5118207938        0.2593665757
O          0.0000000000        0.2798593012        1.0736883924

