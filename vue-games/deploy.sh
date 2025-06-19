npm run build
aws s3 sync ./dist/ s3://play2learn-bucket/vue-games/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --cache-control "public, max-age=31536000, immutable"
