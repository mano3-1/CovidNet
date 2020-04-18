# CovidNet
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
