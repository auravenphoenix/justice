#!/bin/bash

files=`find -name "*.txt"`
files="$files `find -name "*.mkv"`"

for file in $files
do
    echo $file
    git add $file
    git commit -m "Add $file."
    git push
done
