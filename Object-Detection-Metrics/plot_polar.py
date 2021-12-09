#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:54:04 2021

@author: ytshen
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_polar(data, max_value=0, step=10, name=""):
    data = data.tolist()
    data.append(data[0])
    
    plt.figure(figsize=(10, 6))
    ax = plt.subplot(polar=True)
    
    if(max_value != 0):
        ax.set_ylim(0, max_value)
        ax.set_yticks(np.arange(0, max_value, step))
    
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
 
    theta = np.linspace(0, 2 * np.pi, len(data))
 
    angle = [str(a * 2) if (a * 2) %10 == 0 else "" for a in list(range(180))]
    lines, labels = plt.thetagrids(range(0, 360, int(360/len(angle))), (angle))

    plt.plot(theta, data)
    plt.fill(theta, data, 'b', alpha=0.1)
    plt.title(name)
    plt.show()
    
import json
import glob, os
import sys
# Opening JSON file
test = np.zeros(180)
imgs = glob.glob('/media/yaesop/YAESOP\'S/detect_nano_standing/')
#print(imgs)
altitude = sys.argv[2]
radius = sys.argv[3]
time = sys.argv[4]
#xywh -> 1,2,3,4
img_selected =[]
imgs.sort()
for img in imgs:
    if img.split('/')[5].split('.')[0].split("_")[3]==altitude and img.split('/')[5].split('.')[0].split("_")[4]==radius:
        #fileName = '/media/yaesop/YAESOP\'S/detect_nano_standing/'+name+'/labels/'+ img.split('/')[5].split('.')[0]+".txt"
        img_selected.append(img)    
for img in img_selected:
        test[int(int(img.split('/')[5].split('.')[0].split("_")[-2])/2)]
#test = np.arange(180)
plot_polar(test, max_value=np.max(test), step=30, name="test polar plot")
