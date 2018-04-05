import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='59c3ae87c6ec4d70d9dd16ec5cfa0bb196c58fe6')

with open('A_rusty_bridge_-_panoramio.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        parameters=json.dumps({
            'owners': ['me', 'IBM'], 
			'threshold': 0.0,
			"classifier_id": "rustxzip_39936321"
        }))
print(json.dumps(classes, indent=2))
