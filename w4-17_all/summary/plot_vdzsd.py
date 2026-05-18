import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------- load data ----------

afqmc = {}   # mol -> (energy, err)
with open('all_vdzsd.dat') as f:
    for line in f.readlines()[2:]:
        p = line.split()
        if not p: continue
        afqmc[p[0]] = (float(p[7]), float(p[8]))

mol_order = []
ref = {}     # mol -> (uhf_ccsdt_t, uhf_uccsdt, ccsdt_q)
with open('reference_vdzsd.dat') as f:
    for line in f.readlines()[2:]:
        p = line.split()
        if not p or p[0].startswith('#'): continue
        mol_order.append(p[0])
        ref[p[0]] = (float(p[3]), float(p[4]), float(p[5]))

n = len(mol_order)

# ---------- compute differences vs CCSDT(Q) in mEh ----------

diff_afqmc  = []
err_afqmc   = []
diff_ccsdt_t = []
diff_uccsdt  = []

for mol in mol_order:
    ccsdt_q = ref[mol][2]
    diff_afqmc.append((afqmc[mol][0] - ccsdt_q) * 1000)
    err_afqmc.append(afqmc[mol][1] * 1000)
    diff_ccsdt_t.append((ref[mol][0] - ccsdt_q) * 1000)
    diff_uccsdt.append((ref[mol][1]  - ccsdt_q) * 1000)

def rmsd(diffs):
    return math.sqrt(sum(d**2 for d in diffs) / len(diffs))

rmsd_afqmc   = rmsd(diff_afqmc)
rmsd_ccsdt_t = rmsd(diff_ccsdt_t)
rmsd_uccsdt  = rmsd(diff_uccsdt)

# ---------- plot ----------

xs = list(range(n))

fig, ax = plt.subplots(figsize=(28, 7))

ax.errorbar(xs, diff_afqmc, yerr=err_afqmc, fmt='o-', markersize=3, linewidth=0.7,
            color='tab:blue', ecolor='tab:blue', elinewidth=0.8, capsize=2,
            label=f'AFQMC  (RMSD = {rmsd_afqmc:.2f} mEh)')
ax.plot(xs, diff_ccsdt_t, 's-', markersize=3, linewidth=0.7, color='tab:orange',
        label=f'UHF-UCCSD(T)  (RMSD = {rmsd_ccsdt_t:.2f} mEh)')
ax.plot(xs, diff_uccsdt,  '^-', markersize=3, linewidth=0.7, color='tab:green',
        label=f'UHF-UCCSDT  (RMSD = {rmsd_uccsdt:.2f} mEh)')

ax.axhline(0, color='k', linewidth=0.6, linestyle='--')
ax.set_xticks(xs)
ax.set_xticklabels(mol_order, rotation=90, fontsize=5)
ax.set_ylabel('E - E[CCSDT(Q)]  (mEh)')
ax.set_title('VDZ(d,s): Deviation from CCSDT(Q)')
ax.legend(fontsize=9)
ax.grid(axis='y', linewidth=0.4, alpha=0.5)

plt.tight_layout()
plt.savefig('vdzsd_vs_ccsdt_q.png', dpi=200)
print("Saved vdzsd_vs_ccsdt_q.png")

print(f"RMSD  AFQMC={rmsd_afqmc:.4f}  UHF-UCCSD(T)={rmsd_ccsdt_t:.4f}  UHF-UCCSDT={rmsd_uccsdt:.4f}  [mEh]")
