#!/usr/bin/env bash

# ResNet-101 model

sudo docker run \
--runtime=nvidia \
--name resnet101 \
--restart always \
-d \
-e CUDA_VISIBLE_DEVICES=0 \
-p 8500:8500 -p 8501:8501 \
--mount type=bind,source=/home/qishuo/PycharmProjects/resnet101/models,target=/models/resnet101 \
-t --entrypoint=tensorflow_model_server tensorflow/serving:1.13.0-gpu \
--port=8500 --rest_api_port=8501 \
--model_name=resnet101 \
--model_base_path=/models/resnet101 \
--per_process_gpu_memory_fraction=0.8

# Build

sudo docker build -t multi_label_5000 .

# flask model

sudo docker run \
--link resnet101:resnet101 \
-p 8080:8080 -itd multi_label_5000
