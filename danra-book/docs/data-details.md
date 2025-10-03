# Details about parameters
This section describes special parameters in the DANRA dataset. 

!include "../docs/parameters.md"

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