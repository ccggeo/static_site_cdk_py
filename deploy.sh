if [ $# -ne 1 ]; then
   echo "No bucket provided";
   exit 1
fi
aws s3 cp  .  s3://$1 --exclude "*" --include "*.html" --include "*.css" --recursive
