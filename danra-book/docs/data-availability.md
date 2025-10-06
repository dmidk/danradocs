# Data Availability
DANRA reanalysis consists of gridded data for a large number of weather and climate variables, both at 3-hourly analysis time. Some of the parameters are defined on height or pressure levels, the rest are on a single level.

The DANRA reanalysis data, available at three-hour intervals at 00:00, 03:00, 06:00, ..., and 21:00 UTC daily (analysis data), can be accessed from an Amazon S3 object store. The data is split into three different Zarr datasets:
\begin{itemize}
\item \href{s3://dmi-danra-05/height_levels.zarr}{s3://dmi-danra-05/height\_levels.zarr}
\item \href{s3://dmi-danra-05/single_levels.zarr}{s3://dmi-danra-05/single\_levels.zarr}
\item \href{s3://dmi-danra-05/pressure_levels.zarr}{s3://dmi-danra-05/pressure\_levels.zarr}
\end{itemize}

Fetching one of these datasets with Python and xarray using simple loading is as simple as
<code>
ds_danra_sl = xarray.open_zarr(
    "s3://dmi-danra-05/single_levels.zarr",
    consolidated=True,
    storage_options={
        "anon": True,
    }
)
</code>

Efforts are currently underway to prepare the DANRA forecasts for public release. Once available, the dataset will provide hourly temporal resolution. Updates and further details will be posted on the website.