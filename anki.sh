cd "/home/deva/Documents/dps/scripts"

poetry run python random-test.py

echo "DPS for Anki has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

poetry run python roots-class-feedback.py


echo "csv for Root Class has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


poetry run python phonetic-class-feedback.py


echo "csv for phonetic Class has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


cd "/home/deva/Documents/dps/word-frequency"

poetry run python class-feedback.py


echo "Vocab for class Anki has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


while true; do
    read -p "need make upadted grammar.csv?" yn
    case $yn in
        [Yy]* ) poetry run python grammar-csv.py; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

echo "done"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"