#!/bin/bash

SOURCE_FOLDER=$1
DESTINATION_FOLDER=$2

for SOURCE_FILE in $SOURCE_FOLDER/*.hocr
do
    FILENAME=$(basename $SOURCE_FILE .hocr)
    DESTINATION_FILE=$DESTINATION_FOLDER/$FILENAME.xml
    echo $SOURCE_FILE
    python3 tesseract.py -i $SOURCE_FILE -o $DESTINATION_FILE
done
