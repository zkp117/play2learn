#!/bin/bash

set -e  # Exit on any error

# Clean dist folder before all builds
echo "Cleaning build directory..."
rm -rf dist/

# ------------------ Math Facts ------------------

echo "Building Math Facts game..."
VUE_APP_BASE_URL=/vue-games/math-facts/ npm run build

echo "Deploying Math Facts to S3..."

# Upload everything *except* index.html with long cache lifetime
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/math-facts/ \
  --exclude "index.html" \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "public, max-age=31536000"

# Upload index.html with no-cache
aws s3 cp ./dist/index.html s3://play2learn-bucket/vue-games/math-facts/index.html \
  --acl public-read \
  --cache-control "no-cache, no-store, must-revalidate"

# Clean before next build
rm -rf dist/

# ------------------ Anagram Hunt ------------------

echo "Building Anagram Hunt game..."
VUE_APP_BASE_URL=/vue-games/anagram-hunt/ npm run build

echo "Deploying Anagram Hunt to S3..."

# Upload everything except index.html
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/anagram-hunt/ \
  --exclude "index.html" \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "public, max-age=31536000"

# Upload index.html separately with no-cache
aws s3 cp ./dist/index.html s3://play2learn-bucket/vue-games/anagram-hunt/index.html \
  --acl public-read \
  --cache-control "no-cache, no-store, must-revalidate"

echo "✅ Deployment complete!"
