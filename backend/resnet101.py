# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import io
import json
import base64
import requests
import numpy as np

from PIL import Image

from settings import *


class ResNet101(object):

    def __init__(self,
                 resnet_101_predict_url=RESNET_101_PREDICT_URL,
                 class_name_file_en=CLASS_NAMES_EN,
                 class_name_file_zh=CLASS_NAMES_ZH):
        self.resnet_101_predict_url = resnet_101_predict_url
        class_names_en = []
        class_names_zh = []
        with open(class_name_file_en) as class_file:
            for line in class_file.readlines():
                class_names_en.append(line.strip())
        with open(class_name_file_zh) as class_file:
            for line in class_file.readlines():
                class_names_zh.append(line.strip())
        self.class_names = ["{} - {}".format(x, y) for x, y in zip(class_names_en, class_names_zh)]

    def predict(self, image_b64):
        post_json = {
            "instances": [{
                "b64": image_b64
            }]
        }
        response = requests.post(self.resnet_101_predict_url, data=json.dumps(post_json))
        response.raise_for_status()
        result = response.json()
        confidence = result["predictions"]
        top_k = np.array(confidence).argsort()[::-1]
        return confidence, top_k.tolist()

    @staticmethod
    def convert_base64_from_url(image_url):
        response = requests.get(image_url)
        response = response.content
        bytes_obj = io.BytesIO(response)
        img = Image.open(bytes_obj).convert('RGB')
        output_buffer = io.BytesIO()
        img.save(output_buffer, format='JPEG')
        byte_data = output_buffer.getvalue()
        base64_str = base64.b64encode(byte_data)
        return base64_str.decode()
