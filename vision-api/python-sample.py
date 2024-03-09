import io
import os

from google.cloud import vision
client = vision.ImageAnnotatorClient()
file_name = os.path.abspath('D:/vertex-ai/vision-api/shanghai.jpeg')
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    
image = vision.Image(content=content)
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels: ')
for label in labels:
    print(label.description)
    
if response.error.message:
    raise Exception(
        "{}\nFor more info on error messages, check: "
        "https://cloud.google.com/apis/design/errors".format(response.error.message)
    )