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


def _dropdown(summary, title, description, datasets, levels=None):
    """One collapsible section of the parameter tables.

    Raw HTML headings are used instead of markdown headings, since a markdown
    heading starts a new section and would break the <details> block.
    """
    lines = [
        "<details>",
        f"<summary>{summary}</summary>",
        "",
        f"<h3>{title}</h3>",
        "",
        description,
        "",
    ]
    if levels is not None:
        label, values = levels
        lines += [
            f"<h4>{label}</h4>",
            "",
            ", ".join(str(v.item()) for v in values),
            "",
            "<h4>Available parameters</h4>",
            "",
        ]
    lines += _retrieve_variable_description(datasets)
    lines += ["", "</details>"]
    return "\n".join(lines)


sections = [
    _dropdown(
        "Single Levels",
        "Single level parameters",
        "Single level refers to parameters that are defined at a single "
        "vertical level in the atmosphere or at the surface.",
        ds_danra_sl,
    ),
    _dropdown(
        "Height Levels",
        "Height level parameters",
        "Height level refers to parameters that are defined at specific "
        "vertical levels in the atmosphere.",
        ds_danra_hl,
        levels=(
            "Available height levels (meters above ground)",
            ds_danra_hl["analysis"].height.values,
        ),
    ),
    _dropdown(
        "Pressure Levels",
        "Pressure level parameters",
        "Pressure level refers to parameters that are defined at specific "
        "pressure levels in the atmosphere.",
        ds_danra_pl,
        levels=(
            "Available pressure levels (hPa)",
            ds_danra_pl["analysis"].pressure.values,
        ),
    ),
]

# Included from docs/data-details.md
out_path = Path(__file__).parent.parent / "docs" / "parameters.md"
out_path.write_text("\n\n".join(sections) + "\n")
