# Build and deploy Anagram Hunt
VUE_APP_GAME=anagram-hunt VUE_APP_BASE_URL=/vue-games/anagram-hunt/ npm run build
aws s3 sync ./dist/anagram-hunt/ s3://play2learn-bucket/vue-games/anagram-hunt/ \
  --delete --acl public-read --exact-timestamps --cache-control "public, max-age=31536000, immutable"

# Build and deploy Math Facts
VUE_APP_GAME=math-facts VUE_APP_BASE_URL=/vue-games/math-facts/ npm run build
aws s3 sync ./dist/math-facts/ s3://play2learn-bucket/vue-games/math-facts/ \
  --delete --acl public-read --exact-timestamps --cache-control "public, max-age=31536000, immutable"
