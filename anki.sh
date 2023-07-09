cd "/home/deva/Documents/dps/scripts"

python3 random-test.py

echo "DPS for Anki has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python3 roots-class-feedback.py


echo "csv for Root Class has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


python3 phonetic-class-feedback.py


echo "csv for phonetic Class has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


cd "/home/deva/Documents/dps/word-frequency"

python3 class-feedback.py


echo "Vocab for class Anki has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


while true; do
    read -p "need make upadted grammar.csv?" yn
    case $yn in
        [Yy]* ) python3 grammar-csv.py; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

echo "done"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"