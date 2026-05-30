import csv
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------- load data ----------

mol_order = []
delta_afqmc   = []
err_afqmc     = []
delta_ccsdt_t = []
delta_uccsdt  = []

with open('atomization_energies_vdzsd.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        mol_order.append(row['molecule'])
        delta_afqmc.append(float(row['delta_AFQMC_kcal']))
        err_afqmc.append(float(row['AE_AFQMC_err_kcal']))
        delta_ccsdt_t.append(float(row['delta_UHF-CCSD(T)_kcal']))
        delta_uccsdt.append(float(row['delta_UHF-CCSDT_kcal']))

n = len(mol_order)

# ---------- compute RMSD ----------

def rmsd(diffs):
    return math.sqrt(sum(d**2 for d in diffs) / len(diffs))

def rmsd_uncertainty(diffs, errs):
    r = rmsd(diffs)
    return math.sqrt(sum(d**2 * s**2 for d, s in zip(diffs, errs))) / (len(diffs) * r)

rmsd_afqmc     = rmsd(delta_afqmc)
rmsd_afqmc_unc = rmsd_uncertainty(delta_afqmc, err_afqmc)
rmsd_ccsdt_t   = rmsd(delta_ccsdt_t)
rmsd_uccsdt    = rmsd(delta_uccsdt)

# ---------- plot ----------

xs = list(range(n))

fig, ax = plt.subplots(figsize=(28, 7))

ax.errorbar(xs, delta_afqmc, yerr=err_afqmc, fmt='o-', markersize=3, linewidth=0.7,
            color='tab:blue', ecolor='tab:blue', elinewidth=0.8, capsize=2,
            label=f'AFQMC  (RMSD = {rmsd_afqmc:.3f} ± {rmsd_afqmc_unc:.3f} kcal/mol)')
ax.plot(xs, delta_ccsdt_t, 's-', markersize=3, linewidth=0.7, color='tab:orange',
        label=f'UHF-CCSD(T)  (RMSD = {rmsd_ccsdt_t:.3f} kcal/mol)')
ax.plot(xs, delta_uccsdt, '^-', markersize=3, linewidth=0.7, color='tab:green',
        label=f'UHF-CCSDT  (RMSD = {rmsd_uccsdt:.3f} kcal/mol)')

ax.axhline(0, color='k', linewidth=0.6, linestyle='--')
ax.set_xticks(xs)
ax.set_xticklabels(mol_order, rotation=90, fontsize=5)
ax.set_ylabel('AE - AE[CCSDT(Q)]  (kcal/mol)')
ax.set_title('VDZ(d,s): Atomization Energy Deviation from CCSDT(Q)')
ax.legend(fontsize=9)
ax.grid(axis='y', linewidth=0.4, alpha=0.5)

plt.tight_layout()
plt.savefig('atomization_deviations_from_ccsdtq_vdzsd.png', dpi=200)
print("Saved atomization_deviations_from_ccsdtq_vdzsd.png")
print(f"RMSD  AFQMC={rmsd_afqmc:.4f}±{rmsd_afqmc_unc:.4f}  UHF-CCSD(T)={rmsd_ccsdt_t:.4f}  UHF-CCSDT={rmsd_uccsdt:.4f}  [kcal/mol]")
