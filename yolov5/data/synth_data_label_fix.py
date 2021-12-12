#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Synthetic Training Data Generation Script
synth_data.py
Description: 
Outputs:
Last edit: 11 July 2020

POC: Damon Conover, Army Research Laboratory
    damon.m.conover.civ@mail.mil
    301.394.0240
    
Usage: python synth_data.py <arguments>
Arguments: 
Example: 
"""

import cv2
import os
import re
import math
import sys

# python synth_data.py '/home/damon/Unity/extractTrainingData_20200710/out/' 'synthdata' 't72'
# cp *_id.png ~/Unity/extractTrainingData_20200710/out/mask/
# rm *_id.png
# ffmpeg -y -pattern_type glob -framerate 50 -i "*.png" -c:v libx264 -r 30 -pix_fmt yuv420p synthData_t72_50fps.mp4

# dir_png = "/home/damon/Unity/extractTrainingData_20200702/out/"
# name = "synthdata"
# target = "t72"

dir_png = sys.argv[1]
name    = sys.argv[2]
target  = sys.argv[3]

fn_out  = "{}.json".format(name)
dir_msk = "{}/mask/".format(dir_png)
f       = open("{}/{}".format(dir_png, fn_out), "w")
f.write("[\n")
first = 0
for idx, fn in enumerate(os.listdir(dir_msk)):
    if fn.endswith("_id.png"):        
        trial   = re.split('_id.png', fn)
        fn_img  = "{}_img.png".format(trial[0])
        
        print(idx)
        
        img0    = cv2.imread("{}/{}".format(dir_png, fn_img), cv2.IMREAD_COLOR)
        img     = cv2.imread("{}/{}".format(dir_msk, fn),cv2.IMREAD_GRAYSCALE)
        _, msk  = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
        pts     = cv2.findNonZero(msk)
        x, y, w, h = cv2.boundingRect(pts)
        img0    = cv2.rectangle(img0, (x,y), (x+w,y+h), (0,255,0), 3)
        # x = int(x + math.ceil(w/2))
        # y = int(y + math.ceil(h/2))
        x = int(x)
        y = int(y)

        # fn_img_out = "{}_out.png".format(trial[0])
        # cv2.imwrite(fn_img_out, img0)        
        # cv2.imshow('image', img0)
        # cv2.waitKey()
        
        if (first == 1):
            f.write(",\n")
        elif (first == 0):
            first = 1
        f.write("\t{\n")
        f.write("\t\t\"image\": \"{}\",\n".format(fn_img))
        f.write("\t\t\"annotations\": [\n")
        f.write("\t\t\t{\n")
        f.write("\t\t\t\t\"label\": \"{}\",\n".format(target))
        f.write("\t\t\t\t\"coordinates\": {\n")
        f.write("\t\t\t\t\t\"x\": {},\n".format(x))
        f.write("\t\t\t\t\t\"y\": {},\n".format(y))
        f.write("\t\t\t\t\t\"width\": {},\n".format(w))
        f.write("\t\t\t\t\t\"height\": {}\n".format(h))
        f.write("\t\t\t\t}\n")
        f.write("\t\t\t}\n")
        f.write("\t\t]\n")
        f.write("\t}")
f.write("\n")
f.write("]\n")
f.close()