#!/bin/bash
set -e

echo "Cleaning build directory..."
rm -rf dist/

# Build Math Facts
echo "Building Math Facts game..."
VUE_APP_BASE_URL=/vue-games/math-facts/ npm run build

echo "Deploying Math Facts to S3..."
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/math-facts/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "public, max-age=31536000"

aws s3 cp ./dist/index.html s3://play2learn-bucket/vue-games/math-facts/index.html \
  --acl public-read \
  --cache-control "no-cache, no-store, must-revalidate"

rm -rf dist/

# Build Anagram Hunt
echo "Building Anagram Hunt game..."
VUE_APP_BASE_URL=/vue-games/anagram-hunt/ npm run build

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
