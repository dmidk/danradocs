#!/usr/bin/env python3
"""Script to check data availability for DANRA intake catalog."""

import sys

import intake


def main():
    """Load the catalog and try to load each dataset as dask array."""
    try:
        cat = intake.open_catalog("catalog/catalog.yaml")
        print("Catalog opened successfully.")
    except Exception as e:
        print(f"Failed to open catalog: {e}")
        sys.exit(1)

    failures = []

    for name in cat:
        try:
            _ = cat[name].to_dask()
            print(f"{name}: OK")
        except Exception as e:
            print(f"{name}: FAILED - {e}")
            failures.append(name)

    if failures:
        print(f"Failed datasets: {', '.join(failures)}")
        sys.exit(1)
    else:
        print("All datasets available.")


if __name__ == "__main__":
    main()
