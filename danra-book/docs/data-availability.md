---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.17.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
execution:
  timeout: 120
---

# Data Availability
DANRA reanalysis consists of gridded data for a large number of weather and climate variables at 3-hourly analysis time (00:00, 03:00, 06:00, ..., and 21:00 UTC). Some of the parameters are defined on height or pressure levels, the rest are on a single level.

The datasets can be accessed via an [Intake catalog](https://intake.readthedocs.io/en/latest/catalog.html) published at [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17294180.svg)](https://doi.org/10.5281/zenodo.17294180)

```{code-cell} ipython3
import intake
cat = intake.open_catalog("zip://dmidk-danradocs-a856614/catalog/catalog.yaml::https://zenodo.org/records/17294180/files/dmidk/danradocs-v0.2.2.zip", driver="yaml_file_cat")
list(cat)
```

Individual datasets can be loaded with xarray via the catalog:

```{code-cell} ipython3
ds_danra_sl = cat.single_levels.to_dask()
ds_danra_sl
```

Alternatively, the data can be accessed directly from the S3 object store:

- [s3://dmi-danra-05/height_levels.zarr](https://registry.opendata.aws/dmi-danra-05/)
- [s3://dmi-danra-05/single_levels.zarr](https://registry.opendata.aws/dmi-danra-05/)
- [s3://dmi-danra-05/pressure_levels.zarr](https://registry.opendata.aws/dmi-danra-05/)

Fetching one of these datasets with Python and xarray using simple loading is as simple as
```
import xarray
ds_danra_sl = xarray.open_zarr(
    "s3://dmi-danra-05/single_levels.zarr",
    consolidated=True,
    storage_options={
        "anon": True,
    }
)
```

Efforts are currently underway to prepare the DANRA forecasts for public release. Once available, the dataset will provide hourly temporal resolution. Updates and further details will be posted on the website.
