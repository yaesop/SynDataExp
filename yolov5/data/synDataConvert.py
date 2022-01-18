import json
import sys
import glob, os


# Opening JSON file
name = sys.argv[1]
altitude = sys.argv[2]
radius = sys.argv[3]
time = sys.argv[4]
model = sys.argv[5]
position = sys.argv[6]

print(model," ",position, " :",altitude,"_", radius, "_", time)

if position == "stand" :
    if name =='exp_desert_juliet':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_juliet/'
    elif name =='exp_desert_kelly':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_kelly/'
    elif name =='exp_desert_lucy':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_lucy/'
    elif name =='exp_desert_mary':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_mary/'
    elif name =='exp_desert_romeo':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_romeo/'
    elif name =='exp_desert_scott':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_scott/'
    elif name =='exp_desert_troy':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_troy/'
    elif name =='exp_desert_victor':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_victor/'
elif position == "prone":
    if name =='exp_desert_juliet':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_juliet_prone/'
    elif name =='exp_desert_kelly':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_kelly_prone/'
    elif name =='exp_desert_lucy':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_lucy_prone/'
    elif name =='exp_desert_mary':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_mary_prone/'
    elif name =='exp_desert_romeo':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_romeo_prone/'
    elif name =='exp_desert_scott':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_scott_prone/'
    elif name =='exp_desert_troy':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_troy_prone/'
    elif name =='exp_desert_victor':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_victor_prone/'
elif position == "squat":
    if name =='exp_desert_juliet':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_juliet_squat/'
    elif name =='exp_desert_kelly':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_kelly_squat/'
    elif name =='exp_desert_lucy':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_lucy_squat/'
    elif name =='exp_desert_mary':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_mary_squat/'
    elif name =='exp_desert_romeo':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_romeo_squat/'
    elif name =='exp_desert_scott':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_scott_squat/'
    elif name =='exp_desert_troy':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_troy_squat/'
    elif name =='exp_desert_victor':
        datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_victor_squat/'

f = open(datasetName + 'synthdata.json')

#imgs = glob.glob(datasetName+'*.png')
imgs = glob.glob('../../Object-Detection-Metrics/detections/*.txt')
# returns JSON object as
# a dictionary
#print(imgs)
data = json.load(f)

# Iterating through the json
# list
imgs_converted = []
for im in imgs:
    #print(im)
    if im.split('/')[-1].split('.')[0].split('_')[3]==altitude and im.split('/')[-1].split('.')[0].split('_')[4]==radius:
        imgs_converted.append(im.split('/')[-1].split('.')[0])
#print(imgs_converted)
for i in data:
    #print(i['image'])
    if i['image'].split('/')[1].split('.')[0] in imgs_converted:
        if i['image'].split('_')[3] == altitude and i['image'].split('_')[4]==radius:
            #print(i)
        
            #print(i['image'].split('/')[1].split('_')[4])
            #file1 = open("/media/yaesop/TOSHIBA EXT/dataset/synthdata_desert_juliet/labels/"+i['image'].split('.')[0]+".txt","x")
            file1 = open("../../Object-Detection-Metrics/groundtruths/"+i['image'].split('/')[1].split('.')[0]+".txt","x")
            #print("../../Object-Detection-Metrics/groundtruths/"+i['image'].split('/')[1].split('.')[0]+".txt")
            tmp = "person"
            tmp+=" "
            #tmp+= str(float(i['annotations'][0]['coordinates']['x'])+ float(i['annotations'][0]['coordinates']['width'])/2)
            tmp+= str(float(i['annotations'][0]['coordinates']['x']))
            tmp+=" "
            #tmp+= str(float(i['annotations'][0]['coordinates']['y'])+ float(i['annotations'][0]['coordinates']['height'])/2)
            tmp+= str(float(i['annotations'][0]['coordinates']['y']))
            tmp+=" "
            tmp+= str(float(i['annotations'][0]['coordinates']['width']))
            tmp+=" "
            tmp+= str(float(i['annotations'][0]['coordinates']['height']))
            file1.write(tmp)
            tmp = ""
            file1.close() #to change file access modes
           
