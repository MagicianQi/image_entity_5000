# -*- coding: utf-8 -*-

import flask
import json

from backend.resnet101 import ResNet101
from utils.FOP import Logger
from settings import *

app = flask.Flask(__name__)
resnet101 = ResNet101()
logger = Logger(ERROR_LOG_PATH, "error")

@app.route("/")
def homepage():
    return "Welcome to the SOUL Place Classification REST API!"


@app.route("/health")
def health_check():
    return "OK"


@app.route("/api/predict", methods=["POST", "GET"])
def predict_sensitive():
    res = {
        "code": 200,
        "message": "OK"
    }
    if flask.request.method == "POST":
        try:
            data = flask.request.data.decode('utf-8')
            data = json.loads(data)
            if "imgUrl" in data:
                image_base64 = resnet101.convert_base64_from_url(data["imgUrl"])

            elif "imgBase64" in data:
                image_base64 = data["imgBase64"]
            else:
                res.update({"code": 400})
                res.update({ "message": "Bad Request."})
                return flask.jsonify(res)
            confidence_list, top_index = resnet101.predict(image_base64)
            result = []
            confidence_thresh = CLASSIFICATION_THRESHOLD
            class_names = resnet101.class_names
            if "confidence" in data:
                confidence_thresh = data["confidence"]
            for index in top_index:
                if confidence_list[index] < confidence_thresh:
                    break
                result.append([class_names[index], confidence_list[index], index])
            res.update({"prediction": result})
        except Exception as e:
            logger.out_print([e])
    return flask.jsonify(res)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8585)
