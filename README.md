# image_entity_5000

* ResNet-101 trained on OpenImages v3.
* 5000 categories

## The environment

* docker - https://docs.docker.com/install/linux/docker-ce/ubuntu/
* nvidia-docker - https://github.com/NVIDIA/nvidia-docker

# Docker image(Flask)

https://drive.google.com/open?id=1M9GRzR9k9X-ilGrigqouay17ChuEzhfb

## Run

* `sudo docker pull tensorflow/serving:1.13.0-gpu`
* `sudo docker load -i flask-uwsgi-python-centos.tar`
* `https://github.com/MagicianQi/image_entity_5000`
* `cd image_entity_5000 && wget https://github.com/MagicianQi/image_entity_5000/releases/download/v0.1/models.tar.gz && tar -zxvf model.tar.gz`
* Specify the GPU ID: `vim deploy.sh`

    1.https://github.com/MagicianQi/image_entity_5000/blob/master/deploy.sh#L10
* Specify the model absolute path：`vim deploy.sh`

    1.https://github.com/MagicianQi/image_entity_5000/blob/master/deploy.sh#L12
* `bash deploy.sh`
* Test: `curl localhost:8080`

## Other

* Other API：https://github.com/MagicianQi/image_entity_5000/blob/master/flask_server.py
