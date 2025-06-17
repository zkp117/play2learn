# builds MathFacts game
echo "Building Math Facts game..."
VUE_APP_GAME=math-facts npm run build
echo "Math Facts build completed."

# uploads MathFacts JavaScript files
echo "Syncing Math Facts JavaScript files to S3..."
aws s3 sync ./dist/js/ s3://play2learn-bucket/static/vue-games/math-facts/js/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "application/javascript" \
  --cache-control "no-cache, no-store, must-revalidate"
echo "Math Facts JavaScript sync completed."

# uploads MathFacts CSS files
echo "Syncing Math Facts CSS files to S3..."
aws s3 sync ./dist/css/ s3://play2learn-bucket/static/vue-games/math-facts/css/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "text/css" \
  --cache-control "no-cache, no-store, must-revalidate"
echo "Math Facts CSS sync completed."

# builds AnagramHunt game
echo "Building Anagram Hunt game..."
VUE_APP_GAME=anagram-hunt npm run build
echo "Anagram Hunt build completed."

# uploads AnagramHunt JavaScript files
echo "Syncing Anagram Hunt JavaScript files to S3..."
aws s3 sync ./dist/js/ s3://play2learn-bucket/static/vue-games/anagram-hunt/js/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "application/javascript" \
  --cache-control "no-cache, no-store, must-revalidate"
echo "Anagram Hunt JavaScript sync completed."

# uploads AnagramHunt CSS files
echo "Syncing Anagram Hunt CSS files to S3..."
aws s3 sync ./dist/css/ s3://play2learn-bucket/static/vue-games/anagram-hunt/css/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "text/css" \
  --cache-control "no-cache, no-store, must-revalidate"
echo "Anagram Hunt CSS sync completed."