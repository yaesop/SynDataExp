#!/bin/bash
cd /media/yaesop/YAESOP\'S/
mkdir detect_xlarge_squatting
#for file in ~/SynDataExp/yolov5/runs/detect/*/labels/*.txt; do 
#    mv $file .
#done
cd ~/SynDataExp/yolov5/
for  dirName in synthdata_desert_juliet2 synthdata_desert_kelly2 synthdata_desert_lucy2 synthdata_desert_mary2 synthdata_desert_romeo2 synthdata_desert_scott2 synthdata_desert_troy2 synthdata_desert_victor2; do
    
    python detect.py --imgsz 512 --save-txt --save-conf --nosave --source /media/yaesop/YAESOP\'S/$dirName --weights yolov5x.pt --project /media/yaesop/YAESOP\'S/detect_xlarge_squatting/ --classes 0

done
