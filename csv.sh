
cd "/home/deva/Documents/dps/word-frequency"

while true; do
    read -p "grammar-csv for anki need update?" yn
    case $yn in
        [Yy]* ) poetry run python grammar-csv.py; 
        break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "grammar csv up to date"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd "/home/deva/Documents/dps/scripts"

while true; do
    read -p "dps need update?" yn
    case $yn in
        [Yy]* ) poetry run python ods2csv.py "../spreadsheets/dps.ods" PALI; 
        
        break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "dps up-to-date"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

while true; do
    read -p "nidh need update?" yn
    case $yn in
        [Yy]* ) poetry run python xls2csv.py "../spreadsheets/nidh_bold.xlsx"; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

echo "nidh up-to-date"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

while true; do
    read -p "friquent-words need update?" yn
    case $yn in
        [Yy]* ) poetry run python ods2csv.py "../pāli-course/frequent-words.ods" words; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

echo "frequent-words completed"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"




cd "/home/deva/Documents/dps/word-frequency"

poetry run python pos-maker.py

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "summary-for-class.csv generated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# cd "/home/deva/Documents/dps/word-frequency/frequent-words-dps"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "classes updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


libreoffice "frequent-words-dps/summary-for-class.csv"


while true; do
    read -p "DPS updated?" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        *  ) echo "only yes or no";;
    esac
done

cd "/home/deva/Downloads"

mv -f "dps.ods" "/home/deva/Documents/dps/spreadsheets/dps.ods"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date

cd "/home/deva/Documents/dps/scripts"

poetry run python ods2csv-sort.py "../spreadsheets/dps.ods" PALI

mv "../spreadsheets/dps.ods-pali-s.csv" "../spreadsheets/dps-full.csv"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Done"
date

cd "/home/deva/Documents/dps/word-frequency"
poetry run python class-feedback.py