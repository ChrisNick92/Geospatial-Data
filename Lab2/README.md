# Lab 2 - *Geospatial Services and Web Applications*


In this second lab exercise we shift from the online Platforms for big Earth Observation (EO) Data Management and Analysis (like GEE) that we made extensive use in the previous lab and we move onto the analysis of EO data at a local level. The biggest advantage of working in an online Platform is that we do not have to worry about finding the data. Usually, everything is on the Platform in use. The greatest challenges one has to face when leaving from the safety zone of a well organized platform is 1) where to look for the proper data, 2) how to download them and 3) how to combine them efficiently in order to extract valuable information about the areas of interest. In this lab we make an extensive use of the WFS/WMS services in order to obtain vector/raster data. We combine the raster and vector data to make visualizations, cropp images and focus in the areas of interest. With the use of GeoPandas library we perform geospatial queries and extract valuable information with respect to the locations of airports, coastlines, railroads, administratives areas etc of Greece and Europe. Below we give a short presentation of the contents of this second lab.

- At first, we focus our attention in the area of Kastoria. From <a href="https://pithos.okeanos.grnet.gr/public/fBSNLJeNxerluMj2MVDqF">https://pithos.okeanos.grnet.gr/public/fBSNLJeNxerluMj2MVDqF</a> we download a tif file containing raster data for the area of Kastoria. The data consists of 24 Landsat satellite images with the following 10 bands: 1) Blue, 2) Green, 3) Red, 4) NIR, 5) SWIR1, 6) SWIR2, 7) NDVI, 8) MSAVI, 9) NDWI, 10) NDBI.  Using rasterio to read the data and matplotlib we can create an RGB visualization of the area. 

<h2>Kastoria in RGB</h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab2/Images/RGBkastoria.png?raw=true" width="700" height="550">

By choosing a certain polygon we can focus our attention into a sub-area of Kastoria.

<h2>The transformed image - Cropping the image with respect to a predefined polygon</h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab2/Images/ClippedImage.png?raw=true" width="500" height="350">

By taking advantage the information for the NDVI, NDWI and NDBI we can find the pixels with the highest mean values for these three spectral indices in the area of interest.

<h2>The pixels with maximal mean values for each index. </h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab2/Images/PointMaximalKastoria.png?raw=true" width="500" height="400">
  
  
- Using the WMS/WFS services and GeoPandas library we can perform interesting geospatial queries. For example, we can determine the settlements of Greece within 1km near some airport. In the following table you can see the results of this query.
  
  <table>
  <caption>Settlements within 1km distance near some Airport (only 5 rows)</caption>
  <tr>
    <th>Settlement</th>
    <th>Municipality</th>
    <th>Airport</th>
  </tr>
  <tr>
    <td>Παραδείσιον</td>
    <td>ΔΗΜΟΣ ΠΕΤΑΛΟΥΔΩΝ</td>
    <td>Διαγόρας LGRP RHO Παραδείσι, Ρόδου</td>
  </tr>
  <tr>
    <td>Βαγιές</td>
    <td>ΔΗΜΟΣ ΠΕΤΑΛΟΥΔΩΝ</td>
    <td>Διαγόρας LGRP RHO Παραδείσι, Ρόδου</td>
  </tr>
    <tr>
    <td>Μάννα</td>
    <td>ΔΗΜΟΣ ΕΡΜΟΥΠΟΛΕΩΣ</td>
    <td>Σύρου LGSO JSY</td>
  </tr>
  </tr>
    <tr>
    <td>Παρθένιον</td>
    <td>ΔΗΜΟΣ ΛΕΡΟΥ</td>
    <td>Λέρου LGLE LRS</td>
  </tr>
   </tr>
    <tr>
    <td>Άργος</td>
    <td>ΔΗΜΟΣ ΚΑΛΥΜΝΙΩΝ</td>
    <td>Κάλυμνος LGKY JKL</td>
  </tr>
  
</table>

Futhermore, we can find the number of transportation stations contained in the balls of radius 1.5km having as centers the settlements located in Attica.

 <table>
  <caption>Settlements with the most Transportation stations within 1.5 km radius (only 5 rows)</caption>
  <tr>
    <th>No.</th>
    <th>Settlement</th>
    <th>Number of Stations</th>
  </tr>
  <tr>
    <td>1.</td>
    <td>Αθήνα</td>
    <td>274</td>
  </tr>
  <tr>
    <td>2.</td>
    <td>Πειραιάς</td>
    <td>227</td>
  </tr>
    <tr>
    <td>3,</td>
    <td>Κορυδαλλός</td>
    <td>217</td>
  </tr>
  </tr>
    <tr>
    <td>4.</td>
    <td>Νίκαια</td>
    <td>195</td>
  </tr>
   </tr>
    <tr>
    <td>5.</td>
    <td>Δάφνη</td>
    <td>195</td>
  </tr>
  
</table>

Combining the vector data of the settlements and transportation stations we can create a static map.

<h2>Transportation stations and settlements in Attica. </h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab2/Images/TransportationOASA.png?raw=true" width="800" height="700">

In another visualization, we combine an RGB Image of Europe provided in the form of raster data to add it as a background to visualize the locations of the airports and administrative regions of Greece.

<h2>Airport and Administrative regions of Greece. </h2>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab2/Images/AirportsAdminRegGreece.png?raw=true" width="800" height="700">

More geospatial queries and visualizations are produced for the purposes of this Lab. This is only a little taste!
