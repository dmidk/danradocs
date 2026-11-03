# Changes since v0.5.0

DANRA v0.6.1 replaces the previously published v0.5.0 datasets. It adds the hourly forecasts and corrects a number of names, units and descriptions in the metadata.
Apart from missing values (see below), the data values for the period covered by v0.5.0 are unchanged. However, some of the changes require updates to existing code, and some may affect results computed with v0.5.0.

## New location and datasets

The data has moved to a new S3 bucket, `s3://dmi-danra-061`, and each of the three v0.5.0 datasets is now split into an analysis dataset and two forecast datasets:

| v0.5.0 | v0.6.1 |
|--------|--------|
| `s3://dmi-danra-05/single_levels.zarr` | `s3://dmi-danra-061/single_levels_analysis.zarr` |
| `s3://dmi-danra-05/height_levels.zarr` | `s3://dmi-danra-061/height_levels_analysis.zarr` |
| `s3://dmi-danra-05/pressure_levels.zarr` | `s3://dmi-danra-061/pressure_levels_analysis.zarr` |
| | `s3://dmi-danra-061/{single,height,pressure}_levels_forecast_PT3H.zarr` |
| | `s3://dmi-danra-061/{single,height,pressure}_levels_forecast_PT18H.zarr` |

The analysis datasets correspond to the v0.5.0 datasets, but now cover the full period up to 2023-12-31 21:00 UTC (v0.5.0 ended on 2023-10-13 21:00 UTC). The forecast datasets are new; see [Data availability](data-availability.md).

## Renamed variables and coordinates

Code using the old names must be updated:

| v0.5.0 | v0.6.1 |
|--------|--------|
| `altitude` (height level coordinate) | `height` |
| `orography` | `surface_geopotential` |
| `sf0m` | `snow_water_equivalent` |
| `hcc0m`, `icei0m`, `lcc0m`, `lwavr0m`, `mcc0m`, `mld0m`, `prtp0m`, `psct0m`, `pscw0m`, `pstb0m`, `pstbc0m`, `swavr0m`, `tcc0m`, `xhail0m` | the same names without `0m`, e.g. `tcc` |

## Changes that may affect your results

If you used any of the following with v0.5.0, check your results:

- **Missing values in `cb_column`, `ct_column`, `prtp` and `icei`.** In v0.5.0, undefined points (e.g. cloud base where there are no clouds) had the value 9999, which was not marked as missing. These are now read as NaN. Statistics computed in v0.5.0 that included the 9999 values are wrong, and code that checks for `== 9999` should use `isnull()` instead.
- **`ciwc` and `cwat`** are the mass fractions of cloud ice and cloud water on each pressure level, in kg kg<sup>-1</sup>. v0.5.0 incorrectly described them as column totals in kg m<sup>-2</sup>.
- **`lwavr` and `swavr`** are the net surface long-wave and short-wave radiation (downward positive). v0.5.0 did not say which radiation flux they were.
- **`t0m`** is the surface (skin) temperature, not the air temperature at the surface, and **`pres0m`** is the surface air pressure.
- **`snow_water_equivalent`** (`sf0m` in v0.5.0) is the amount of snow on the ground, not snowfall. Hourly snowfall is available in the forecasts as `snow_accum_past_hr`.
- **`psct`** is an infrared brightness temperature. It is the cloud top temperature where there are clouds, but the ground temperature in clear sky.
- **`r` and `r2m`** are fractions between 0 and 1. v0.5.0 gave the unit as %, but the values were the same.
- **`u`, `v`, `u10m` and `v10m`** are eastward and northward wind components. v0.5.0 described them as relative to the model grid, but the values were already rotated to east and north, so they should not be rotated again.
- **The map projection.** The CF attributes on `danra_projection` (`standard_parallel`, `latitude_of_projection_origin` and `longitude_of_central_meridian`) were a factor 1000 too small in v0.5.0. Tools that build the projection from these attributes, such as `pyproj.CRS.from_cf`, `cf_xarray`, `rioxarray` or `metpy`, would have produced wrong coordinates. The `crs_wkt` attribute, and the `lat` and `lon` coordinates, were correct.

## Other metadata changes

These do not change the meaning of the data, but may matter if your code reads the metadata:

- Units are written without `**`, e.g. `m s-1` instead of `m s**-1`.
- `prtp`, `icei` and `pscw` have the unit `1`, and `pstb` and `pstbc` have the unit `K`, instead of `-`.
- `prtp` and `icei` have `flag_values` and `flag_meanings` attributes describing their categories.
- Several standard names and descriptions have been corrected. See [Details about parameters](data-details.md) for the current metadata.

## New variables

The pressure and height level datasets contain the same variables as in v0.5.0. The single level datasets have 39 new variables:

- **In the analysis and forecasts:** `fog`, `freezing_height`, `nlwrt_toa`, `nswrt_toa`, `q2m`, `wdir10m`, `ws10m`, and from the land surface scheme `albedo`, `roughness_length`, `thermal_roughness_length`, `surface_soil_moisture`, `soil_moisture`, `soil_ice`, `soil_temperature` and `t_surface_isba`. The land surface variables are not in the 18-hourly forecasts.
- **In the forecasts only:** hourly accumulations such as precipitation (`*_accum_past_hr`), wind gusts (`ugst10m_past_hr`, `vgst10m_past_hr`), and maximum and minimum temperature (`tmax2m_since_analysis`, `tmin2m_since_analysis`).

See [Details about parameters](data-details.md) for the full list.
