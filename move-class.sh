#!/usr/bin/env bash

# move all class materials on the server and GitHub

cd "/home/deva/Documents/dps/utilities"

# bash push-sbs-pd.sh

# bash push-ru.sh

cd "/home/deva/Downloads"

cp -f "Vocab Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Vocab Pāli Class.apkg"

mv -f "Vocab Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Vocab Pāli Class.apkg"

cp -f "Grammar Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Grammar Pāli Class.apkg"

mv -f "Grammar Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Grammar Pāli Class.apkg"

cp -f "Roots Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Roots Pāli Class.apkg"

mv -f "Roots Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Roots Pāli Class.apkg"

cp -f "Phonetic Changes Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Phonetic Changes Pāli Class.apkg"

mv -f "Phonetic Changes Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Phonetic Changes Pāli Class.apkg"

cp -f "Common Roots Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Common Roots Pāli Class.apkg"

mv -f "Common Roots Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Common Roots Pāli Class.apkg"

cp -f "Suttas Advanced Pāli Class.apkg" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/Suttas Advanced Pāli Class.apkg"

mv -f "Suttas Advanced Pāli Class.apkg" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/Suttas Advanced Pāli Class.apkg"



echo "all apkg - done"

# cp -rf "/home/deva/Documents/dps/word-frequency/vocab" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/"

# cp -rf "/home/deva/Documents/dps/word-frequency/vocab" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/"

# echo "all vocab.xlsx - done"

cp -rf "/home/deva/Documents/dps/csv-for-anki/classes" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/"

cp -rf "/home/deva/Documents/dps/csv-for-anki/grammar" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/"

cp -f "/home/deva/Documents/dps/csv-for-anki/abbr.xlsx" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/Anki Decks/abbreviations.xlsx"

echo "all csv for anki - done"

# cp -f "/home/deva/Documents/dps/test.md" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/class-test.md"

# echo "making wordtree"

# cd "/home/deva/Documents/dps/word-frequency/"

# bash wordtree-for-all-class.sh

# echo "wordtree cleaning"

# cd "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/wordtree"

# find . -wholename './class1/*' | xargs rm -rf
# find . -wholename './class2/*' | xargs rm -rf
# find . -wholename './class3/*' | xargs rm -rf
# find . -wholename './class4/*' | xargs rm -rf
# find . -wholename './class5/*' | xargs rm -rf
# find . -wholename './class6/*' | xargs rm -rf
# find . -wholename './class7/*' | xargs rm -rf
# find . -wholename './class8/*' | xargs rm -rf
# find . -wholename './class9/*' | xargs rm -rf
# find . -wholename './class10/*' | xargs rm -rf
# find . -wholename './class11/*' | xargs rm -rf
# find . -wholename './class12/*' | xargs rm -rf
# find . -wholename './class13/*' | xargs rm -rf
# find . -wholename './class14/*' | xargs rm -rf

# cd "/home/deva/Documents/sasanarakkha/study-tools/pali-class/wordtree"

# find . -wholename './class1/*' | xargs rm -rf
# find . -wholename './class2/*' | xargs rm -rf
# find . -wholename './class3/*' | xargs rm -rf
# find . -wholename './class4/*' | xargs rm -rf
# find . -wholename './class5/*' | xargs rm -rf
# find . -wholename './class6/*' | xargs rm -rf
# find . -wholename './class7/*' | xargs rm -rf
# find . -wholename './class8/*' | xargs rm -rf
# find . -wholename './class9/*' | xargs rm -rf
# find . -wholename './class10/*' | xargs rm -rf
# find . -wholename './class11/*' | xargs rm -rf
# find . -wholename './class12/*' | xargs rm -rf
# find . -wholename './class13/*' | xargs rm -rf
# find . -wholename './class14/*' | xargs rm -rf


# cp -rf "/home/deva/Documents/dps/word-frequency/pics-wordtree/wordtree" "/home/deva/filesrv1/share1/Sharing between users/13 For Pāli class/"

# cp -rf "/home/deva/Documents/dps/word-frequency/pics-wordtree/wordtree" "/home/deva/Documents/sasanarakkha/study-tools/pali-class/"


# echo "all pics-wordtree - done"

echo "all done - new class updated"


