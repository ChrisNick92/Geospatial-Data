# Lab 1 - *Data retrieval, analysis and timeseries of geospatial products using online platforms*

The first lab serves as an introduction to the world of geospatial big data analytics. We work solely in <a href="https://earthengine.google.com">*Google Earth Engine (GEE)*</a>. An online computing platform that allows users to run geospatial analysis on Google's infrastracture. GEE provides an online code editor for writing and running scripts. In this directory you can find the code that was produced for the purposes of this Lab in JavaScript programming language. The goal of this lab is to gain familiary with the different types of data used for geospatial analysis, study certain areas of interest and extract timeseries for various spectral indices for these areas for certain periods of time and make comparisons. For our analysis we use the hyperspectral images provided by <a href="https://en.wikipedia.org/wiki/Landsat_8">*Landsat 8*</a> satellite. A brief summary of the tasks in this lab are given below. 

- We focus on a specific polygon near the city of Larisa.

<h2>The area of interest near the city of Larisa</h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab1/images/ruralpoly.png?raw=true" alt="The area of interest near the city of Larisa" width="900" height="500">


- Using custom palettes we provide different spectral visualizations for the area of interest.

<h2>The area of interest in RGB</h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab1/images/clearestRGB.png?raw=true" alt="The area of interest near the city of Larisa" width="450" height="200">

<h2>The area of interest in Pseudocolor</h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab1/images/clearestFalse.png?raw=true" alt="The area of interest near the city of Larisa" width="450" height="200">

<h2>NDVI visualization</h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab1/images/clearestNDVI.png?raw=true" alt="The area of interest near the city of Larisa" width="450" height="200">

Futhermore, we perform a classification task in an area of interest. We choose the following five categories: 1) urban fabric (red), 2) rural areas (light green), 3) woodland (green), 4) lakes (light blue), 5) sea areas (blue).

<h2>The training set for the classification task</h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab1/images/TrainingSet.png?raw=true" alt="The area of interest near the city of Larisa" width="450" height="200">

Using the GEE API we develop a CART and a SVM classifier to learn the five aforementioned categories. In the image below you can see the results obtained from the CART classifier.

<h2>The classification of CART</h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab1/images/CART-RGB.png" alt="The area of interest near the city of Larisa" width="700" height="200">
