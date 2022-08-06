echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "making csv with bold"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

while true; do
    read -p "golden dict need update?" yn
    case $yn in
        [Yy]* ) bash test.sh;
        python3 ods2csv.py "../spreadsheets/dps.ods" PALI; 
        
        break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done



echo "dps up-to-date"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

while true; do
    read -p "nidh need update?" yn
    case $yn in
        [Yy]* ) python3 xls2csv.py "../spreadsheets/nidh_bold.xlsx"; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

echo "nidh up-to-date"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

while true; do
    read -p "friquent-words need update?" yn
    case $yn in
        [Yy]* ) python3 ods2csv.py "../word-frequency/pāli-course/frequent-words.ods" words; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

echo "frequent-words completed"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"




cd "/home/deva/Documents/dps/word-frequency"

python3 pos-maker.py

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

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date

cd "/home/deva/Documents/dps/scripts"

python3 ods2csv-sort.py "../spreadsheets/dps.ods" PALI

mv "../spreadsheets/dps.ods-pali-s.csv" "../spreadsheets/dps-full.csv"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Done"
date

cd "/home/deva/Documents/dps/word-frequency"
python3 class-feedback.py