# DANRA Parameters

DANRA output is ordered into three main categories based on the vertical levels of the data: surface or single level (SL), height levels (HL), and pressure levels (PL). Each category contains various meteorological parameters, which are described in detail below.

<details>
<summary>Single Levels</summary>

## Single level parameters

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

## Height level parameters

Height level refers to parameters that are defined at specific vertical levels in the atmosphere.
### Available height levels (m)

30, 50, 75, 100, 150, 200, 250, 300, 500

### Available parameters

| Variable Name | CF Standard Name | Description | Unit | Analysis | Forecast (3 h) | Forecast (18 h) |
|---------------|------------------|-------------|------|:---:|:---:|:---:|
| r | relative_humidity | Relative humidity | 1 | ✓ | ✓ | ✓ |
| t | air_temperature | Temperature | K | ✓ | ✓ | ✓ |
| u | eastward_wind | u-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
| v | northward_wind | v-component of wind | m s<sup>-1</sup> | ✓ | ✓ | ✓ |
</details>

<details>
<summary>Pressure Levels</summary>

## Pressure level parameters

Pressure level refers to parameters that are defined at specific pressure levels in the atmosphere.
### Available pressure levels (hPa)

1000, 950, 925, 900, 850, 800, 700, 600, 500, 400, 300, 250, 200, 100

### Available parameters

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
