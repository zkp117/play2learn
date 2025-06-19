#!/bin/bash

set -e  # Exit if anything fails

# Install dependencies if needed
echo "Installing npm dependencies..."
npm install

# Common S3 sync options
CACHE_CONTROL="--cache-control no-cache,no-store,must-revalidate"
ACL="--acl public-read"
EXACT="--exact-timestamps"
DELETE="--delete"

# ----------- Math Facts -----------
echo "Building Math Facts game..."
VUE_APP_GAME=math-facts npm run build

echo "Deploying Math Facts to S3..."
aws s3 sync dist/ s3://play2learn-bucket/vue-games/math-facts/ \
  $DELETE $ACL $EXACT $CACHE_CONTROL

# ----------- Anagram Hunt -----------
echo "Building Anagram Hunt game..."
VUE_APP_GAME=anagram-hunt npm run build

echo "Deploying Anagram Hunt to S3..."
aws s3 sync dist/ s3://play2learn-bucket/vue-games/anagram-hunt/ \
  $DELETE $ACL $EXACT $CACHE_CONTROL

echo "✅ Deployment complete!"