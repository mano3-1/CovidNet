# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:14:38 2020

@author: Lenovo
"""


from PIL import Image
import os


params = {'per_w' : 0.80 ,'per_h' : 0.85}

def crop_and_save(img_dir ,per_w ,per_h ,save_dir = None):
    img = Image.open(img_dir)
    width, height = img.size   
    new_width ,new_height = int(per_w*width) ,int(per_h*height)
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    cropped = img.crop((left ,top ,right ,bottom))
    if save_dir is not None:
        cropped.save(save_dir)
        
if __name__ == '__main__':
    directory = '..\covid_dataset'
    folders = os.listdir(directory)
    for folder in folders:
        print(folder)
        save_dir = '..\covid_cropped'
        os.mkdir(os.path.join(save_dir ,folder))
        save_dir = save_dir +'/'+ folder
        load_dir = directory +'/'+ folder
        for subfolder in os.listdir(load_dir):
            print('***',subfolder)
            os.mkdir(os.path.join(save_dir ,subfolder))
            sub_save_dir = save_dir + '/' + subfolder
            present_load_dir = os.path.join(load_dir ,subfolder)
            for file in os.listdir(present_load_dir):
                file_name = present_load_dir + '/' + file
                present_save_dir = sub_save_dir + '/' + file
                crop_and_save(file_name ,params['per_w'] ,params['per_h'] ,present_save_dir)
