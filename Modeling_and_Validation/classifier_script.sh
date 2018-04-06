#!/bin/sh
curl -X POST \
--form "self_positive_examples=@$1" \
--form "negative_examples=@$2" \
--form "name=$1" \
"https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers?api_key=59c3ae87c6ec4d70d9dd16ec5cfa0bb196c58fe6&version=2016-05-20"
