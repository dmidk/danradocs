# Details about parameters
This section describes special parameters in the DANRA dataset. 

## DANRA Parameters

DANRA output is ordered into three main categories based on the vertical levels of the data: surface or single level (SL), height levels (HL), and pressure levels (PL). Each category contains various meteorological parameters, which are described in detail below.
Each category is available as an analysis dataset and two forecast datasets (see [Data availability](data-availability.md)); the tables below show which parameters are available in which dataset.

```{include} parameters.md
```


<details>
<summary>Special Parameters</summary>
<h2> Special parameters</h2>
The following parameters are encoded using a different schema than WMO standards. Thus, we provide a brief description of those below.

<h3>Precipitation type</h3>
The precipitation type, <code>prtp</code>, describes the most prevalent type of precipitation in the given time frame. Where there is no precipitation the value is missing (NaN). The following types are available:

| Code | Description |
|------|-------------|
| 0    | Drizzle |
| 1    | Rain |
| 2    | Sleet |
| 3    | Snow |
| 4    | Freezing drizzle |
| 5    | Freezing rain |
| 6    | Graupel |
| 7    | Hail |

<h3>Icing index</h3>
The icing index, <code>icei</code>, is a measure of the risk of icing in the atmosphere. The index is calculated as the maximum risk of icing somewhere in the atmosphere column. The index is an integer between 1 and 4, corresponding to the following risk levels. Where there is no risk of icing the value is missing (NaN).

| Code | Description |
|------|-------------|
| 1    | Trace |
| 2    | Light |
| 3    | Moderate |
| 4    | Severe | 

<h3>AROME Hail diagnostic</h3>
The hail diagnostic, <code>xhail</code>, is a measure of the risk of hail. It is the maximum total column graupel in kg/m^2 since previous post-processing. Values above 16 kg/m^2 are considered to be a risk of hail.
<h3>Missing values</h3>
Some parameters are only defined in part of the domain or under certain conditions. Where they are undefined, the value is missing and is read as NaN by xarray:

- <code>cb_column</code> and <code>ct_column</code>: where there are no clouds.
- <code>prtp</code>: where there is no precipitation.
- <code>icei</code>: where there is no risk of icing.
- <code>albedo</code>, <code>soil_ice</code>, <code>soil_moisture</code>, <code>surface_soil_moisture</code>, <code>soil_temperature</code> and <code>t_surface_isba</code>: outside the land surface scheme, i.e. over sea. Use the missing values, not <code>lsm</code>, to find where these are valid, since the land surface scheme also covers some points that <code>lsm</code> classifies as sea.

<h3>Surface temperatures</h3>

- <code>t0m</code> is the surface (skin) temperature, averaged over all surface types in the grid box.
- <code>t_surface_isba</code> is the surface (skin) temperature of the land surface only.
- <code>soil_temperature</code> is the mean temperature of the root-zone soil layer.

<h3>Radiation</h3>
The instantaneous and accumulated radiation parameters hold different quantities, even where their names are similar:

| Parameter | Quantity |
|-----------|----------|
| <code>lwavr</code> | Net surface long-wave radiation (downwelling minus upwelling) |
| <code>swavr</code> | Net surface short-wave radiation (downwelling minus reflected) |
| <code>lwavr_accum_past_hr</code> | Downwelling surface long-wave radiation |
| <code>swavr_accum_past_hr</code> | Direct (beam) short-wave radiation on a horizontal surface |
| <code>grad_accum_past_hr</code> | Global radiation: direct plus diffuse downwelling short-wave radiation |
| <code>dni_accum_past_hr</code> | Direct normal irradiance, perpendicular to the solar beam |
| <code>nlwrs_accum_past_hr</code> | Net surface long-wave radiation |
| <code>nswrs_accum_past_hr</code> | Net surface short-wave radiation |

<code>albedo</code> is only valid in daylight.

<h3>Accumulated and interval parameters</h3>
These are only available in the forecast datasets.

- <code>*_accum_past_hr</code> parameters are accumulated over the hour ending at the valid time. Radiation and heat fluxes are therefore in W s m<sup>-2</sup> (J m<sup>-2</sup>); divide by 3600 to get the mean flux in W m<sup>-2</sup>. Precipitation amounts are in kg m<sup>-2</sup>, which is equal to mm. Very small negative values can occur due to numerical noise.
- <code>ugst10m_past_hr</code> and <code>vgst10m_past_hr</code> are the components of the maximum wind gust over the hour ending at the valid time.
- <code>tmax2m_since_analysis</code> and <code>tmin2m_since_analysis</code> are the maximum and minimum 2 m temperature since the start of the forecast, so the period they cover grows with the lead time.

<h3>Sign conventions</h3>
The surface fluxes <code>wevap_accum_past_hr</code>, <code>snsub_accum_past_hr</code>, <code>lhe_accum_past_hr</code>, <code>lhsub_accum_past_hr</code> and <code>sshf_accum_past_hr</code> are positive downwards, so evaporation, sublimation and upward heat fluxes are negative.
The momentum fluxes <code>uflx_accum_past_hr</code> and <code>vflx_accum_past_hr</code> are positive upwards, so they are negative under a westerly and southerly wind, respectively.

<h3>Freezing level</h3>
<code>freezing_height</code> is the height of the 0 °C isotherm. Where the whole atmospheric column is below freezing, the value is extrapolated below the surface and can be negative.
</details>