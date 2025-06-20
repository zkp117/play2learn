#!/bin/bash
set -e

echo "Cleaning build directory..."
rm -rf dist/

# Build once with shared base path
echo "Building games with shared base path..."
VUE_APP_BASE_URL=/vue-games/ npm run build

# Deploy to Math Facts subfolder
echo "Deploying Math Facts to S3..."
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/math-facts/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "public, max-age=31536000"

aws s3 cp ./dist/index.html s3://play2learn-bucket/vue-games/math-facts/index.html \
  --acl public-read \
  --cache-control "no-cache, no-store, must-revalidate"

# Deploy to Anagram Hunt subfolder
echo "Deploying Anagram Hunt to S3..."
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/anagram-hunt/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "public, max-age=31536000"

aws s3 cp ./dist/index.html s3://play2learn-bucket/vue-games/anagram-hunt/index.html \
  --acl public-read \
  --cache-control "no-cache, no-store, must-revalidate"

echo "✅ Deployment complete!"