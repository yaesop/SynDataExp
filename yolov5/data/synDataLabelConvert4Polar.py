import json
import glob, os
import sys
# Opening JSON file
name = sys.argv[1]
#imgs = glob.glob('../../yolov5/runs/detect/'+expNum+'/labels/*.txt')
altitude = sys.argv[2]
radius = sys.argv[3]
time1 = sys.argv[4]
model = sys.argv[5]
position = sys.argv[6]
img_selected =[]
for time in ["1", "2", "3", "4"]:
    if position == "stand" :
        if name =='exp_desert_juliet':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_juliet/trial'+time+'/*.png'
        elif name =='exp_desert_kelly':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_kelly/trial'+time+'/*.png'
        elif name =='exp_desert_lucy':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_lucy/trial'+time+'/*.png'
        elif name =='exp_desert_mary':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_mary/trial'+time+'/*.png'
        elif name =='exp_desert_romeo':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_romeo/trial'+time+'/*.png'
        elif name =='exp_desert_scott':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_scott/trial'+time+'/*.png'
        elif name =='exp_desert_troy':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_troy/trial'+time+'/*.png'
        elif name =='exp_desert_victor':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_victor/trial'+time+'/*.png'
    elif position == "prone":
        if name =='exp_desert_juliet':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_juliet_prone/trial'+time+'/*.png'
        elif name =='exp_desert_kelly':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_kelly_prone/trial'+time+'/*.png'
        elif name =='exp_desert_lucy':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_lucy_prone/trial'+time+'/*.png'
        elif name =='exp_desert_mary':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_mary_prone/trial'+time+'/*.png'
        elif name =='exp_desert_romeo':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_romeo_prone/trial'+time+'/*.png'
        elif name =='exp_desert_scott':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_scott_prone/trial'+time+'/*.png'
        elif name =='exp_desert_troy':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_troy_prone/trial'+time+'/*.png'
        elif name =='exp_desert_victor':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_victor_prone/trial'+time+'/*.png'
    elif position == "squat":
        if name =='exp_desert_juliet':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_juliet_squat/trial'+time+'/*.png'
        elif name =='exp_desert_kelly':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_kelly_squat/trial'+time+'/*.png'
        elif name =='exp_desert_lucy':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_lucy_squat/trial'+time+'/*.png'
        elif name =='exp_desert_mary':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_mary_squat/trial'+time+'/*.png'
        elif name =='exp_desert_romeo':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_romeo_squat/trial'+time+'/*.png'
        elif name =='exp_desert_scott':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_scott_squat/trial'+time+'/*.png'
        elif name =='exp_desert_troy':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_troy_squat/trial'+time+'/*.png'
        elif name =='exp_desert_victor':
            datasetName = '/media/yaesop/ARL_FZNV/extended20210222/desert_victor_squat/trial'+time+'/*.png'

    #print(datasetName.split('/'))
    imgs = glob.glob(datasetName)
    #print(imgs)

    #xywh -> 1,2,3,4
    imgs.sort()
    for img in imgs:
        if img.split('/')[-1].split('.')[0].split("_")[3]==altitude and img.split('/')[-1].split('.')[0].split("_")[4]==radius:
            img_selected.append(img)
#print(len(img_selected))
k = 0

for img in img_selected:
    #fileName = '/home/yaesop/syn_result/detect_'+model+'_'+position+'/'+name+'/exp/labels/'+ img.split('/')[7].split('.')[0]+".txt"
    fileName = '/home/yaesop/syn_result/detect_'+model+'_'+position+'/'+name+'_'+position+'/exp/labels/'+ img.split('/')[7].split('.')[0]+".txt"
    if os.path.exists(fileName):
        #print("ex")
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
    #k=k+1
