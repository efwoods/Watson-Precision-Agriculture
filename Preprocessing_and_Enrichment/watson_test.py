'''from watson_developer_cloud import VisualRecognitionV3\
visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='988d558c4a7e45a98f2aa9f1d52a66d5be30287d'
)

classify(images_file=None, parameters=None, accept_language=None, images_file_content_type=None, images_filename=None)


api_key = 988d558c4a7e45a98f2aa9f1d52a66d5be30287d
'''
'''
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='988d558c4a7e45a98f2aa9f1d52a66d5be30287d')

with open('./fruitbowl.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        parameters=json.dumps({
            'classifier_ids': ['fruits_1462128776','SatelliteModel_6242312846'],
            'threshold': 0.6
        }))
print(json.dumps(classes, indent=2))


prez.jpg
fruitbowl.jpg
###
'''
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='988d558c4a7e45a98f2aa9f1d52a66d5be30287d')

with open('A_rusty_bridge_-_panoramio.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(images_file,
    parameters=json.dumps({'owners':[IBM, me]}))
print(json.dumps(classes, indent=2))

