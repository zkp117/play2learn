#!/bin/bash

set -e  # Exit on any error

# Clean dist folder before all builds
echo "Cleaning build directory..."
rm -rf dist/

# ------------------ Math Facts ------------------

echo "Building Math Facts game..."
VUE_APP_BASE_URL=/vue-games/math-facts/ npm run build

echo "Deploying Math Facts to S3..."
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/math-facts/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "no-cache, no-store, must-revalidate"

# Clean before next build
rm -rf dist/

# ------------------ Anagram Hunt ------------------

echo "Building Anagram Hunt game..."
VUE_APP_BASE_URL=/vue-games/anagram-hunt/ npm run build

echo "Deploying Anagram Hunt to S3..."
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/anagram-hunt/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "no-cache, no-store, must-revalidate"

echo "✅ Deployment complete!"
