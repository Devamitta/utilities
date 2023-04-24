cd "/home/deva/Downloads"

mv -f "dps.ods" "/home/deva/Documents/dps/spreadsheets/dps.ods"
mv -f "grammar.xlsx" "/home/deva/Documents/dps/word-frequency/pāli-course/grammar.xlsx"

cd "/home/deva/Documents/dps/spreadsheets"

libreoffice dps.ods

cd "/home/deva/Documents/dps/word-frequency/pāli-course"

libreoffice grammar.xlsx

while true; do
    read -p "DPS & grammar updated?" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        *  ) echo "only yes or no";;
    esac
done

cd "/home/deva/Documents/dps/scripts"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "making csv with bold and sorted by pāli alphabet"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python3 ods2csv-sort.py "../spreadsheets/dps.ods" PALI

mv "../spreadsheets/dps.ods-pali-s.csv" "../spreadsheets/dps-full.csv"

python3 random-test.py

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "DPS for Anki has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cp "/home/deva/Documents/dpd-br/dpd-db/backups/PaliWord.tsv" "/home/deva/Documents/dpd-br/csvs/dpd-full.csv"


python3 DPD-ex-insert.py

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "dps-dpd-ex.csv has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


python3 roots-class-feedback.py

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "csv for Root Class has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python3 phonetic-class-feedback.py

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "csv for phonetic Class has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd "/home/deva/Documents/dps/word-frequency"

python3 class-feedback.py

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Vocab for class Anki has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python3 grammar-csv.py

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "grammar.csv for class Anki has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date



echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "  >>> see dps-csv-for-anki  <<<"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


