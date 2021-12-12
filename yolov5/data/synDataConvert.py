import json
import sys
import glob, os


# Opening JSON file
name = sys.argv[1]
print(name)
if name =='exp':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_juliet2/'
elif name =='exp2':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_kelly2/'
elif name =='exp3':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_lucy2/'
elif name =='exp4':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_mary2/'
elif name =='exp5':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_romeo2/'
elif name =='exp6':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_scott2/'
elif name =='exp7':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_troy2/'
elif name =='exp8':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_victor2/'

f = open(datasetName + 'synthdata.json')

#imgs = glob.glob(datasetName+'*.png')
imgs = glob.glob('../../Object-Detection-Metrics/detections/*.txt')
# returns JSON object as
# a dictionary
#print(imgs)
data = json.load(f)
altitude = sys.argv[2]
radius = sys.argv[3]
# Iterating through the json
# list
imgs_converted = []
for im in imgs:
    imgs_converted.append(im.split('/')[-1].split('.')[0])
#print(imgs_converted)
for i in data:
    #print(i['image'])
    #print(i['image'].split('/')[1].split('_')[4])
    if i['image'].split('.')[0] in imgs_converted:
        if i['image'].split('_')[3] == altitude and i['image'].split('_')[4]==radius:
            #print(i['image'])
        
            #print(i['image'].split('/')[1].split('_')[4])
            #file1 = open("/media/yaesop/TOSHIBA EXT/dataset/synthdata_desert_juliet/labels/"+i['image'].split('.')[0]+".txt","x")
            file1 = open("../../Object-Detection-Metrics/groundtruths/"+i['image'].split('.')[0]+".txt","x")
            tmp = "person"
            tmp+=" "
            tmp+= str(float(i['annotations'][0]['coordinates']['x'])+ float(i['annotations'][0]['coordinates']['width'])/2)
            tmp+=" "
            tmp+= str(float(i['annotations'][0]['coordinates']['y'])+ float(i['annotations'][0]['coordinates']['height'])/2)
            tmp+=" "
            tmp+= str(float(i['annotations'][0]['coordinates']['width']))
            tmp+=" "
            tmp+= str(float(i['annotations'][0]['coordinates']['height']))
            file1.write(tmp)
            tmp = ""
            file1.close() #to change file access modes
           
