import json
import sys
import glob, os
import cv2

#store the data for training in ../syn_training/
# images in ../syn_training/images/
# labels in ../syn_training/labels/
# Convert the json file to each txt annotation to have centerX centerY Width Height

#select the training dataset. 
datasetNames = ['/media/yaesop/ARL_FZNV/extended20210222/desert_juliet/', \
'/media/yaesop/ARL_FZNV/extended20210222/desert_kelly/', \
'/media/yaesop/ARL_FZNV/extended20210222/desert_juliet_prone/', \
'/media/yaesop/ARL_FZNV/extended20210222/desert_kelly_prone/', \
'/media/yaesop/ARL_FZNV/extended20210222/desert_juliet_squat/', \
'/media/yaesop/ARL_FZNV/extended20210222/desert_kelly_squat/']

for datasetName in datasetNames:
    f = open(datasetName + 'synthdata.json')
    data = json.load(f)
    # get the original image 
    for i in data:
        altitude = int(i['image'].split('_')[3])
        radius = int(i['image'].split('_')[4])
        if (altitude==15 or altitude==20) and (radius == 45 or radius == 50): 
        #select low altitude and large radius
            image = cv2.imread(datasetName+"/"+ i['image'].split('/')[1])
            im_path = r'../syn_training/images/'+ i['image'].split('/')[1]
            cv2.imwrite(im_path , image)
            file1 = open("../syn_training/labels/"+i['image'].split('/')[1].split('.')[0]+".txt","x")
            xmin = float(i['annotations'][0]['coordinates']['x'])
            ymin = float(i['annotations'][0]['coordinates']['y'])
            width = float(i['annotations'][0]['coordinates']['width'])
            height = float(i['annotations'][0]['coordinates']['height'])
            tmp = "person"
            tmp+=" "
            tmp+= str( (xmin + width/2)/512 )
            tmp+=" "
            tmp+= str( (ymin + width/2)/512 )
            tmp+=" "
            tmp+= str( width/512 )
            tmp+=" "
            tmp+= str( height/512 )
            file1.write(tmp)
            tmp = ""
            file1.close() 
       
