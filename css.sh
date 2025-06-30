#!/bin/bash
# uploading 

echo "Uploading CSS to S3..."
aws s3 cp ./static/css/style.css s3://play2learn-bucket/css/style.css --acl public-read --content-type "text/css"