#!/bin/bash

#for position in stand; do 
#for model in n s m l x; do  #nano small medium large; do
#cd /home/yaesop/syn_result/
#mkdir detect_${model}_${position}

#cd ~/SynDataExp/yolov5/
#for  dirName in desert_juliet desert_kelly desert_lucy desert_mary desert_romeo desert_scott desert_troy desert_victor; do
#    for tr in 1 2 3 4; do
#    python detect.py --imgsz 512 --save-txt --save-conf --nosave --source /media/yaesop/ARL_FZNV/extended20210222/$dirName/trial${tr} --weights yolov5${model}.pt --project /home/yaesop/syn_result/detect_${model}_${position}/ --classes 0
#    mkdir /home/yaesop/syn_result/detect_${model}_${position}/exp_${dirName}
#    rsync -a /home/yaesop/syn_result/detect_${model}_${position}/exp /home/yaesop/syn_result/detect_${model}_${position}/exp_${dirName}
#    rm -rf /home/yaesop/syn_result/detect_${model}_${position}/exp
#    done
#done
#done
#done

for position in squat prone; do 
for model in n s m l x; do  #nano small medium large; do
cd /home/yaesop/syn_result/
mkdir detect_${model}_${position}

cd ~/SynDataExp/yolov5/
for  dirName in desert_juliet_${position} desert_kelly_${position} desert_lucy_${position} desert_mary_${position} desert_romeo_${position} desert_scott_${position} desert_troy_${position} desert_victor_${position}; do
    for tr in 1 2 3 4; do
    python detect.py --imgsz 512 --save-txt --save-conf --nosave --source /media/yaesop/ARL_FZNV/extended20210222/$dirName/trial${tr} --weights yolov5${model}.pt --project /home/yaesop/syn_result/detect_${model}_${position}/ --classes 0
    mkdir /home/yaesop/syn_result/detect_${model}_${position}/exp_${dirName}
    rsync -a /home/yaesop/syn_result/detect_${model}_${position}/exp /home/yaesop/syn_result/detect_${model}_${position}/exp_${dirName}
    rm -rf /home/yaesop/syn_result/detect_${model}_${position}/exp
    done
done
done
done
