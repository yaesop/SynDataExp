#!/bin/bash
#cd /media/yaesop/YAESOP\'S/exp_small/
#for file in ~/SynDataExp/yolov5/runs/detect/*/labels/*.txt; do 
#    mv $file .
#done
cd ~/SynDataExp/Object-Detection-Metrics/

for position in stand squat prone; do 

for model in n s m l x; do  #nano small medium large; do
for time in 1 2 3 4; do
rm -rf output.txt
for  radius in 5 30 55 80; do
for  altitude in 5 25 45  ; do

    rm -rf groundtruths/
    mkdir groundtruths
    rm -rf detections/
    mkdir detections

## now loop through the above array
for dirName in exp_desert_juliet exp_desert_kelly exp_desert_lucy exp_desert_mary exp_desert_romeo exp_desert_scott exp_desert_troy exp_desert_victor ; do
    cd ~/SynDataExp/yolov5/data
    python synDataLabelConvert4Polar.py $dirName $altitude $radius $time $model $position
    python synDataConvert4Polar.py $dirName $altitude $radius $time $mdl $position
done    

    cd ~/SynDataExp/Object-Detection-Metrics/
    #rm output_${model}_${position}_${altitude}_${radius}.txt
    python polar_eval.py $altitude $radius $model $position #> tmp/output.txt
    cat tmp/output.txt >> /home/yaesop/syn_result/output_${model}_${position}_${altitude}_${radius}.txt
done
done
done
done
done
