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

md_lines = _retireve_variable_description(ds_danra_sl)
with open("danra_sl_variables.md", "w") as f:
    f.write("\n".join(md_lines))

md_lines = []

md_lines = _retireve_variable_description(ds_danra_hl)
with open("danra_hl_variables.md", "w") as f:
    f.write("\n".join(md_lines))

md_lines = []

md_lines = _retireve_variable_description(ds_danra_pl)
with open("danra_pl_variables.md", "w") as f:
    f.write("\n".join(md_lines))