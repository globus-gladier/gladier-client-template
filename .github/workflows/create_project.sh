#!/usr/bin/env bash

full_name=$1

echo $full_name

repo=$(echo $full_name | awk -F '/' '{print $2}')
author=$(echo $full_name | awk -F '/' '{print $1}')
owner=$(echo $full_name | awk -F '/' '{print $1}')
package=$(echo $full_name | awk -F '/' '{print $2}' | tr '-' '_' | tr '[:upper:]' '[:lower:]')

original_repo="gladier-client-template"


echo $repo
echo $original_repo

mv README.md HOW-TO.md
cp .github/README_STD.md README.md
sed -i "s/$original_repo/$repo/g" README.md

cp -r full_client $name
mv $name/full_client.py $name/$name.py
rm -rf .github
rm -rf CITATION.cff