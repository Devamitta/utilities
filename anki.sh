cd "/home/deva/Downloads"

mv -f "dps.ods" "/home/deva/Documents/dps/spreadsheets/dps.ods"
mv -f "grammar.xlsx" "/home/deva/Documents/dps/pāli-course/grammar.xlsx"

cd "/home/deva/Documents/dps/spreadsheets"

libreoffice dps.ods 2>/dev/null

cd "/home/deva/Documents/dps/pāli-course"

libreoffice grammar.xlsx 2>/dev/null

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
echo "making csv with bold and sorted by pāli alphabet"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python3 ods2csv-sort.py "../spreadsheets/dps.ods" PALI

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

duplicates=$(sort -t ',' -k 1 "../spreadsheets/dps.ods-pali-s.csv" | uniq -d)
if [ -n "$duplicates" ]; then
    echo -e "\e[31mDuplicates found:\e[0m"
    echo -e "\e[31m$duplicates\e[0m"
    exit 1
else
    echo "No duplicates found."
fi

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

mv "../spreadsheets/dps.ods-pali-s.csv" "../spreadsheets/dps-full.csv"

# cp "../spreadsheets/dps-full.csv" "/home/deva/Documents/dpd-br/dpd-db/csvs/dps.csv"



python3 random-test.py

echo "DPS for Anki has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


# cp "/home/deva/Documents/dpd-br/dpd-db/backups/PaliWord.tsv" "/home/deva/Documents/dpd-br/csvs/dpd-full.csv"

python3 DPD-ex-insert.py


echo "dps-dpd-ex.csv has been updated"
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


python3 grammar-csv.py


echo "grammar.csv for class Anki has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"







