# CovidNet
The aim is not only to make a model which can classify the chest x-ray data but also to extract the heat maps  of the x-ray for faster diagnosis and making it more reliable to use in real time.
Plans include:
1. using a lung segmenatation model to get rid of unnecessary biases and create new data.
2. using self super learning to pretrain a CNN model with new data taken from various sources.
3. fine tuining it on the classification task and getting Grad-cam heatmaps.
4.creating a fully optimised pipeline for the above in one package.
