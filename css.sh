#!/bin/bash

echo "Uploading CSS to S3..."
aws s3 cp ./static/css/style.css s3://play2learn-bucket/css/style.css --acl public-read --content-type "text/css"

# open this file in terminal
# run (first) 'chmod +x css.sh'
# run (second) './css.sh'
# do NOT run this script unless you make changes to './css/styles.css'