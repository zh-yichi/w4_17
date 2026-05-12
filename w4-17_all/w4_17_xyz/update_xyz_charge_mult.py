#!/usr/bin/env python3
"""Add charge and spin multiplicity from Gaussian .com files to .xyz comment lines."""

import os
import re
import glob

gaussian_dir = "/home/sharmagroup/sharmagroup/project/w4_17/w4-17_all/w4_17_gaussian"
xyz_dirs = [
    "/home/sharmagroup/sharmagroup/project/w4_17/w4-17_all/w4_17_xyz/mol",
    "/home/sharmagroup/sharmagroup/project/w4_17/w4-17_all/w4_17_xyz/atom",
]

# Extract charge and multiplicity from every .com file
charge_mult = {}
for com_path in glob.glob(os.path.join(gaussian_dir, "*.com")):
    name = os.path.splitext(os.path.basename(com_path))[0]
    with open(com_path) as f:
        for line in f:
            m = re.fullmatch(r'\s*(-?\d+)\s+(\d+)\s*', line)
            if m:
                charge_mult[name] = (int(m.group(1)), int(m.group(2)))
                break

updated = 0
missing = []

for xyz_dir in xyz_dirs:
    for xyz_path in sorted(glob.glob(os.path.join(xyz_dir, "*.xyz"))):
        name = os.path.splitext(os.path.basename(xyz_path))[0]

        if name not in charge_mult:
            missing.append(name)
            continue

        charge, mult = charge_mult[name]

        with open(xyz_path) as f:
            lines = f.readlines()

        # Replace second line (comment) with: name charge=X mult=Y
        lines[1] = f"{name} charge={charge} mult={mult}\n"

        with open(xyz_path, "w") as f:
            f.writelines(lines)

        updated += 1

print(f"Updated {updated} files.")
if missing:
    print(f"No Gaussian data found for: {', '.join(missing)}")
