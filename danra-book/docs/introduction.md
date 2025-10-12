# Introduction to the Danish Reanalysis
The DANRA dataset covers the period from Sept 1990 to Dec 2023. \
DANRA is produced using 3D-Var data assimilation and model forecasts with the reanalysis system based on the adapted Harmonie-arome CY40h1.1 forecast system ([Bengtsson et al., 2017](https://journals.ametsoc.org/view/journals/mwre/145/5/mwr-d-16-0417.1.xml)). DANRA runs on a horizontal grid-mesh of 800 x 600 at 2.5 km grid size,  with 65 hybrid sigma/pressure (model) levels in the vertical and the bottom level at around 12 meter and top level at 10 hPa. For data assimilation, quality controlled local observation data from synoptic stations in Denmark and nearby countries have been added, along with conventional weather observations collected from the Global Telecommunication System (GTS) for synoptic, ship, drift buoy, radiosonde, aircraft observations,  as well as satellite remote sensing data on radiance, atmospheric motion vector (AMV), scatterometer, radio occultation, has been assimilated. Selected atmospheric data are available on model levels and they are also interpolated to 14 pressure levels. "Surface or single level" data are also available, containing 2D parameters such as screen level properties, accumulated precipitation, top of atmosphere radiation and vertical integrals over the entire depth of the atmosphere. \
The DANRA dataset contains high resolution reanalysis for key meteorological parameters. The data are available at a 1h and 3h frequency and consist of analyses and short (18 hour) forecasts, initialised 8 times daily every three hours. Many analysed parameters are also available from the forecasts. However, there are a number of forecast parameters, e.g. fluxes, minima and maxima, and accumulations,  that are not available from the analyses.\
The data are archived in the internal DMI data archive and a pertinent sub-set of the data has been copied to the European Weather Cloud. Where single level and pressure level data are available, analyses are provided rather than forecasts, unless the parameter is only available from the forecasts.

## Technical details
For a full technical description of the dataset, please refer to the @danratech.\

### Domain
![DANRA Domain](https://raw.githubusercontent.com/dmidk/danradocs/refs/heads/main/danra-book/docs/figures/domain.png)\
The DANRA domain covers the area bounded in a box spanning from roughly 47.5°N, 3.0°W to 65.5°N, 25.0°E (as seen in the figure above) on a Lambert Conformal grid centered around 56.7°N, 8.2°E.\
The horizontal resolution is 2.5 km and the vertical resolution is 65 hybrid sigma/pressure levels. The complete domain spans 800x600 horizontal grid points, including an extension zone covering 11 grid points. Thus, output is available in 789x589 horizontal grid points.

### Reanalysis system
DANRA uses hourly global ERA5 reanalysis as lateral boundary conditions. In contrast to time-critical operational systems that use forecast lateral boundaries, DANRA uses analysis boundary conditions, providing optimal boundary conditions of the regional reanalysis. \
The operational production has been carried out over 9 streams of each 4 years except for the final, near-real time, each consisting of a full year spin-up.
| Stream | Reanalysis period |
|-----------|-------------|
| 1989 | 1990.09.01 - 1994.08.30 |
| 1993 | 1994.09.01 - 1998.08.30 |
| 1997 | 1998.09.01 - 2002.08.30 |
| 2001 | 2002.09.01 - 2006.08.30 |
| 2005 | 2006.09.01 - 2010.08.30 |
| 2009 | 2010.09.01 - 2014.08.30 |
| 2013 | 2014.09.01 - 2017.08.30 |
| 2016 | 2017.09.01 - 2019.11.30 |
| 2018 | 2019.12.01 - 2023.12.31 |