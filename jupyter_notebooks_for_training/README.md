
The efficient net model was first trained on cropped dataset and then finetuned on the covid dataset to get better results.
All the standard metrics like confusion matrix ,F1 score ,precision ,recall were calculated in the jupyter notebook(named eff_net_fine_tune).<br/>
accuracy score : 0.8809523809523809<br/>
precision score : 0.8809523809523809<br/>
recall score : 0.8809523809523809<br/>
f1 score : 0.8809523809523809<br/>
confusion matrix of the above mentioned model :<br/>
!["confusion matrix"](https://github.com/mano3-1/CovidNet/blob/master/jupyter_notebooks_for_training/images/cm2.PNG)<br/>
To get more efficiency we imported pretrained segmentation model and cropped the dataset by using that segmentation model(link was provided) and trained it on the dataset. The standard metrcis for the model rae as followes:<br/>
accuracy score : 0.8571428571428571<br/>
precision score : 0.8571428571428571<br/>
recall score : 0.8571428571428571<br/>
f1 score : 0.8571428571428571<br/>
Confusion Matrix of the above mentioned model:<br/>
!["confusion matrix"](https://github.com/mano3-1/CovidNet/blob/master/jupyter_notebooks_for_training/images/cm.PNG)

To improve the accuracy and gradcams ,we tried a ensemble of two models which yielded relatively good gradcams.

cropped covid input:<br/>

!["covid affected lungs"](https://github.com/mano3-1/CovidNet/blob/master/results/covid.jpeg)<br/>

gradcam for covid affected lungs<br/>

!["gradcam for covid affected lungs"](https://github.com/mano3-1/CovidNet/blob/master/results/gradcam_covid.jpeg)<br/>

normal input:<br/>

!["normal lungs image"](https://github.com/mano3-1/CovidNet/blob/master/results/normal%20normal.jpeg)<br/>

gradcam for normal lungs:<br/>

!["graadcam for normal lungs images](https://github.com/mano3-1/CovidNet/blob/master/results/normal_gc.jpeg)<br/>

The above results were obtained by using an esnsemble of two classification models and their combined Grad-CAM heatmaps.
The inputs are cropped to focus on the lungs using the lungs segmentation model specified above.
The first model is pretraied on Non cropped pneumonia dataset and fine tuned on the center cropped covid data set.
The other model is pretraied on cropped pneumonia dataset and fine tuned on the cropped covid data set using segmentataion model.
