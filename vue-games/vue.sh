#!/bin/bash
# index.html is excluded 
set -e

build_and_deploy() {
  GAME_NAME=$1
  echo "🚀 Building $GAME_NAME..."
  cd "$GAME_NAME"
  npm ci
  npm run build

  echo "📦 Deploying $GAME_NAME to S3"
  aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/$GAME_NAME/ \
    --exclude "index.html" \ 
    --delete \
    --acl public-read \
    --exact-timestamps \
    --cache-control "public, max-age=31536000"

  cd ..
}

build_and_deploy "math-facts"
build_and_deploy "anagram-hunt"

echo "✅ Deployment complete!"