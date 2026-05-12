#!/usr/bin/env python3
"""Convert Gaussian .com input files to .xyz molecular geometry format."""

import os
import re
import glob

xyz_dir = os.path.dirname(os.path.abspath(__file__))
com_files = glob.glob(os.path.join(xyz_dir, "*.com"))

converted = 0
failed = []

for com_path in sorted(com_files):
    mol_name = os.path.splitext(os.path.basename(com_path))[0]
    xyz_path = os.path.join(xyz_dir, mol_name + ".xyz")

    with open(com_path) as f:
        lines = f.readlines()

    # Find the charge/multiplicity line: two integers on a line by themselves
    # It appears after the blank line following the title comment
    charge_mult_idx = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if re.fullmatch(r'-?\d+\s+-?\d+', stripped):
            charge_mult_idx = i
            break

    if charge_mult_idx is None:
        failed.append(mol_name)
        print(f"  SKIP {mol_name}: could not find charge/multiplicity line")
        continue

    # Read coordinate lines after charge/multiplicity until blank line or EOF
    coord_lines = []
    for line in lines[charge_mult_idx + 1:]:
        stripped = line.strip()
        if not stripped:
            break
        # Each coordinate line: element x y z
        parts = stripped.split()
        if len(parts) >= 4:
            coord_lines.append(f"{parts[0]:<4s} {parts[1]:>14s} {parts[2]:>14s} {parts[3]:>14s}\n")
        elif len(parts) == 1:
            # Single atom with no coordinates (rare), place at origin
            coord_lines.append(f"{parts[0]:<4s} {'0.000000':>14s} {'0.000000':>14s} {'0.000000':>14s}\n")

    if not coord_lines:
        failed.append(mol_name)
        print(f"  SKIP {mol_name}: no coordinate lines found")
        continue

    with open(xyz_path, "w") as f:
        f.write(f"{len(coord_lines)}\n")
        f.write(f"{mol_name}\n")
        f.writelines(coord_lines)

    converted += 1

print(f"\nConverted {converted} files.")
if failed:
    print(f"Failed ({len(failed)}): {', '.join(failed)}")
