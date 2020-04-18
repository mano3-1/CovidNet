# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:26:53 2020

@author: Lenovo
"""


import os
import cv2
import numpy as np
#import math
import argparse
from keras.preprocessing.image import ImageDataGenerator

parser = argparse.ArgumentParser()
parser.add_argument('--category' ,type = str ,default = 'covid')
args = parser.parse_args()
category = args.category

def load_images_and_labels(images ,dir):

    X_train=[]
    i=0
    for image in images:
        k=image
        i=i+1
        image=cv2.imread(dir+'/'+image)
        image=cv2.resize(image,(224,224))
        print(i,k,'is loaded')
        X_train.append(image)

    X_train=np.asarray(X_train)
    return X_train

def augmentation_and_save(images ,dir ,factor ,rotation_range ,save_dir):
    X_train=load_images_and_labels(images ,dir)
    print(X_train.shape)
    dgen=ImageDataGenerator(rotation_range=rotation_range)
    aug=dgen.flow(X_train ,save_to_dir=save_dir ,batch_size=1 ,save_prefix='aug',save_format='jpg')
    k=X_train.shape[0]
    for j in range(factor):
        i=0
        for X_batch in aug:
            if i==k:
                break
            else:
                i=i+1
if __name__ == '__main__':
    path = os.path.join('..\covid_cropped\train' ,category)
    images = os.listdir(path)
    augmentation_and_save(images, path, factor = 1, rotation_range = 30, save_dir = path)