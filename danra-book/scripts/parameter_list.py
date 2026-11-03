from pathlib import Path
import xarray as xr
import os
import re

STORE_KINDS = {
    "analysis": "Analysis",
    "forecast_PT3H": "Forecast (3 h)",
    "forecast_PT18H": "Forecast (18 h)",
}


def _format_units(units):
    # e.g. "kg m-2" -> "kg m<sup>-2</sup>"
    return re.sub(r"([a-zA-Z])(-?\d+)", r"\1<sup>\2</sup>", units)


def _retrieve_variable_description(datasets):
    md_lines = [
        "| Variable Name | CF Standard Name | Description | Unit | "
        + " | ".join(STORE_KINDS.values()) + " |",
        "|---------------|------------------|-------------|------|"
        + "|".join(":---:" for _ in STORE_KINDS) + "|",
    ]
    var_names = sorted(
        {var for ds in datasets.values() for var in ds.data_vars} - {"danra_projection"}
    )
    for var in var_names:
        da = next(ds[var] for ds in datasets.values() if var in ds)
        standard_name = da.attrs.get("standard_name", "")
        long_name = da.attrs.get("long_name", "")
        units = _format_units(da.attrs.get("units", ""))
        available = " | ".join(
            "✓" if var in datasets[kind] else "" for kind in STORE_KINDS
        )
        md_lines.append(
            f"| {var} | {standard_name} | {long_name} | {units} | {available} |"
        )
    return md_lines


def _open_level_type(level_type):
    return {
        kind: xr.open_zarr(fp_root / f"{level_type}_{kind}.zarr")
        for kind in STORE_KINDS
    }


fp_root = Path(os.environ.get("DANRA_DATA_PATH"))

ds_danra_sl = _open_level_type("single_levels")
ds_danra_hl = _open_level_type("height_levels")
ds_danra_pl = _open_level_type("pressure_levels")

with open("parameters.md", "w") as f:
    # Single levels
    f.write("# DANRA Parameters\n\n")
    f.write("DANRA output is ordered into three main categories based on the vertical levels of the data: surface or single level (SL), height levels (HL), and pressure levels (PL). Each category contains various meteorological parameters, which are described in detail below.\n\n")
    f.write("<details>\n<summary>Single Levels</summary>\n\n")
    f.write("## Single level parameters\n\n")
    f.write("Single level refers to parameters that are defined at a single vertical level in the atmosphere or at the surface.\n")
    f.write("\n".join(_retrieve_variable_description(ds_danra_sl)))
    f.write("\n</details>\n\n")

    # Height levels
    f.write("<details>\n<summary>Height Levels</summary>\n\n")
    f.write("## Height level parameters\n\n")
    f.write("Height level refers to parameters that are defined at specific vertical levels in the atmosphere.\n")
    heights = ds_danra_hl["analysis"].coords.get("height", None)
    if heights is not None:
        f.write("### Available height levels (m)\n\n")
        f.write(", ".join(str(h.item()) for h in heights.values))
        f.write("\n\n")
    f.write("### Available parameters\n\n")
    f.write("\n".join(_retrieve_variable_description(ds_danra_hl)))
    f.write("\n</details>\n\n")

    # Pressure levels
    f.write("<details>\n<summary>Pressure Levels</summary>\n\n")
    f.write("## Pressure level parameters\n\n")
    f.write("Pressure level refers to parameters that are defined at specific pressure levels in the atmosphere.\n")
    pressures = ds_danra_pl["analysis"].coords.get("pressure", None)
    if pressures is not None:
        f.write("### Available pressure levels (hPa)\n\n")
        f.write(", ".join(str(p.item()) for p in pressures.values))
        f.write("\n\n")
    f.write("### Available parameters\n\n")
    f.write("\n".join(_retrieve_variable_description(ds_danra_pl)))
    f.write("\n</details>\n")
