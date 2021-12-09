#!/bin/bash
#cd /media/yaesop/YAESOP\'S/exp_small/
#for file in ~/SynDataExp/yolov5/runs/detect/*/labels/*.txt; do 
#    mv $file .
#done
cd ~/SynDataExp/Object-Detection-Metrics/
$position = squatting
$model = nano
#declare -a arr=("exp" "exp2" "exp3" "exp4" "exp5" "exp6" "exp7" "exp8")
for time in 0; do
rm -rf output.txt
for  radius in 5  ; do
for  altitude in 5   ; do

    rm -rf groundtruths/
    mkdir groundtruths
    rm -rf detections/
    mkdir detections

## now loop through the above array

for dirName in exp exp2 exp3 exp4 exp5 exp6 exp7 exp8 ; do
    cd ~/SynDataExp/yolov5/data
    python synDataLabelConvert4Polar.py $dirName $altitude $radius $time $model $position
    python synDataConvert4Polar.py $dirName $altitude $radius
done    

    cd ~/SynDataExp/Object-Detection-Metrics/
    rm output_${altitude}_${radius}.txt
    python  polar_eval.py $altitude $radius > tmp/output.txt
    cat tmp/output.txt >> output_${altitude}_${radius}.txt
done
done
done
