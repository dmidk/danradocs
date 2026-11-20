<details>
<summary>Single Levels</summary>

<h3>Single level parameters</h3>

Single level refers to parameters that are defined at a single vertical level in the atmosphere or at the surface.

| Variable Name | CF Standard Name | Description | Unit | Analysis | Forecast (3 h) | Forecast (18 h) |
|---------------|------------------|-------------|------|:---:|:---:|:---:|
| albedo | surface_<wbr>albedo | ISBA total albedo | 1 | ✓ | ✓ |  |
| cape_column | atmosphere_<wbr>convective_<wbr>available_<wbr>potential_<wbr>energy_<wbr>wrt_<wbr>surface | CAPE out of the model | J kg<sup>-1</sup> | ✓ | ✓ | ✓ |
| cb_column | cloud_<wbr>base_<wbr>altitude | Cloud base | m | ✓ | ✓ | ✓ |
| ct_column | cloud_<wbr>top_<wbr>altitude | Cloud top | m | ✓ | ✓ | ✓ |
| dni_accum_past_hr |  | Direct normal irradiance, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| fog | fog_<wbr>area_<wbr>fraction | Fog area fraction | 1 | ✓ | ✓ | ✓ |
| freezing_height | freezing_<wbr>level_<wbr>altitude | Height of the 0 degC isotherm | m | ✓ | ✓ | ✓ |
| grad_accum_past_hr | integral_<wbr>wrt_<wbr>time_<wbr>of_<wbr>surface_<wbr>downwelling_<wbr>shortwave_<wbr>flux_<wbr>in_<wbr>air | Global radiation flux, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| grpl_accum_past_hr | graupel_<wbr>fall_<wbr>amount | Graupel, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| grpl_column | atmosphere_<wbr>mass_<wbr>content_<wbr>of_<wbr>graupel | Graupel | kg m<sup>-2</sup> | ✓ | ✓ | ✓ |
| hcc | high_<wbr>type_<wbr>cloud_<wbr>area_<wbr>fraction | High cloud cover | 1 | ✓ | ✓ | ✓ |
| icei |  | Icing index | 1 | ✓ | ✓ | ✓ |
| lcc | low_<wbr>type_<wbr>cloud_<wbr>area_<wbr>fraction | Low cloud cover | 1 | ✓ | ✓ | ✓ |
| lhe_accum_past_hr |  | Latent heat flux through evaporation, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| lhsub_accum_past_hr |  | Latent Heat Sublimation, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| lsm | land_<wbr>binary_<wbr>mask | Land cover (1=land, 0=sea) | 1 | ✓ |  |  |
| lwavr | surface_<wbr>net_<wbr>downward_<wbr>longwave_<wbr>flux | Long-wave radiation flux | W m<sup>-2</sup> | ✓ | ✓ | ✓ |
| lwavr_accum_past_hr | integral_<wbr>wrt_<wbr>time_<wbr>of_<wbr>surface_<wbr>downwelling_<wbr>longwave_<wbr>flux_<wbr>in_<wbr>air | Long-wave radiation flux, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| mcc | medium_<wbr>type_<wbr>cloud_<wbr>area_<wbr>fraction | Medium cloud cover | 1 | ✓ | ✓ | ✓ |
| mld | atmosphere_<wbr>boundary_<wbr>layer_<wbr>thickness | Height of the planetary boundary layer | m | ✓ | ✓ | ✓ |
| nlwrs_accum_past_hr | integral_<wbr>wrt_<wbr>time_<wbr>of_<wbr>surface_<wbr>net_<wbr>downward_<wbr>longwave_<wbr>flux | Net long-wave radiation flux (surface), accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| nlwrt_toa | toa_<wbr>net_<wbr>downward_<wbr>longwave_<wbr>flux | Net long-wave radiation flux (atmosph.top) | W m<sup>-2</sup> | ✓ | ✓ | ✓ |
| nlwrt_toa_accum_past_hr |  | Net long-wave radiation flux (atmosph.top), accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| nswrs_accum_past_hr | integral_<wbr>wrt_<wbr>time_<wbr>of_<wbr>surface_<wbr>net_<wbr>downward_<wbr>shortwave_<wbr>flux | Net short-wave radiation flux (surface), accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| nswrt_toa | toa_<wbr>net_<wbr>downward_<wbr>shortwave_<wbr>flux | Net short-wave radiation flux (atmosph.top) | W m<sup>-2</sup> | ✓ | ✓ | ✓ |
| nswrt_toa_accum_past_hr | integral_<wbr>wrt_<wbr>time_<wbr>of_<wbr>toa_<wbr>net_<wbr>downward_<wbr>shortwave_<wbr>flux | Net short-wave radiation flux (atmosph.top), accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| pres0m | surface_<wbr>air_<wbr>pressure | Pressure | Pa | ✓ | ✓ | ✓ |
| pres_seasurface | air_<wbr>pressure_<wbr>at_<wbr>mean_<wbr>sea_<wbr>level | Mean sea level pressure | Pa | ✓ | ✓ | ✓ |
| prtp | predominant_<wbr>precipitation_<wbr>type_<wbr>at_<wbr>surface | Precipitation Type | 1 | ✓ | ✓ | ✓ |
| psct | brightness_<wbr>temperature | Pseudo satellite image: infrared brightness temperature (cloud top where cloudy, ground where clear) | K | ✓ | ✓ | ✓ |
| pscw |  | Pseudo satellite image: cloud water reflectivity (visible) | 1 | ✓ | ✓ | ✓ |
| pstb | brightness_<wbr>temperature | Pseudo satellite image: water vapour Tb | K | ✓ | ✓ | ✓ |
| pstbc | brightness_<wbr>temperature | Pseudo satellite image: water vapour Tb + correction for clouds | K | ✓ | ✓ | ✓ |
| pwat_column | atmosphere_<wbr>mass_<wbr>content_<wbr>of_<wbr>water_<wbr>vapor | Precipitable water | kg m<sup>-2</sup> | ✓ | ✓ | ✓ |
| q2m | specific_<wbr>humidity | Specific humidity | kg kg<sup>-1</sup> | ✓ | ✓ | ✓ |
| r2m | relative_<wbr>humidity | Relative humidity | 1 | ✓ | ✓ | ✓ |
| rain_accum_past_hr | rainfall_<wbr>amount | Rain, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| roughness_length | surface_<wbr>roughness_<wbr>length | Surface roughness length | m | ✓ | ✓ |  |
| snow_accum_past_hr | snowfall_<wbr>amount | Snow, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| snow_water_equivalent | surface_<wbr>snow_<wbr>amount | Water equivalent of accumulated snow depth | kg m<sup>-2</sup> | ✓ | ✓ | ✓ |
| snsub_accum_past_hr |  | Snow Sublimation, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| soil_ice | volume_<wbr>fraction_<wbr>of_<wbr>frozen_<wbr>water_<wbr>in_<wbr>soil | Soil ice, root zone | m<sup>3</sup> m<sup>-3</sup> | ✓ | ✓ |  |
| soil_moisture |  | Soil moisture, root zone | m<sup>3</sup> m<sup>-3</sup> | ✓ | ✓ |  |
| soil_temperature | soil_<wbr>temperature | Soil temperature, root zone | K | ✓ | ✓ |  |
| sshf_accum_past_hr |  | Sensible heat flux, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| surface_geopotential | surface_<wbr>geopotential | Geopotential | m<sup>2</sup> s<sup>-2</sup> | ✓ |  |  |
| surface_soil_moisture |  | Surface soil moisture | m<sup>3</sup> m<sup>-3</sup> | ✓ | ✓ |  |
| swavr | surface_<wbr>net_<wbr>downward_<wbr>shortwave_<wbr>flux | Short-wave radiation flux | W m<sup>-2</sup> | ✓ | ✓ | ✓ |
| swavr_accum_past_hr |  | Short-wave radiation flux, accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| swavr_toa_accum_past_hr |  | Short-wave radiation flux (atmosph.top), accumulated over the past hour | W s m<sup>-2</sup> |  | ✓ | ✓ |
| t0m | surface_<wbr>temperature | Surface (skin) temperature | K | ✓ | ✓ | ✓ |
| t2m | air_<wbr>temperature | Temperature | K | ✓ | ✓ | ✓ |
| t_surface_isba | surface_<wbr>temperature | ISBA surface temperature | K | ✓ | ✓ |  |
| tcc | cloud_<wbr>area_<wbr>fraction | Total cloud cover | 1 | ✓ | ✓ | ✓ |
| thermal_roughness_length | surface_<wbr>roughness_<wbr>length_<wbr>for_<wbr>heat_<wbr>in_<wbr>air | Surface roughness length for heat | m | ✓ | ✓ |  |
| tmax2m_since_analysis | air_<wbr>temperature | Maximum temperature | K |  | ✓ | ✓ |
| tmin2m_since_analysis | air_<wbr>temperature | Minimum temperature | K |  | ✓ | ✓ |
| tp_accum_past_hr | precipitation_<wbr>amount | Total precipitation, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| u10m | eastward_<wbr>wind | u-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| uflx_accum_past_hr |  | Momentum flux, u-component, accumulated over the past hour | Pa s |  | ✓ | ✓ |
| ugst10m_past_hr |  | Gust, u-component | m s<sup>-1</sup> |  | ✓ | ✓ |
| v10m | northward_<wbr>wind | v-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| vflx_accum_past_hr |  | Momentum flux, v-component, accumulated over the past hour | Pa s |  | ✓ | ✓ |
| vgst10m_past_hr |  | Gust, v-component | m s<sup>-1</sup> |  | ✓ | ✓ |
| vis0m | visibility_<wbr>in_<wbr>air | Visibility | m | ✓ | ✓ | ✓ |
| wdir10m | wind_<wbr>from_<wbr>direction | Wind direction | degree | ✓ | ✓ | ✓ |
| wevap_accum_past_hr |  | Water evaporation, accumulated over the past hour | kg m<sup>-2</sup> |  | ✓ | ✓ |
| ws10m | wind_<wbr>speed | Wind speed | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
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
| r | relative_<wbr>humidity | Relative humidity | 1 | ✓ | ✓ | ✓ |
| t | air_<wbr>temperature | Temperature | K | ✓ | ✓ | ✓ |
| u | eastward_<wbr>wind | u-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| v | northward_<wbr>wind | v-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |

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
| ciwc | mass_<wbr>fraction_<wbr>of_<wbr>cloud_<wbr>ice_<wbr>in_<wbr>air | Cloud ice | kg kg<sup>-1</sup> | ✓ | ✓ | ✓ |
| cwat | mass_<wbr>fraction_<wbr>of_<wbr>cloud_<wbr>liquid_<wbr>water_<wbr>in_<wbr>air | Cloud water | kg kg<sup>-1</sup> | ✓ | ✓ | ✓ |
| r | relative_<wbr>humidity | Relative humidity | 1 | ✓ | ✓ | ✓ |
| t | air_<wbr>temperature | Temperature | K | ✓ | ✓ | ✓ |
| tw | upward_<wbr>air_<wbr>velocity | Vertical velocity | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| u | eastward_<wbr>wind | u-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| v | northward_<wbr>wind | v-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| z | geopotential | Geopotential | m<sup>2</sup> s<sup>-2</sup> | ✓ | ✓ | ✓ |

</details>
