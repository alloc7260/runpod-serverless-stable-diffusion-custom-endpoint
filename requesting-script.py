import requests
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image

def base64_to_image_and_display(base64_strings):

    for i,per_image in enumerate(base64_strings):

        # Decode the Base64 string to bytes
        image_bytes = base64.b64decode(per_image)

        # Convert bytes to a PIL Image
        image_pil = Image.open(BytesIO(image_bytes))

        # Convert PIL Image to NumPy array
        image_np = np.array(image_pil)

        # Convert RGB to BGR (OpenCV uses BGR order)
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        # Display the image using OpenCV
        cv2.imshow(f"Base64 to Image {i}", image_bgr)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


url = "https://api.runpod.ai/v2/<endpoint id>/runsync"     # put your endpoint id here

payload = {"input": {
        "api_name": "txt2img",
        "prompt": "a red toy car with number 95 on it racing on track",                             # inference using base model
        # "prompt": "a red toy car with number 95 on it racing on track <lora:sdxl-base-10000:1>",  # inference using Lora checkpoint
        "seed": 1000,
        "sampler_index": "DDIM",
        "steps": 10,
        "negative_prompt": "blur",
        "batch_size": 1 
    }}

headers = {"Content-Type": "application/json",
           "Authorization": "Bearer <api key>"}                 # put your api key here            

response = requests.request("POST", url, json=payload, headers=headers)

print(response.json())

images = (response.json())['output']['images']
base64_to_image_and_display(images)