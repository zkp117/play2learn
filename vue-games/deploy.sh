# this file I run when I update either of the vue games (actual .vue files only)
# it's setup this way so if I update them it deletes the old files and replaces it with the new one
# instructions: 
    # run "npm run build && ./deploy.sh"
    # npm command builds games and './deploy.sh' sends the current build to aws

# builds MathFacts game
echo "Building Math Facts game..."
VUE_APP_GAME=math-facts npm run build
echo "Math Facts build completed."

# loads js files for MathFacts aws
echo "Syncing Math Facts JavaScript files to S3..."
aws s3 sync ./dist/js/ s3://play2learn-bucket/vue-games/math-facts/js/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "application/javascript" \
  --cache-control "no-cache, no-store, must-revalidate"
echo "Math Facts JavaScript sync completed."

# loads css files for MathFacts aws
echo "Syncing Math Facts CSS files to S3..."
aws s3 sync ./dist/css/ s3://play2learn-bucket/vue-games/math-facts/css/ \
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

# loads js files for AnagramHunt aws
echo "Syncing Anagram Hunt JavaScript files to S3..."
aws s3 sync ./dist/js/ s3://play2learn-bucket/vue-games/anagram-hunt/js/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "application/javascript" \
  --cache-control "no-cache, no-store, must-revalidate"
echo "Anagram Hunt JavaScript sync completed."

# loads css files for AnagramHunt aws
echo "Syncing Anagram Hunt CSS files to S3..."
aws s3 sync ./dist/css/ s3://play2learn-bucket/vue-games/anagram-hunt/css/ \
  --delete \
  --acl public-read \
  --exact-timestamps \
  --content-type "text/css" \
  --cache-control "no-cache, no-store, must-revalidate"
echo "Anagram Hunt CSS sync completed."

echo "Uploading HTML entry points for Math Facts..."
aws s3 cp ./dist/index.html s3://play2learn-bucket/vue-games/math-facts/templates/index.html \
  --acl public-read \
  --content-type "text/html" \
  --cache-control "no-cache, no-store, must-revalidate"

echo "Uploading HTML entry points for Anagram Hunt..."
aws s3 cp ./dist/index.html s3://play2learn-bucket/vue-games/anagram-hunt/templates/index.html \
  --acl public-read \
  --content-type "text/html" \
  --cache-control "no-cache, no-store, must-revalidate"
