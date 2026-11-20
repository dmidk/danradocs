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
DANRA reanalysis consists of gridded data for a large number of weather and climate variables at 3-hourly analysis time (00:00, 03:00, 06:00, ..., and 21:00 UTC), as well as hourly forecasts started from the analyses. Some of the parameters are defined on height or pressure levels, the rest are on a single level.

The current version of the data is v0.6.1. If you have used the previous version, v0.5.0, see [Changes since v0.5.0](changes-v0.6.1.md).

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

Alternatively, the data can be accessed directly from the S3 object store. For each of the single level, height level and pressure level data there are three datasets:

| Dataset | Content | Dimensions |
|---------|---------|------------|
| `*_analysis.zarr` | Analysis every 3 hours | `time` |
| `*_forecast_PT3H.zarr` | Forecasts started from every analysis (every 3 hours), lead times 1 to 3 hours | `analysis_time`, `forecast_period` |
| `*_forecast_PT18H.zarr` | Forecasts started at 00 and 12 UTC, lead times 1 to 18 hours | `analysis_time`, `forecast_period` |

The forecast datasets have the time a forecast was started (`analysis_time`) and the lead time (`forecast_period`) as dimensions. The time each value is valid for is given by the coordinate `valid_time = analysis_time + forecast_period`.
Some parameters, such as accumulated precipitation, are only available in the forecasts; see [Details about parameters](data-details.md).

- [s3://dmi-danra-061/single_levels_analysis.zarr](s3://dmi-danra-061/single_levels_analysis.zarr)
- [s3://dmi-danra-061/single_levels_forecast_PT3H.zarr](s3://dmi-danra-061/single_levels_forecast_PT3H.zarr)
- [s3://dmi-danra-061/single_levels_forecast_PT18H.zarr](s3://dmi-danra-061/single_levels_forecast_PT18H.zarr)
- [s3://dmi-danra-061/height_levels_analysis.zarr](s3://dmi-danra-061/height_levels_analysis.zarr)
- [s3://dmi-danra-061/height_levels_forecast_PT3H.zarr](s3://dmi-danra-061/height_levels_forecast_PT3H.zarr)
- [s3://dmi-danra-061/height_levels_forecast_PT18H.zarr](s3://dmi-danra-061/height_levels_forecast_PT18H.zarr)
- [s3://dmi-danra-061/pressure_levels_analysis.zarr](s3://dmi-danra-061/pressure_levels_analysis.zarr)
- [s3://dmi-danra-061/pressure_levels_forecast_PT3H.zarr](s3://dmi-danra-061/pressure_levels_forecast_PT3H.zarr)
- [s3://dmi-danra-061/pressure_levels_forecast_PT18H.zarr](s3://dmi-danra-061/pressure_levels_forecast_PT18H.zarr)

Fetching one of these datasets with Python and xarray using simple loading is as simple as
```
import xarray
ds_danra_sl = xarray.open_zarr(
    "s3://dmi-danra-061/single_levels_analysis.zarr",
    consolidated=True,
    storage_options={
        "anon": True,
    }
)
```
