rm -rf output.txt


for  altitude in 5 10 15 20 25 30 35 40 45 50 ; do
for  radius in 5 10 15 20 25 30 ; do
    rm -rf groundtruths/
    mkdir groundtruths
    rm -rf detections/
    mkdir detections
    cd ~/yolov5/data
    python synDataLabelConvert.py $altitude $radius
    python synDataConvert.py $altitude $radius
    
    cd ~/Object-Detection-Metrics/

    python pascalvoc.py -detformat xywh -gtformat xywh -np > tmp/output.txt
    echo $altitude $radius >> output.txt
    cat tmp/output.txt >> output.txt
done
done
