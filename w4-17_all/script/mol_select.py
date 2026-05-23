import os
import glob


def _parse_index_range(spec):
    """Parse '1-10', '5', or '1,3,5-8' into a sorted list of 1-based ints."""
    indices = set()
    for part in spec.split(','):
        part = part.strip()
        if '-' in part:
            lo, hi = part.split('-', 1)
            indices.update(range(int(lo), int(hi) + 1))
        else:
            indices.add(int(part))
    return sorted(indices)


def get_xyz_files(xyz_dir, select_molecules=None, index=None):
    """Return a filtered, sorted list of .xyz paths from xyz_dir.

    select_molecules : list of molecule name strings, or None for all
    index            : index range string e.g. '1-10', '5', '1,3,5-8', or None for all
    """
    all_xyz = sorted(glob.glob(os.path.join(xyz_dir, '*.xyz')))

    if select_molecules is not None:
        select_set = set(select_molecules)
        all_xyz = [p for p in all_xyz
                   if os.path.splitext(os.path.basename(p))[0] in select_set]
        missing = select_set - {os.path.splitext(os.path.basename(p))[0] for p in all_xyz}
        if missing:
            print(f"Warning: no .xyz found for: {', '.join(sorted(missing))}")

    if index is not None:
        wanted = _parse_index_range(index)
        out_of_range = [i for i in wanted if i < 1 or i > len(all_xyz)]
        if out_of_range:
            print(f"Warning: indices out of range (1–{len(all_xyz)}): {out_of_range}")
        all_xyz = [all_xyz[i - 1] for i in wanted if 1 <= i <= len(all_xyz)]

    print(f"Molecules to run: {len(all_xyz)}")
    for i, p in enumerate(all_xyz, 1):
        print(f"  {i:3d}. {os.path.basename(p)}")

    return all_xyz
