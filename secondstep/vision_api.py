import io
import os
from .models import UserObject
from .serializers import ObjectSerializer

def localize_objects(path):
    """Detects labels in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    # response = client.label_detection(image=image)
    # labels = response.label_annotations
    # print('Labels:')
    # print(labels[0].description)

    print('objects:')
    print(objects[0].name)

    # if response.error.message:
    #     raise Exception(
    #         '{}\nFor more info on error messages, check: '
    #         'https://cloud.google.com/apis/design/errors'.format(
    #             response.error.message))

    return objects[0].name
