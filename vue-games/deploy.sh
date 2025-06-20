#!/bin/bash

set -e  # Exit on any error

# Function to build and deploy a game
deploy_game() {
  GAME_NAME=$1
  BASE_URL="/vue-games/$GAME_NAME/"
  S3_PATH="s3://play2learn-bucket/vue-games/$GAME_NAME/"

  echo "🚀 Deploying $GAME_NAME..."

  echo "Cleaning build directory..."
  rm -rf dist/

  echo "Preparing index.html for $GAME_NAME..."
  sed "s|%BASE_URL%|$BASE_URL|" public/index-template.html > public/index.html

  echo "Building $GAME_NAME game..."
  VUE_APP_BASE_URL=$BASE_URL npm run build

  echo "Removing old index.html from S3 to avoid stale cache..."
  aws s3 rm "${S3_PATH}index.html" || true

  echo "Syncing assets for $GAME_NAME to S3..."
  aws s3 sync ./dist/ "$S3_PATH" \
    --exclude "index.html" \
    --delete \
    --acl public-read \
    --exact-timestamps \
    --cache-control "public, max-age=31536000"

  echo "Uploading fresh index.html with no-cache..."
  aws s3 cp ./dist/index.html "${S3_PATH}index.html" \
    --acl public-read \
    --cache-control "no-cache, no-store, must-revalidate"
}

# ------------------ Deploy Each Game ------------------

deploy_game "math-facts"
deploy_game "anagram-hunt"

echo "✅ All games deployed successfully!"
