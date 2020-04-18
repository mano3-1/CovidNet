# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:14:07 2020

@author: Lenovo
"""


import os
import shutil
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--virus' ,type = str ,default = 'COVID-19')
parser.add_argument('--x_ray_view' ,type = str ,default = 'PA')
parser.add_argument('--outputDir' ,type = str ,default = r'D:\COMPUTERS\AI\dataset_and_embeddings\covid_dataset\covid')
args = parser.parse_args()

virus = args.virus
x_ray_view = args.x_ray_view
outputDir = args.outputDir
path = r'D:\COMPUTERS\AI\DEEP_LEARNING\COVID\covid-chestxray-dataset'
metadata = r'D:\COMPUTERS\AI\DEEP_LEARNING\COVID\covid-chestxray-dataset\metadata.csv'

metadata_csv = pd.read_csv(metadata)

for (i,row) in metadata_csv.iterrows():
    if row['finding'] != virus or row['view'] != x_ray_view:
        continue
    file_dir = os.path.join(path , row['folder'] ,row['filename'])
    out_dir = os.path.join(outputDir ,row['filename'])
    shutil.copy(file_dir ,out_dir)