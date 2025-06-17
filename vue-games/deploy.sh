#!/bin/bash

# ----------- Math Facts -----------
echo "Building Math Facts game..."
VUE_APP_GAME=math-facts npm run build

echo "Syncing Math Facts files to S3..."
aws s3 sync ./dist/js/ s3://play2learn-bucket/static/vue-games/math-facts/js/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "application/javascript" \
  --cache-control "no-cache, no-store, must-revalidate"

aws s3 sync ./dist/css/ s3://play2learn-bucket/static/vue-games/math-facts/css/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "text/css" \
  --cache-control "no-cache, no-store, must-revalidate"

# ----------- Clear dist before next build -----------
echo "Cleaning build directory..."
rm -rf dist/

# ----------- Anagram Hunt -----------
echo "Building Anagram Hunt game..."
VUE_APP_GAME=anagram-hunt npm run build

echo "Syncing Anagram Hunt files to S3..."
aws s3 sync ./dist/js/ s3://play2learn-bucket/static/vue-games/anagram-hunt/js/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "application/javascript" \
  --cache-control "no-cache, no-store, must-revalidate"

aws s3 sync ./dist/css/ s3://play2learn-bucket/static/vue-games/anagram-hunt/css/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "text/css" \
  --cache-control "no-cache, no-store, must-revalidate"

echo "Deployment complete!"
