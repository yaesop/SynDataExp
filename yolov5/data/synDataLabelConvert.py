import json
import glob, os
import sys
# Opening JSON file
name = sys.argv[1]
#imgs = glob.glob('../../yolov5/runs/detect/'+expNum+'/labels/*.txt')
if name =='exp':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_juliet2/*.png'
elif name =='exp2':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_kelly2/*.png'
elif name =='exp3':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_lucy2/*.png'
elif name =='exp4':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_mary2/*.png'
elif name =='exp5':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_romeo2/*.png'
elif name =='exp6':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_scott2/*.png'
elif name =='exp7':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_troy2/*.png'
elif name =='exp8':
    datasetName = '/media/yaesop/YAESOP\'S/synthdata_desert_victor2/*.png'
#print(datasetName.split('/'))
imgs = glob.glob(datasetName)
#print(imgs)
altitude = sys.argv[2]
radius = sys.argv[3]
time = sys.argv[4]
model = sys.argv[5]
position = sys.argv[6]
#xywh -> 1,2,3,4
k=0
imgs.sort()
imgs_selected = []
for img in imgs:
    fileName = '/media/yaesop/YAESOP\'S/detect_'+model+'_'+position+'/'+name+'/labels/'+ img.split('/')[5].split('.')[0]+".txt"
    if img.split('/')[5].split('.')[0].split("_")[3]==altitude and img.split('/')[5].split('.')[0].split("_")[4]==radius:
        imgs_selected.append(img)
imgs_selected.sort()
for img in imgs_selected:
    fileName = '/media/yaesop/YAESOP\'S/detect_'+model+'_'+position+'/'+name+'/labels/'+ img.split('/')[5].split('.')[0]+".txt"
    if k%4 == int(time):

        if os.path.exists(fileName):

            with open(fileName) as f:
                for fLine in f:
                    tmp=""
                    if fLine.startswith("0"):
                        tmp="person"   
                        tmp+=" "
                        tmp+= str(float(fLine.split(" ")[5]))
                        tmp+=" "
                        tmp+= str( float(fLine.split(" ")[1])*512)
                        tmp+=" "
                        tmp+= str( float(fLine.split(" ")[2])*512)
                        tmp+=" "
                        tmp+= str( float(fLine.split(" ")[3])*512)
                        tmp+=" "
                        tmp+= str(float(fLine.split(" ")[4])*512)
        else:
            tmp="person"   
            tmp+=" "
            tmp+= str(0)
            tmp+=" "
            tmp+= str(0)
            tmp+=" "
            tmp+= str(0)
            tmp+=" "
            tmp+= str(0)
            tmp+=" "
            tmp+= str(0)
        file1 = open('../../Object-Detection-Metrics/detections/'+fileName.split('/')[-1],"x")
        file1.write(tmp)
        file1.close() #to change file access modes
    k= k+1
