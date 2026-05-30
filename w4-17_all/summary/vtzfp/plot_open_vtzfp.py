import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------- load data ----------

# open_vtzfp.dat columns:
# [0] Molecule  [1] Shell  [2] E_HF  [3] E_CCSD  [4] E_AFQMC  [5] E_AFQMC_ERR  [6] nelec  [7] norb  [8] Runtime
afqmc = {}   # mol -> (energy, err)
with open('open_vtzfp.dat') as f:
    for line in f.readlines()[2:]:
        p = line.split()
        if not p: continue
        afqmc[p[0]] = (float(p[4]), float(p[5]))

# reference_vtzfp.dat columns:
# [0] Molecule  [1] E_HF  [2] E_CCSD  [3] E_UHF-UCCSD(T)  [4] E_UHF-UCCSDT  [5] E_CCSDT(Q)
mol_order = []
ref = {}     # mol -> (uhf_ccsdt_t, uhf_uccsdt, ccsdt_q)
with open('reference_vtzfp.dat') as f:
    for line in f.readlines()[2:]:
        p = line.split()
        if not p or p[0].startswith('#'): continue
        mol = p[0]
        if mol not in afqmc: continue   # skip closed-shell / atoms
        if len(p) < 6 or p[5] == 'missing': continue
        mol_order.append(mol)
        ref[mol] = (float(p[3]), float(p[4]), float(p[5]))

n = len(mol_order)

# ---------- compute differences vs CCSDT(Q) in mEh ----------

diff_afqmc   = []
err_afqmc    = []
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

def rmsd_uncertainty(diffs, errs):
    r = rmsd(diffs)
    n = len(diffs)
    return math.sqrt(sum(d**2 * s**2 for d, s in zip(diffs, errs))) / (n * r)

rmsd_afqmc     = rmsd(diff_afqmc)
rmsd_afqmc_unc = rmsd_uncertainty(diff_afqmc, err_afqmc)
rmsd_ccsdt_t   = rmsd(diff_ccsdt_t)
rmsd_uccsdt    = rmsd(diff_uccsdt)

# ---------- plot ----------

xs = list(range(n))

fig, ax = plt.subplots(figsize=(14, 6))

ax.errorbar(xs, diff_afqmc, yerr=err_afqmc, fmt='o-', markersize=4, linewidth=0.8,
            color='tab:blue', ecolor='tab:blue', elinewidth=0.8, capsize=2,
            label=f'AFQMC  (RMSD = {rmsd_afqmc:.2f} ± {rmsd_afqmc_unc:.2f} mEh)')
ax.plot(xs, diff_ccsdt_t, 's-', markersize=4, linewidth=0.8, color='tab:orange',
        label=f'UHF-UCCSD(T)  (RMSD = {rmsd_ccsdt_t:.2f} mEh)')
ax.plot(xs, diff_uccsdt,  '^-', markersize=4, linewidth=0.8, color='tab:green',
        label=f'UHF-UCCSDT  (RMSD = {rmsd_uccsdt:.2f} mEh)')

ax.axhline(0, color='k', linewidth=0.6, linestyle='--')
ax.set_xticks(xs)
ax.set_xticklabels(mol_order, rotation=90, fontsize=8)
ax.set_ylabel('E - E[CCSDT(Q)]  (mEh)')
ax.set_title('VTZ(f,p) Open-Shell: Deviation from CCSDT(Q)')
ax.legend(fontsize=9)
ax.grid(axis='y', linewidth=0.4, alpha=0.5)

plt.tight_layout()
plt.savefig('vtzfp_open_vs_ccsdt_q.png', dpi=200)
print("Saved vtzfp_open_vs_ccsdt_q.png")

# ---------- update RMSD summary in reference_vtzfp.dat ----------

with open('reference_vtzfp.dat', 'r') as f:
    content = f.read()
if '\n# RMSD from CCSDT(Q)' in content:
    content = content[:content.index('\n# RMSD from CCSDT(Q)')]
with open('reference_vtzfp.dat', 'w') as f:
    f.write(content)
    f.write('\n')
    f.write('# RMSD from CCSDT(Q) [mEh]  (open-shell W4-17, VTZ(f,p))\n')
    f.write(f'# {"Method":<22} {"RMSD (mEh)":>12}   {"Uncertainty":>12}\n')
    f.write(f'# {"-"*52}\n')
    f.write(f'# {"AFQMC":<22} {rmsd_afqmc:>12.4f}   {rmsd_afqmc_unc:>12.4f}\n')
    f.write(f'# {"UHF-UCCSD(T)":<22} {rmsd_ccsdt_t:>12.4f}\n')
    f.write(f'# {"UHF-UCCSDT":<22} {rmsd_uccsdt:>12.4f}\n')

print(f"RMSD  AFQMC={rmsd_afqmc:.4f}±{rmsd_afqmc_unc:.4f}  UHF-UCCSD(T)={rmsd_ccsdt_t:.4f}  UHF-UCCSDT={rmsd_uccsdt:.4f}  [mEh]")
