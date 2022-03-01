#!/usr/bin/env bash

full_name=$1

echo $full_name

repo=$(echo $full_name | awk -F '/' '{print $2}')
author=$(echo $full_name | awk -F '/' '{print $1}')
owner=$(echo $full_name | awk -F '/' '{print $1}')
package=$(echo $full_name | awk -F '/' '{print $2}' | tr '-' '_' | tr '[:upper:]' '[:lower:]')

original_repo="gladier-client-template"
original_author="The Gladier Team"
original_owner="globus-gladier"
original_package="gladier_client" 

echo $repo
echo $original_repo
echo $owner
echo $original_owner
echo $package
echo $original_package
echo $author
echo $original_author

for filename in $(git ls-files) 
do
    sed -i "s/$original_repo/$repo/g" $filename
    sed -i "s/$original_author/$author/g" $filename
    sed -i "s/$original_owner/$owner/g" $filename
    sed -i "s/$original_package/$package/g" $filename
    echo "Renamed $filename"
done

sed -i "3,14d" README.md

mv gladier_client $name

rm -rf .github/workflows
rm -rf CHANGELOG.md

