#!/bin/bash

set -e  # Exit on any error

echo "Cleaning build directory..."
rm -rf dist/

# ------------------ Math Facts ------------------

echo "Preparing index.html for Math Facts..."
sed "s|%BASE_URL%|/vue-games/math-facts/|" public/index-template.html > public/index.html

echo "Building Math Facts game..."
VUE_APP_BASE_URL=/vue-games/math-facts/ npm run build

echo "Deploying Math Facts to S3..."

aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/math-facts/ \
  --exclude "index.html" \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "public, max-age=31536000"

aws s3 cp ./dist/index.html s3://play2learn-bucket/vue-games/math-facts/index.html \
  --acl public-read \
  --cache-control "no-cache, no-store, must-revalidate"

rm -rf dist/

# ------------------ Anagram Hunt ------------------

echo "Preparing index.html for Anagram Hunt..."
sed "s|%BASE_URL%|/vue-games/anagram-hunt/|" public/index-template.html > public/index.html

echo "Building Anagram Hunt game..."
VUE_APP_BASE_URL=/vue-games/anagram-hunt/ npm run build

echo "Deploying Anagram Hunt to S3..."

aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/anagram-hunt/ \
  --exclude "index.html" \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "public, max-age=31536000"

aws s3 cp ./dist/index.html s3://play2learn-bucket/vue-games/anagram-hunt/index.html \
  --acl public-read \
  --cache-control "no-cache, no-store, must-revalidate"

echo "✅ Deployment complete!"
