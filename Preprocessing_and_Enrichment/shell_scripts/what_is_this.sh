#!/bin/sh
curl -X POST -F "images_file=$1" -F "owners=me" "https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key=59c3ae87c6ec4d70d9dd16ec5cfa0bb196c58fe6&version=2016-05-20"
