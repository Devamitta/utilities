#!/usr/bin/env bash

echo "making wordtree"

cd "/home/deva/Documents/dps/word-frequency/"

uv run bash wordtree-for-all-class.sh

echo "wordtree cleaning"

cd "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/wordtree"

find . -wholename './class1/*' | xargs rm -rf
find . -wholename './class2/*' | xargs rm -rf
find . -wholename './class3/*' | xargs rm -rf
find . -wholename './class4/*' | xargs rm -rf
find . -wholename './class5/*' | xargs rm -rf
find . -wholename './class6/*' | xargs rm -rf
find . -wholename './class7/*' | xargs rm -rf
find . -wholename './class8/*' | xargs rm -rf
find . -wholename './class9/*' | xargs rm -rf
find . -wholename './class10/*' | xargs rm -rf
find . -wholename './class11/*' | xargs rm -rf
find . -wholename './class12/*' | xargs rm -rf
find . -wholename './class13/*' | xargs rm -rf
find . -wholename './class14/*' | xargs rm -rf

cd "/home/deva/Documents/sasanarakkha/study-tools/pali-class/wordtree"

find . -wholename './class1/*' | xargs rm -rf
find . -wholename './class2/*' | xargs rm -rf
find . -wholename './class3/*' | xargs rm -rf
find . -wholename './class4/*' | xargs rm -rf
find . -wholename './class5/*' | xargs rm -rf
find . -wholename './class6/*' | xargs rm -rf
find . -wholename './class7/*' | xargs rm -rf
find . -wholename './class8/*' | xargs rm -rf
find . -wholename './class9/*' | xargs rm -rf
find . -wholename './class10/*' | xargs rm -rf
find . -wholename './class11/*' | xargs rm -rf
find . -wholename './class12/*' | xargs rm -rf
find . -wholename './class13/*' | xargs rm -rf
find . -wholename './class14/*' | xargs rm -rf


cp -rf "/home/deva/Documents/dps/word-frequency/pics-wordtree/wordtree" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/"

cp -rf "/home/deva/Documents/dps/word-frequency/pics-wordtree/wordtree" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/"


echo "all pics-wordtree - done"



