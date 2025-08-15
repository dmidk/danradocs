from pathlib import Path
import xarray as xr
import os
import re

def _retireve_variable_description(ds):
    md_lines = [
        "| Variable Name | CF Standard Name | Description | Unit |",
        "|---------------|------------------|-------------|------|"
    ]
    for var in ds.data_vars:
        da = ds[var]
        standard_name = da.attrs.get("standard_name", "")
        long_name = da.attrs.get("long_name", "")
        units = da.attrs.get("units", "")
        units = re.sub(r"\*\*(-?\d+)", lambda m: f"<sup>{m.group(1)}</sup>", units)
        md_lines.append(f"| {var} | {standard_name} | {long_name} | {units} |")
    return md_lines

fp_root = Path(os.environ.get("DANRA_DATA_PATH"))

ds_danra_sl = xr.open_zarr(fp_root / "single_levels.zarr")
ds_danra_hl = xr.open_zarr(fp_root / "height_levels.zarr")
ds_danra_pl = xr.open_zarr(fp_root / "pressure_levels.zarr")

with open("parameters.md", "w") as f:
    # Single levels
    f.write("# DANRA Parameters\n\n")
    f.write("DANRA output is ordered into three main categories based on the vertical levels of the data: surface or single level (SL), height levels (HL), and pressure levels (PL). Each category contains various meteorological parameters, which are described in detail below.\n\n")
    f.write("<details>\n<summary>Single Levels</summary>\n\n")
    f.write("## Single level parameters\n\n")
    f.write("Single level refers to parameters that are defined at a single vertical level in the atmosphere or at the surface.\n")
    f.write("\n".join(_retireve_variable_description(ds_danra_sl)))
    f.write("\n</details>\n\n")

    # Height levels
    f.write("<details>\n<summary>Height Levels</summary>\n\n")
    f.write("## Height level parameters\n\n")
    f.write("Height level refers to parameters that are defined at specific vertical levels in the atmosphere.\n")
    altitudes = ds_danra_hl.coords.get("altitude", None)
    if altitudes is not None:
        f.write("### Available height levels (m)\n\n")
        f.write(", ".join(str(a.item()) for a in altitudes.values))
        f.write("\n\n")
    f.write("### Available parameters\n\n")
    f.write("\n".join(_retireve_variable_description(ds_danra_hl)))
    f.write("\n</details>\n\n")

    # Pressure levels
    f.write("<details>\n<summary>Pressure Levels</summary>\n\n")
    f.write("## Pressure level parameters\n\n")
    f.write("Pressure level refers to parameters that are defined at specific pressure levels in the atmosphere.\n")
    pressures = ds_danra_pl.coords.get("pressure", None)
    if pressures is not None:
        f.write("### Available pressure levels (hPa)\n\n")
        f.write(", ".join(str(p.item()) for p in pressures.values))
        f.write("\n\n")
    f.write("### Available parameters\n\n")
    f.write("\n".join(_retireve_variable_description(ds_danra_pl)))
    f.write("\n</details>\n")