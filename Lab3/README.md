# Lab 3 - *Classification and segmentation of Hyperspectral Images*

- <b> Short Description: </b> In this third lab we begin our investigation into the Deep Learning framework. The problem at hand is the classification of hyperspectral images. Hyperspectral image classification has been a vibrant area of research in recent years. Given an image, usually obtained from a satellite, the goal is to assign each pixel of the image to a class from a predetermined set of classes. In the case of satellite images, one is usually interested in mapping each pixel to the corresponding land use; e.g. urban fabric, forest, water etc. In this lab our goal is to develop a model with the highest generalization capabilities in order to make pixel-wise predictions to three satellite images. 

- <b> The Dataset: </b> The dataset that we use in this lab is the <a href="https://www2.isprs.org/commissions/comm3/wg4/hyrank/">HyRANK</a> dataset which was developed by a scientific initiative of the ISPRS, WG III/4. It is composed of five hyperspectral images gathered with the Hyperion sensor Earth Observing-1. After a preprocessing step, these images were provided with 176 surface reflectance bands. The ground truths from two (Loukia and Dioni) out of five images were provided. 14 Land Use and Land Cover (LULC) were annotated in the ground truth following the CORINE Land Cover principles. In the following table we see the 14 categories and their corresponding labels and color codes.


<h2 id="The 14 LULC classes of the HyRANK dataset">The 14 LULC classes of the HyRANK dataset</h2>

<table>
  <thead>
    <tr>
      <th>Label</th>
      <th>Color Code</th>
      <th>Category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>#000000</td>
      <td>Non Defined</td>
    </tr>
    <tr>
      <td>1</td>
      <td>#ff0000</td>
      <td>Dense Urban Fabric</td>
    </tr>
    <tr>
      <td>2</td>
      <td>#a600cc</td>
      <td>Mineral Extraction Sites</td>
    </tr>
    <tr>
      <td>3</td>
      <td>#ffffa8/td>
      <td>Non Irrigated Arable Land</td>
    </tr>
    <tr>
      <td>4</td>
      <td>#f2a64d</td>
      <td>Fruit Trees/td>
    </tr>
    <tr>
      <td>5</td>
      <td>#e6a600</td>
      <td>Olive Groves/td>
    </tr>
    <tr>
      <td>6</td>
      <td>#80ff00</td>
      <td>Broad-leaved forest</td>
    </tr>
    <tr>
      <td>7</td>
      <td>#00a600</td>
      <td>Coniferous-Forest</td>
    </tr>
    <tr>
      <td>8</td>
      <td>#a600cc</td>
      <td>Mixed Forest</td>
    </tr>
    <tr>
      <td>9</td>
      <td>#819c25</td>
      <td>Dense Sclerophyllous Vegetation</td>
    </tr>
    <tr>
      <td>10</td>
      <td>#e6cc4d/td>
      <td>Sparse Sclerophyllous Vegetation</td>
    </tr>
    <tr>
      <td>11</td>
      <td>#e6e64d</td>
      <td>Sparcely Vegetated Areas</td>
    </tr>
    <tr>
      <td>12</td>
      <td>#cccccc</td>
      <td>Rocks and Sand</td>
    </tr>
    <tr>
      <td>13</td>
      <td>#4d4dff</td>
      <td>Water</td>
    </tr>
    <tr>
      <td>14</td>
      <td>#80f2e6</td>
      <td>Coastal Water</td>
    </tr>
  </tbody>
</table>

The images of Dioni and Loukia and their corresponding ground truth labels are depicted in the following figures.

<h4>The image of Dioni in RGB composite and the corresponding ground truth labels. The size of the image is 250x1376 with 176 spectral bands and the spatial resolution is 30m. Pixels shown in black color correspond to undefined land uses.</h4>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab3/results/DioniRGB.png?raw=true" width="1376" height="500">


<h4>The image of Loukia in RGB composite and the corresponding ground truth labels. The size of the image is 249x945 with 176 spectral bands and the spatial resolution is 30m. Pixels shown in black color correspond to undefined land uses.</h4>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab3/results/LoukiaRGB.png?raw=true" width="945" height="500">

Below you can see the three images for validation in RGB composite. Erato, Kirki and Nefeli.

<h4>The validation images in RGB composite. Each image has spatial resolution equal to 30m and 176 spectral bands. On top is Erato with size 241x1623. In middle is Kirki with size 245x1626 and in bottom is Nefeli with size 249x772. The ground truth labels are not given and the end goal is to make predictions for these images.</h4>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab3/results/ValidationImages.png?raw=true" width="945" height="500">

- <b> Approach to the classification problem: </b> For the classification of the hyperspectral images we develop several approaches and different models. At first, we examine we train some classic ML classifiers like Random forest and a Multi-Layer-Perceptron (MLP). These classifiers correspond to the pixel-based approach where the features consists of all the available pixels from the images of Dioni and Loukia. This approach is not the optimal one in order to make prediction to unknown images, e.g. Erato, Kirki and Nefeli, because the high-dependency of neighboring-pixels. To this end, we develop more sophisticated approaches and models to deal with this problem. A CNN model is designed and a patched based approached is utilized. We train the CNN by allowing maximum overlapping between the patches and with no overlapping at all. Furthermore, we use techniques of data augmentation and transfer learning. In the maximum overlapping case we achieve the highest score on the training images. However, this approach is not the appropriate one for making predictions to Erato, Kirki and Nefeli but we can still use this model to completey annotate our training images. In the following figure we see the annotation of Dioni using the CNN model.


<h4>Predictions made by the CNN with maximum overlapping on Dioni.</h4>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab3/results/PredDioniCNN.png?raw=true" width="945" height="500">

The best model in order to make predictions to Erato, Kirki and Nefeli turns out to be the one following the UNet principles. It achieves an 80% accuracy score on the test set and it is trained without overlapping images. Futhermore, with this approach we create a dataset we enough samples in order to train and test the model. In the following figures you can see the confusion matrix of the model on the test set and the predictions made on Erato, Kirki and Nefeli.

<h4>The Confusion matrix of the UNet model on the test set.</h4>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab3/results/UNet.png?raw=true" width="600" height="600">

<h4>Predictions made by the UNet On Erato.</h4>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab3/results/EratoPredsUNet.png?raw=true" width="945" height="500">

<h4>Predictions made by the UNet On Kirki.</h4>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab3/results/KirkiPredsUNet.png?raw=true" width="945" height="500">

<h4>Predictions made by the UNet On Nefeli.</h4>
<img src="https://github.com/ChrisNick92/Geospatial-Data/blob/main/Lab3/results/NefeliPredsUNet.png?raw=true" width="945" height="500">
