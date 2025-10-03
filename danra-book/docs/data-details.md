# Details about parameters
This section describes special parameters in the DANRA dataset. 

## DANRA Parameters

DANRA output is ordered into three main categories based on the vertical levels of the data: surface or single level (SL), height levels (HL), and pressure levels (PL). Each category contains various meteorological parameters, which are described in detail below.

<details>
<summary>Single Levels</summary>

### Single level parameters

Single level refers to parameters that are defined at a single vertical level in the atmosphere or at the surface.
| Variable Name | CF Standard Name | Description | Unit |
|---------------|------------------|-------------|------|
| cape_column | atmosphere_convective_available_potential_energy_wrt_surface | CAPE out of the model | J kg-1 |
| cb_column | cloud_base_altitude | Cloud base | m |
| ct_column | cloud_top_altitude | Cloud top | m |
| danra_projection |  |  |  |
| grpl_column | atmosphere_mass_content_of_graupel | Graupel | kg m<sup>-2</sup> |
| hcc0m | high_type_cloud_area_fraction | High cloud cover | 1 |
| icei0m |  | Icing index | - |
| lcc0m | low_type_cloud_area_fraction | Low cloud cover | 1 |
| lsm | land_binary_mask | Land cover (1=land, 0=sea) | 1 |
| lwavr0m |  | Long-wave radiation flux | W m<sup>-2</sup> |
| mcc0m | medium_type_cloud_area_fraction | Medium cloud cover | 1 |
| mld0m | atmosphere_boundary_layer_thickness | Mixed layer depth | m |
| orography |  | Geopotential | m<sup>2</sup> s<sup>-2</sup> |
| pres0m | air_pressure | Pressure | Pa |
| pres_seasurface | air_pressure_at_mean_sea_level | Pressure | Pa |
| prtp0m |  | Precipitation Type | - |
| psct0m | brightness_temperature_at_cloud_top | Pseudo satellite image: cloud top temperature (infrared) | K |
| pscw0m |  | Pseudo satellite image: cloud water reflectivity (visible) | - |
| pstb0m |  | Pseudo satellite image: water vapour Tb | - |
| pstbc0m |  | Pseudo satellite image: water vapour Tb + correction for clouds | - |
| pwat_column | atmosphere_mass_content_of_water_vapor | Precipitable water | kg m<sup>-2</sup> |
| r2m | relative_humidity | Relative humidity | % |
| sf0m | snowfall_amount | Water equivalent of accumulated snow depth | kg m<sup>-2</sup> |
| swavr0m |  | Short-wave radiation flux | W m<sup>-2</sup> |
| t0m | air_temperature | Temperature | K |
| t2m | air_temperature | Temperature | K |
| tcc0m | cloud_area_fraction | Total cloud cover | 1 |
| u10m | x_wind | u-component of wind | m s<sup>-1</sup> |
| v10m | y_wind | v-component of wind | m s<sup>-1</sup> |
| vis0m | visibility_in_air | Visibility | m |
| xhail0m |  | AROME hail diagnostic | kg m<sup>-2</sup> |
</details>

<details>
<summary>Height Levels</summary>
<h3>Height level parameters</h3>

<h>Available height levels (m):**</h4>

30, 50, 75, 100, 150, 200, 250, 300, 500

<h4>Available parameters</h4>

Height level refers to parameters that are defined at specific vertical levels in the atmosphere.
| Variable Name | CF Standard Name | Description | Unit |
|---------------|------------------|-------------|------|
| danra_projection |  |  |  |
| r | relative_humidity | Relative humidity | % |
| t | air_temperature | Temperature | K |
| u | x_wind | u-component of wind | m s<sup>-1</sup> |
| v | y_wind | v-component of wind | m s<sup>-1</sup> |
</details>

<details>
<summary>Pressure Levels</summary>

### Pressure level parameters

Pressure level refers to parameters that are defined at specific pressure levels in the atmosphere.
**Available pressure levels (hPa)**

1000, 950, 925, 900, 850, 800, 700, 600, 500, 400, 300, 250, 200, 100

**Available parameters**

| Variable Name | CF Standard Name | Description | Unit |
|---------------|------------------|-------------|------|
| ciwc | atmosphere_mass_content_of_cloud_ice | Cloud ice | kg m<sup>-2</sup> |
| cwat | atmosphere_mass_content_of_cloud_liquid_water | Cloud water | kg m<sup>-2</sup> |
| danra_projection |  |  |  |
| r | relative_humidity | Relative humidity | % |
| t | air_temperature | Temperature | K |
| tw | upward_air_velocity | Vertical velocity | m s<sup>-1</sup> |
| u | x_wind | u-component of wind | m s<sup>-1</sup> |
| v | y_wind | v-component of wind | m s<sup>-1</sup> |
| z | geopotential | Geopotential | m<sup>2</sup> s<sup>-2</sup> |
</details>


## Special parameters
The following parameters are encoded using a different schema than WMO standards. Thus, we provide a brief description of those below.

### Precipitation type
The precipitation type, `prtp0m,` describes the most prevalent type of precipitation in the given time frame. The following types are available:
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

### Icing index
The icing index, `icei0m` is a measure of the risk of icing in the atmosphere. The index is calculated as the maximum risk of icing somewhere in the atmosphere column. The index is an integer between 1 and 4, corresponding to the following risk levels:
| Code | Description |
|------|-------------|
| 1    | Trace |
| 2    | Light |
| 3    | Moderate |
| 4    | Severe | 

### AROME Hail diagnostic
The hail diagnostic, `xhail0m,` is a measure of the risk of hail. It is the maximum total column graupel in kg/m^2 since previous post-processing. Values above 16 kg/m^2 are considered to be a risk of hail.