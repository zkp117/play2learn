#!/bin/bash

# builds MathFacts game
echo "Building Math Facts game..."
VUE_APP_GAME=math-facts npm run build
echo "Math Facts build completed."

# loads js files for MathFacts aws
echo "Syncing Math Facts JavaScript files to S3..."
aws s3 sync ./dist/js/ s3://play2learn-bucket/vue-games/math-facts/js/ --delete --acl public-read --exact-timestamps --content-type "application/javascript"
echo "Math Facts JavaScript sync completed."

# loads css files for MathFacts aws
echo "Syncing Math Facts CSS files to S3..."
aws s3 sync ./dist/css/ s3://play2learn-bucket/vue-games/math-facts/css/ --delete --acl public-read --exact-timestamps --content-type "text/css"
echo "Math Facts CSS sync completed."

# builds AnagramHunt game
echo "Building Anagram Hunt game..."
VUE_APP_GAME=anagram-hunt npm run build
echo "Anagram Hunt build completed."

# loads js files for AnagramHunt aws
echo "Syncing Anagram Hunt JavaScript files to S3..."
aws s3 sync ./dist/js/ s3://play2learn-bucket/vue-games/anagram-hunt/js/ --delete --acl public-read --exact-timestamps --content-type "application/javascript"
echo "Anagram Hunt JavaScript sync completed."

# loads css files for AnagramHunt aws
echo "Syncing Anagram Hunt CSS files to S3..."
aws s3 sync ./dist/css/ s3://play2learn-bucket/vue-games/anagram-hunt/css/ --delete --acl public-read --exact-timestamps --content-type "text/css"
echo "Anagram Hunt CSS sync completed."

# shows that everything went through
echo "✅ Deployment complete!"
