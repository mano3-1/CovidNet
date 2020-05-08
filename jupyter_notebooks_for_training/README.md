
The efficient net model was first trained on cropped dataset and thenfinetuned on the covid dataset to get better results.
All the standard metrics like confusion matrix ,F1 score ,precision ,recall were calculated in the jupyter notebook(named eff_net_fine_tune).
To get more efficiency we imported pretrained segmentation model and cropped the dataset by using that segmentation model(link was provided) 
and trained it on the dataset.
