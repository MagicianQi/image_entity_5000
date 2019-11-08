import requests
import json
import base64
import numpy as np
from io import BytesIO

# pip3 install pillow
from PIL import Image


def image_to_base64(image_url):
    response = requests.get(image_url)
    response = response.content
    bytes_obj = BytesIO(response)
    img = Image.open(bytes_obj).convert('RGB')
    output_buffer = BytesIO()
    img.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str.decode()


post_json = {
	"imgBase64": image_to_base64("https://chat.cdn.soulapp.cn/chat-image/2019-05-28/7181ab39-7024-4a4b-915e-a93516ffac6d-1559055665705.jpeg"),
	"confidence": 0.1
}

response = requests.post("http://172.29.100.23:8585/api/predict", data=json.dumps(post_json))
response.raise_for_status()
result = response.json()
predictions = result["prediction"]
print(predictions)
