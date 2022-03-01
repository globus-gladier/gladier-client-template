#!/usr/bin/env bash

repo_name=$1

name=$(echo $repo_name | awk -F '/' '{print $2}' | tr '-' '_' | tr '[:upper:]' '[:lower:]')
author=$(echo $repo_name | awk -F '/' '{print $1}')
urlname=$(echo $repo_name)

original_author="The Gladier Team"
original_name="gladier_client" 
original_urlname="globus-gladier/gladier-client-template"

echo $original_name
echo $name

echo $original_author
echo $author

echo $original_urlname
echo $urlname

for filename in $(git ls-files) 
do
    sed -i "s/$original_author/$author/g" $filename
    sed -i "s/$original_name/$name/g" $filename
    sed -i "s/$original_urlname/$urlname/g" $filename
    echo "Renamed $filename"
done

mv gladier_client $name

rm -rf .github/workflows
rm -rf CHANGELOG.md

