#!/bin/bash
set -e

cd "$(dirname "$0")"

build_and_deploy() {
  GAME_NAME=$1
  echo "🚀 Building $GAME_NAME..."
  cd "$GAME_NAME"
  npm ci
  npm run build

  echo "📦 Deploying $GAME_NAME to S3..."
  aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/$GAME_NAME/ \
    --delete \
    --acl public-read \
    --exact-timestamps \
    --cache-control "public, max-age=31536000"

  aws s3 cp ./dist/index.html s3://play2learn-bucket/vue-games/$GAME_NAME/index.html \
    --acl public-read \
    --cache-control "no-cache, no-store, must-revalidate"

  cd ..
}

build_and_deploy "math-facts"
build_and_deploy "anagram-hunt"

echo "✅ Deployment complete!"
