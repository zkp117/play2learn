#!/bin/bash

# Build Math Facts game
echo "Building Math Facts game..."
VUE_APP_GAME=math-facts npm run build
echo "Math Facts build completed."

# Sync Math Facts to S3 with content-type explicitly set for JS
echo "Syncing Math Facts JavaScript files to S3..."
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/math-facts/ --delete --acl public-read --exact-timestamps --content-type "application/javascript" --exclude "*.css"
echo "Math Facts JavaScript sync completed."

# Sync CSS files separately for Math Facts with correct content-type
echo "Syncing Math Facts CSS files to S3..."
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/math-facts/ --delete --acl public-read --exact-timestamps --content-type "text/css" --include "*.css"
echo "Math Facts CSS sync completed."

# Build Anagram Hunt game
echo "Building Anagram Hunt game..."
VUE_APP_GAME=anagram-hunt npm run build
echo "Anagram Hunt build completed."

# Sync Anagram Hunt to S3 with content-type explicitly set for JS
echo "Syncing Anagram Hunt JavaScript files to S3..."
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/anagram-hunt/ --delete --acl public-read --exact-timestamps --content-type "application/javascript" --exclude "*.css"
echo "Anagram Hunt JavaScript sync completed."

# Sync CSS files separately for Anagram Hunt with correct content-type
echo "Syncing Anagram Hunt CSS files to S3..."
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/anagram-hunt/ --delete --acl public-read --exact-timestamps --content-type "text/css" --include "*.css"
echo "Anagram Hunt CSS sync completed."

echo "✅ Deployment complete!"
