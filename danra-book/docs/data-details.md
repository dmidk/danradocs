# Details about parameters
This section describes special parameters in the DANRA dataset. 

## DANRA Parameters

DANRA output is ordered into three main categories based on the vertical levels of the data: surface or single level (SL), height levels (HL), and pressure levels (PL). Each category contains various meteorological parameters, which are described in detail below.
Each category is available as an analysis dataset and two forecast datasets (see [Data availability](data-availability.md)); the tables below show which parameters are available in which dataset.

<details>
<summary>Single Levels</summary>

<h3>Single level parameters</h3>

Single level refers to parameters that are defined at a single vertical level in the atmosphere or at the surface.
| Variable Name | CF Standard Name | Description | Unit | Analysis | Forecast (3 h) | Forecast (18 h) |
|---------------|------------------|-------------|------|:---:|:---:|:---:|
| albedo | surface_albedo | ISBA total albedo | 1 | ✓ | ✓ |  |
| cape_column | atmosphere_convective_available_potential_energy_wrt_surface | CAPE out of the model | J kg<sup>-1</sup> | ✓ | ✓ | ✓ |
| cb_column | cloud_base_altitude | Cloud base | m | ✓ | ✓ | ✓ |
| ct_column | cloud_top_altitude | Cloud top | m | ✓ | ✓ | ✓ |
| dni_accum_past_hr |  | Direct normal irradiance, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| fog | fog_area_fraction | Fog area fraction | 1 | ✓ | ✓ | ✓ |
| freezing_height | freezing_level_altitude | Height of the 0 degC isotherm | m | ✓ | ✓ | ✓ |
| grad_accum_past_hr | integral_wrt_time_of_surface_downwelling_shortwave_flux_in_air | Global radiation flux, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| grpl_accum_past_hr | graupel_fall_amount | Graupel, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| grpl_column | atmosphere_mass_content_of_graupel | Graupel | kg m<sup>-2</sup> | ✓ | ✓ | ✓ |
| hcc | high_type_cloud_area_fraction | High cloud cover | 1 | ✓ | ✓ | ✓ |
| icei |  | Icing index | 1 | ✓ | ✓ | ✓ |
| lcc | low_type_cloud_area_fraction | Low cloud cover | 1 | ✓ | ✓ | ✓ |
| lhe_accum_past_hr |  | Latent heat flux through evaporation, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| lhsub_accum_past_hr |  | Latent Heat Sublimation, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| lsm | land_binary_mask | Land cover (1=land, 0=sea) | 1 | ✓ |  |  |
| lwavr | surface_net_downward_longwave_flux | Long-wave radiation flux | W m<sup>-2</sup> | ✓ | ✓ | ✓ |
| lwavr_accum_past_hr | integral_wrt_time_of_surface_downwelling_longwave_flux_in_air | Long-wave radiation flux, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| mcc | medium_type_cloud_area_fraction | Medium cloud cover | 1 | ✓ | ✓ | ✓ |
| mld | atmosphere_boundary_layer_thickness | Height of the planetary boundary layer | m | ✓ | ✓ | ✓ |
| nlwrs_accum_past_hr | integral_wrt_time_of_surface_net_downward_longwave_flux | Net long-wave radiation flux (surface), accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| nlwrt_toa | toa_net_downward_longwave_flux | Net long-wave radiation flux (atmosph.top) | W m<sup>-2</sup> | ✓ | ✓ | ✓ |
| nlwrt_toa_accum_past_hr |  | Net long-wave radiation flux (atmosph.top), accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| nswrs_accum_past_hr | integral_wrt_time_of_surface_net_downward_shortwave_flux | Net short-wave radiation flux (surface), accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| nswrt_toa | toa_net_downward_shortwave_flux | Net short-wave radiation flux (atmosph.top) | W m<sup>-2</sup> | ✓ | ✓ | ✓ |
| nswrt_toa_accum_past_hr | integral_wrt_time_of_toa_net_downward_shortwave_flux | Net short-wave radiation flux (atmosph.top), accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| pres0m | surface_air_pressure | Pressure | Pa | ✓ | ✓ | ✓ |
| pres_seasurface | air_pressure_at_mean_sea_level | Mean sea level pressure | Pa | ✓ | ✓ | ✓ |
| prtp | predominant_precipitation_type_at_surface | Precipitation Type | 1 | ✓ | ✓ | ✓ |
| psct | brightness_temperature | Pseudo satellite image: infrared brightness temperature (cloud top where cloudy, ground where clear) | K | ✓ | ✓ | ✓ |
| pscw |  | Pseudo satellite image: cloud water reflectivity (visible) | 1 | ✓ | ✓ | ✓ |
| pstb | brightness_temperature | Pseudo satellite image: water vapour Tb | K | ✓ | ✓ | ✓ |
| pstbc | brightness_temperature | Pseudo satellite image: water vapour Tb + correction for clouds | K | ✓ | ✓ | ✓ |
| pwat_column | atmosphere_mass_content_of_water_vapor | Precipitable water | kg m<sup>-2</sup> | ✓ | ✓ | ✓ |
| q2m | specific_humidity | Specific humidity | kg kg<sup>-1</sup> | ✓ | ✓ | ✓ |
| r2m | relative_humidity | Relative humidity | 1 | ✓ | ✓ | ✓ |
| rain_accum_past_hr | rainfall_amount | Rain, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| roughness_length | surface_roughness_length | Surface roughness length | m | ✓ | ✓ |  |
| snow_accum_past_hr | snowfall_amount | Snow, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| snow_water_equivalent | surface_snow_amount | Water equivalent of accumulated snow depth | kg m<sup>-2</sup> | ✓ | ✓ | ✓ |
| snsub_accum_past_hr |  | Snow Sublimation, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| soil_ice | volume_fraction_of_frozen_water_in_soil | Soil ice, root zone | m<sup>3</sup> m<sup>-3</sup> | ✓ | ✓ |  |
| soil_moisture | volume_fraction_of_condensed_water_in_soil | Soil moisture, root zone | m<sup>3</sup> m<sup>-3</sup> | ✓ | ✓ |  |
| soil_temperature | soil_temperature | Soil temperature, root zone | K | ✓ | ✓ |  |
| sshf_accum_past_hr |  | Sensible heat flux, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| surface_geopotential | surface_geopotential | Geopotential | m<sup>2</sup> s<sup>-2</sup> | ✓ |  |  |
| surface_soil_moisture | volume_fraction_of_condensed_water_in_soil | Surface soil moisture | m<sup>3</sup> m<sup>-3</sup> | ✓ | ✓ |  |
| swavr | surface_net_downward_shortwave_flux | Short-wave radiation flux | W m<sup>-2</sup> | ✓ | ✓ | ✓ |
| swavr_accum_past_hr |  | Short-wave radiation flux, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| swavr_toa_accum_past_hr |  | Short-wave radiation flux (atmosph.top), accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| t0m | surface_temperature | Surface (skin) temperature | K | ✓ | ✓ | ✓ |
| t2m | air_temperature | Temperature | K | ✓ | ✓ | ✓ |
| t_surface_isba | surface_temperature | ISBA surface temperature | K | ✓ | ✓ |  |
| tcc | cloud_area_fraction | Total cloud cover | 1 | ✓ | ✓ | ✓ |
| thermal_roughness_length | surface_roughness_length_for_heat_in_air | Surface roughness length for heat | m | ✓ | ✓ |  |
| tmax2m_since_analysis | air_temperature | Maximum temperature | K |  | ✓ | ✓ |
| tmin2m_since_analysis | air_temperature | Minimum temperature | K |  | ✓ | ✓ |
| tp_accum_past_hr | precipitation_amount | Total precipitation, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| u10m | eastward_wind | u-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| uflx_accum_past_hr |  | Momentum flux, u-component, accumulated over the past hour | Pa s |  | ✓ | ✓ |
| ugst10m_past_hr |  | Gust, u-component | m s<sup>-1</sup> |  | ✓ | ✓ |
| v10m | northward_wind | v-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| vflx_accum_past_hr |  | Momentum flux, v-component, accumulated over the past hour | Pa s |  | ✓ | ✓ |
| vgst10m_past_hr |  | Gust, v-component | m s<sup>-1</sup> |  | ✓ | ✓ |
| vis0m | visibility_in_air | Visibility | m | ✓ | ✓ | ✓ |
| wdir10m | wind_from_direction | Wind direction | degree | ✓ | ✓ | ✓ |
| wevap_accum_past_hr |  | Water evaporation, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| ws10m | wind_speed | Wind speed | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| xhail |  | AROME hail diagnostic | kg m<sup>-2</sup> | ✓ | ✓ | ✓ |
</details>

<details>
<summary>Height Levels</summary>
<h3>Height level parameters</h3>
Height level refers to parameters that are defined at specific vertical levels in the atmosphere.

<h4>Available height levels (meters above ground)</h4>

30, 50, 75, 100, 150, 200, 250, 300, 500

<h4>Available parameters</h4>

| Variable Name | CF Standard Name | Description | Unit | Analysis | Forecast (3 h) | Forecast (18 h) |
|---------------|------------------|-------------|------|:---:|:---:|:---:|
| r | relative_humidity | Relative humidity | 1 | ✓ | ✓ | ✓ |
| t | air_temperature | Temperature | K | ✓ | ✓ | ✓ |
| u | eastward_wind | u-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| v | northward_wind | v-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
</details>

<details>
<summary>Pressure Levels</summary>

<h3>Pressure level parameters</h3>

Pressure level refers to parameters that are defined at specific pressure levels in the atmosphere.
<h4>Available pressure levels (hPa)</h4>

1000, 950, 925, 900, 850, 800, 700, 600, 500, 400, 300, 250, 200, 100

<h4>Available parameters</h4>

| Variable Name | CF Standard Name | Description | Unit | Analysis | Forecast (3 h) | Forecast (18 h) |
|---------------|------------------|-------------|------|:---:|:---:|:---:|
| ciwc | mass_fraction_of_cloud_ice_in_air | Cloud ice | kg kg<sup>-1</sup> | ✓ | ✓ | ✓ |
| cwat | mass_fraction_of_cloud_liquid_water_in_air | Cloud water | kg kg<sup>-1</sup> | ✓ | ✓ | ✓ |
| r | relative_humidity | Relative humidity | 1 | ✓ | ✓ | ✓ |
| t | air_temperature | Temperature | K | ✓ | ✓ | ✓ |
| tw | upward_air_velocity | Vertical velocity | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| u | eastward_wind | u-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| v | northward_wind | v-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| z | geopotential | Geopotential | m<sup>2</sup> s<sup>-2</sup> | ✓ | ✓ | ✓ |
</details>


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