# AquaViva
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://franfurey.github.io/aquaViva/">
    <img src="visualization/public/visual.png"/>
  </a>
</div>

<p align="center">
  <br/>
  <a href="https://github.com/franfurey/aquaViva" target="_blank"><img src="https://img.shields.io/badge/-View%20Website-29bbff?style=for-the-badge"/></a>
  <a href="https://github.com/franfurey/aquaViva/issues"><img src="https://img.shields.io/badge/-Report%20Bug-black?style=for-the-badge"/></a>
  <a href="https://github.com/franfurey/aquaViva/issues"><img src="https://img.shields.io/badge/-Request%20Feature-black?style=for-the-badge"/></a>
  <br />
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#data">Data</a></li>
        <li><a href="#machine-learning">Machine Learning</a></li>
        <li><a href="#visualization">Visualization</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>



<!-- ABOUT-->
# About
AquaViva is an innovative project aimed at addressing one of the most important sustainable development goals and overall global humanitarian challenges of our time - the lack of access to clean water (SDG 6). To accomplish this, we are using cutting-edge machine learning models, trained on various datasets including satellite imagery, climatic variables, and geological features, to produce near real-time, high resolution maps of groundwater level.

We believe that this tool has great potential to help communities mitigate water scarcity, monitor groundwater, and efficiently identify suitable sources of clean water. As such, we are committed to keeping our project open-source and free-to-use, and we welcome any contributors to build off of what we have done. This project is part of [NASA's Pale Blue Dot Visualization Challenge](https://www.drivendata.org/competitions/256/pale-blue-dot/), which shares our deep commitment to using technology for environmental and social good.

**Created by Team Viva Aqua** | **Francisco Furey, Adam Zheng, Malena Vildoza, Malick Dieye (AKA Jay) 😊**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Data
The AquaViva project relies on a diverse array of datasets to train our machine learning models for predicting groundwater levels in Gambia. These datasets include measurements from wells, satellite imagery, climatic variables, and geological features, providing a comprehensive understanding of the factors influencing groundwater levels.

### Main Data Sources

1. **[Global Groundwater Information System](https://ggis.un-igrac.org/) (GGIS)**: An interactive portal offering data on global groundwater resources. We use it to access piezometric data on 36 wells across Gambia, spanning 2015 to 2022, as well as data on hydrogeological regions.

2. **[British Geological Survey](https://www2.bgs.ac.uk/groundwater/international/africanGroundwater/maps.html) (BGS)**: This research project by BGS focused on the resilience of African groundwater to climate change. We incorporate their depth to groundwater data, which classifies data into 6 categories (0-7, 7-25, 25-50, 50-100, 100-250, >250 meters) - significantly lower resolution & precision than our targets, but still potentially useful.

3. **[Application for Extracting and Exploring Analysis Ready Samples](https://appeears.earthdatacloud.nasa.gov/api/?python#introduction) (AρρEEARS)**: We used this tool to extract various parameters such as NDVI, MIR, EVI, Elevation, Curvature, Drainage Density, and Slope.

4. **[ClimateSERV](https://climateserv.servirglobal.net/help)**: A tool by SERVIR, NASA, & USAID that provides climatic and vegetation data. We used the ClimateSERV API and wrote a Python library ([climateservAccess](https://pypi.org/project/climateservaccess/)) to gather soil moisture, evapotranspiration, streamflow, and precipitation data. 

### Features
| Datatype                                      | Description                                      | Data Source                                 | Resolution       |
|-----------------------------------------------|--------------------------------------------------|---------------------------------------------|------------------|
| LIS_Soil_Moisture_Combined                     | Soil Moisture                                   | ClimateSERV/LIS                              | 3 km            |
| LIS_Streamflow                                 | Streamflow                                      | ClimateSERV/LIS                              | 3 km            |
| LIS_ET                                         | Evapotranspiration                              | ClimateSERV/LIS                              | 3 km            |
| MOD13Q1_061__250m_16_days_EVI                  | Enhanced Vegetation Index (EVI)                 | AρρEEARS/MODIS                               | 250 m           |
| MOD13Q1_061__250m_16_days_MIR_reflectance      | Mid-Infrared Reflectance                        | AρρEEARS/MODIS                               | 250 m           |
| MOD13Q1_061__250m_16_days_NDVI                 | Normalized Difference Vegetation Index (NDVI)   | AρρEEARS/MODIS                               | 250 m           |
| NASA_IMERG_Late                                | Precipitation                                   | ClimateSERV/IMERG                            | 10 km           |
| DepthToGroundwater                             | Estimated Groundwater Level Range               | BGS                                          | 5 km            |
| Curvatu_tif2                                   | Curvature                                       | AρρEEARS/NASADEM                             | 30 m            |
| Drainage_density                               | Drainage Density                                | AρρEEARS/NASADEM                             | 30 m            |
| Slope_tif2                                     | Slope                                           | AρρEEARS/NASADEM                             | 30 m            |
| Hydrogeo                                       | Hydrogeological Region                          | IGRAC/GGIS                                   | N/A             |
| NASADEM_HGT                                    | Elevation                                       | AρρEEARS/NASADEM                             | 30 m            |

### Output
| Datatype                                      | Description                                      | Data Source                                 |
|-----------------------------------------------|--------------------------------------------------|---------------------------------------------|
| GROUNDWATER_LEVEL                             | Groundwater Level                                | IGRAC/GGIS                                  |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Machine Learning

 Our preprocessing steps involved handling diverse data formats and large file sizes (.nc4, .nc, .csv), necessitating careful data cleaning, including addressing missing data with techniques like nearest neighbors. Our final dataset comprised approximately 6300 rows and 22 columns (36 wells information above all Gambia). We use libraries like geopandas to merge the different dataset based on Latitude and Longitude.

Machine Learning Models and Training
 For the machine learning component, we divided our dataset based on well IDs to avoid overfitting, allocating 83% for training and 17% for testing (we didnt have to much data so we need to carefully give more data to the train side). We employed various regression models, including [SVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html), [AdaBoostRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html), [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html), [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html), [SGDRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html), and [LinearSVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html). Our evaluation focused on metrics like Mean Squared Error (MSE), Mean Absolute Error (MAE) and the Coefficient of Determination (R²).

After rigorous testing, [LinearSVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html) emerged as the most effective model, delivering an MAE of 2.6 meters and an R² of 0.42. We also applied [Cross-Validation](https://scikit-learn.org/stable/modules/cross_validation.html) and [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) for hyperparameter tuning to optimize the model's performance, and combined [LinearSVR](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html) with [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html) for kernel optimization.

Challenges and Future Directions
Our computational resources limited our ability to test more computationally intensive models like neural networks. However, with access to more powerful machines, exploring these models could yield even more promising results.

Technical Implementation
Our implementation involved several Python libraries for data processing and machine learning. Key libraries included [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), [Geopandas](https://geopandas.org/en/stable/), [Sickit-Learn](https://scikit-learn.org/stable/), [netCDF4](https://github.com/Unidata/netcdf4-python) and [xarray](https://docs.xarray.dev/en/stable/). We used a Jupyter Notebook environment for development and testing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Visualization

This section will cover the creation of visualizations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With
![Python][Python]
![scikit-learn][scikit-learn]
![TensorFlow][TensorFlow]
![Jupyter][Jupyter]
![HTML][HTML]
![CSS][CSS]
![JavaScript][JavaScript]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

This section will contain a guide for contributing to our project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[![GMAIL](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:adzheng@tamu.edu)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## References
* [A Machine Learning Approach to Predict Groundwater Levels in California Reveals Ecosystems at Risk](https://www.frontiersin.org/articles/10.3389/feart.2021.784499/full#h3)
* [Groundwater Prediction Using Machine-Learning Tools](https://www.mdpi.com/1999-4893/13/11/300)
* [Prediction of groundwater level fluctuations under climate change based on machine learning algorithms in the Mashhad aquifer, Iran](https://iwaponline.com/jwcc/article/14/3/1039/93926/Prediction-of-groundwater-level-fluctuations-under)
* [CodePen Back Button](https://codepen.io/ender2821/pen/LpgYOB)
* [CodePen Info on Hover](https://codepen.io/ruppysuppy/pen/rNWdWNp)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/franfurey/aquaViva.svg?style=for-the-badge
[contributors-url]: https://github.com/franfurey/aquaViva/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/franfurey/aquaViva.svg?style=for-the-badge
[forks-url]: https://github.com/franfurey/aquaViva/network/members
[stars-shield]: https://img.shields.io/github/stars/franfurey/aquaViva.svg?style=for-the-badge
[stars-url]: https://github.com/franfurey/aquaViva/stargazers
[issues-shield]: https://img.shields.io/github/issues/franfurey/aquaViva.svg?style=for-the-badge
[issues-url]: https://github.com/franfurey/aquaViva/issues
[license-shield]: https://img.shields.io/github/license/franfurey/aquaViva.svg?style=for-the-badge
[license-url]: https://github.com/franfurey/aquaViva/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[Python]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Jupyter]: https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white
[TensorFlow]: https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white
[JavaScript]: https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E
[HTML]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[CSS]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[scikit-learn]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
