# Build Anagram Hunt with correct base URL
VUE_APP_BASE_URL=/vue-games/anagram-hunt/ npm run build

# Deploy Anagram Hunt build to its folder on S3
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/anagram-hunt/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "public, max-age=31536000, immutable"

# Build Math Facts with correct base URL
VUE_APP_BASE_URL=/vue-games/math-facts/ npm run build

# Deploy Math Facts build to its folder on S3
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/math-facts/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "public, max-age=31536000, immutable"
