#!/bin/bash
#cd /media/yaesop/YAESOP\'S/exp_small/
#for file in ~/SynDataExp/yolov5/runs/detect/*/labels/*.txt; do 
#    mv $file .
#done
cd ~/SynDataExp/Object-Detection-Metrics/
#declare -a arr=("exp" "exp2" "exp3" "exp4" "exp5" "exp6" "exp7" "exp8")

for position in squat prone; do 

for mdl in n; do  #nano small medium large; do
for time in 1 2 3 4 ; do
rm -rf output.txt
for  radius in 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80; do
for  altitude in 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80; do

    rm -rf groundtruths/
    mkdir groundtruths
    rm -rf detections/
    mkdir detections

## now loop through the above array

for dirName in  exp_desert_juliet exp_desert_kelly exp_desert_lucy exp_desert_mary exp_desert_romeo exp_desert_scott exp_desert_troy exp_desert_victor ; do
    cd ~/SynDataExp/yolov5/data
    python synDataLabelConvert.py $dirName $altitude $radius $time $mdl $position
    python synDataConvert.py $dirName $altitude $radius $time $mdl $position
done
    cd ~/SynDataExp/Object-Detection-Metrics/
    python pascalvoc.py --threshold 0.5 -detformat xywh -gtformat xywh -np > tmp/output.txt
    echo $altitude $radius >> output.txt
    cat tmp/output.txt >> output.txt
done
done
    mv output.txt /home/yaesop/syn_result/output_${mdl}_${position}_${time}.txt
    python plotting.py $time $mdl $position
done
done
done
