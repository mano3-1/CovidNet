# CovidNet
Run the Inference.ipynb in colab by opening it and clicking it on open in colab button.


segmetation model is taken from:https://www.kaggle.com/nikhilpandey360/lung-segmentation-from-chest-x-ray-dataset

covid data is taken from:https://github.com/ieee8023/covid-chestxray-dataset

additional pneumonia data for pretraining is taken from:https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

link to google drive:https://drive.google.com/drive/folders/18_m0UC6-mbFZ7k8rHxJesZTOEcSp6GIv?usp=sharing

The aim is not only to make a model which can classify the chest x-ray data but also to extract the heat maps  of the x-ray for faster diagnosis and making it more reliable to use in real time.
Plans include:
1. using a lung segmenatation model to get rid of unnecessary biases and create new data.
2. using self super learning to pretrain a CNN model with new data taken from various sources.
3. fine tuining it on the classification task and getting Grad-cam heatmaps.
4.creating a fully optimised pipeline for the above in one package

Reason to choose X-ray scans and not CT scans is due to the fact that x-ray is cheaper and safer than CT scans and almost all hospitals have them.
Results look like:

Covid 19 affected lungs<br/>

!["Covid 19 affected lungs"](https://github.com/mano3-1/CovidNet/blob/master/denoising%20autoencoder/gradcams/sample.jpeg)<br/>

Grad cam of covid 19 affected lungs(input was cropped using Bounding Box model)<br/>

!["Grad cam of covid 19 affected lungs"](https://github.com/mano3-1/CovidNet/blob/master/denoising%20autoencoder/gradcams/covid.PNG)<br/>

pneumonia affected Lungs<br/>

!["pneumonia affected Lungs"](https://github.com/mano3-1/CovidNet/blob/master/denoising%20autoencoder/gradcams/PNEUMONIA.jpeg)<br/>

gradcam of normal Lungs(input was cropped using Bounding Box model) <br/>

!["gradcam of pneumonia affected Lungs"](https://github.com/mano3-1/CovidNet/blob/master/denoising%20autoencoder/gradcams/pneumonia.PNG)<br/>


The above results are obtained by training Denoising autoencoder on augmeneted cropped pneumonia dataset and then encoder is taken and re trained it on covid data for classification.But due to high bias in the data the accuracy score it little bit low.We are trying to improve it by using various methods such as outlier detection by generative models(using variational autoencoders to detect the outliers) and active learning.

