# AquaViva
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Data
The AquaViva project relies on a diverse array of datasets to train our machine learning models for predicting groundwater levels in Gambia. These datasets include measurements from wells, satellite imagery, climatic variables, and geological features, providing a comprehensive understanding of the factors influencing groundwater levels.

### Main Data Sources

1. **Global Groundwater Information System (GGIS)**
   - Source: [GGIS](https://ggis.un-igrac.org/)
   - Description: GGIS is an interactive portal offering data on global groundwater resources. We use it to access data on 48 wells across Gambia, spanning 2015 to 2022, which forms our primary dataframe.

2. **British Geological Survey (BGS)**
   - Source: [BGS Africa Groundwater Maps](https://www2.bgs.ac.uk/groundwater/international/africanGroundwater/maps.html)
   - Description: This research project by BGS focused on the resilience of African groundwater to climate change. We incorporate their findings, including quantitative groundwater maps of Africa, to enrich our understanding of the groundwater landscape in Gambia.

3. **Application for Extracting and Exploring Analysis Ready Samples (AρρEEARS)**
   - Source: [AρρEEARS](https://appeears.earthdatacloud.nasa.gov/api/?python#introduction)
   - Data: We extract various parameters such as 1NDVI, MIR reflectance, EVI (250mts, 16 days), NASADEM HGT, Curvature, Drainage Density, Slope, and Hydrogeology from this platform.

4. **ClimateSERV**
   - Source: [ClimateSERV](https://climateserv.servirglobal.net/)
   - Description: ClimateSERV provides actionable data for decision-making on climate-related issues. We use it to gather LIS_Soil_Moisture_Combined, LIS_Streamflow, LIS_ET, and NASA_IMERG_Late data to enhance our model's predictive capabilities.

By integrating these diverse datasets, AquaViva aims to deliver robust and reliable predictions of groundwater levels, contributing to the sustainable management of water resources in Gambia.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Machine Learning

This section will document the process of training machine learning models.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Visualization

This section will cover the creation of visualizations.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With
![Python][Python]
![TensorFlow][TensorFlow]
![Jupyter][Jupyter]

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
