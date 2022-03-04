#!/bin/bash
for model in n s m l x; do
python train.py --imgsz 640 --data data/real.yaml --nosave --epoch 20 --freeze 200 --weights yolov5${model}.pt --device 0
done
#n 270 layers -> freezed 200 layers

