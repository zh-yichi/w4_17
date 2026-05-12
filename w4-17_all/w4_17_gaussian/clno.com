%nproc=8
%mem=5000mb
#p hf/6-31G(d) scf=tight int(grid=ultrafine)  scfcyc=200 symm=tight

This text is a comment

0 1
Cl         0.0000000000        0.0591798781       -1.0439566306
N          0.0000000000       -0.5296837735        0.8378261577
O          0.0000000000        0.3325760649        1.5798226671

