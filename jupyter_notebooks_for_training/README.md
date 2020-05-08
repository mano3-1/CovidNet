
The efficient net model was first trained on cropped dataset and thenfinetuned on the covid dataset to get better results.
All the standard metrics like confusion matrix ,F1 score ,precision ,recall were calculated in the jupyter notebook(named eff_net_fine_tune).<br/>
accuracy score : 0.8809523809523809<br/>
precision score : 0.8809523809523809<br/>
recall score : 0.8809523809523809<br/>
f1 score : 0.8809523809523809<br/>
confusion matrix of the above mentioned model :<br/>
!["confusion matrix"](https://github.com/mano3-1/CovidNet/blob/master/jupyter_notebooks_for_training/images/cm2.PNG)
To get more efficiency we imported pretrained segmentation model and cropped the dataset by using that segmentation model(link was provided) and trained it on the dataset. The standard metrcis for the model rae as followes:<br/>
accuracy score : 0.8571428571428571<br/>
precision score : 0.8571428571428571<br/>
recall score : 0.8571428571428571<br/>
f1 score : 0.8571428571428571<br/>
Confusion Matrix of the above mentioned model:<br/>
!["confusion matrix"](https://github.com/mano3-1/CovidNet/blob/master/jupyter_notebooks_for_training/images/cm.PNG)

