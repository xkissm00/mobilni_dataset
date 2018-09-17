SOURCE_FOLDER="ABBYY_HTML"
DESTINATION_FOLDER="ABBYY_OUT"

for SOURCE_FILE in $SOURCE_FOLDER/*.htm
do
    FILENAME=$(basename $SOURCE_FILE .htm)
    DESTINATION_FILE=$DESTINATION_FOLDER/$FILENAME.xml
    echo $SOURCE_FILE
    python3 abbyy.py -i $SOURCE_FILE -o $DESTINATION_FILE
done
