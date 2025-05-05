#!/bin/bash

# Build Math Facts game
echo "Building Math Facts game..."
VUE_APP_GAME=math-facts npm run build
echo "Math Facts build completed."

# Sync JavaScript files for Math Facts
echo "Syncing Math Facts JavaScript files to S3..."
aws s3 sync ./dist/js/ s3://play2learn-bucket/vue-games/math-facts/js/ --delete --acl public-read --exact-timestamps --content-type "application/javascript"
echo "Math Facts JavaScript sync completed."

# Sync CSS files for Math Facts
echo "Syncing Math Facts CSS files to S3..."
aws s3 sync ./dist/css/ s3://play2learn-bucket/vue-games/math-facts/css/ --delete --acl public-read --exact-timestamps --content-type "text/css"
echo "Math Facts CSS sync completed."

# Build Anagram Hunt game
echo "Building Anagram Hunt game..."
VUE_APP_GAME=anagram-hunt npm run build
echo "Anagram Hunt build completed."

# Sync JavaScript files for Anagram Hunt
echo "Syncing Anagram Hunt JavaScript files to S3..."
aws s3 sync ./dist/js/ s3://play2learn-bucket/vue-games/anagram-hunt/js/ --delete --acl public-read --exact-timestamps --content-type "application/javascript"
echo "Anagram Hunt JavaScript sync completed."

# Sync CSS files for Anagram Hunt
echo "Syncing Anagram Hunt CSS files to S3..."
aws s3 sync ./dist/css/ s3://play2learn-bucket/vue-games/anagram-hunt/css/ --delete --acl public-read --exact-timestamps --content-type "text/css"
echo "Anagram Hunt CSS sync completed."

echo "✅ Deployment complete!"
