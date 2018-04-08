#!/bin/sh
curl -X DELETE \
"https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers/$1?api_key=59c3ae87c6ec4d70d9dd16ec5cfa0bb196c58fe6&version=2016-05-20"
