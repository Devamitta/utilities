cd "/home/deva/Downloads"

mv -f "dps.ods" "/home/deva/Documents/dps/spreadsheets/dps.ods"
mv -f "grammar.xlsx" "/home/deva/Documents/dps/pāli-course/grammar.xlsx"

# cd "/home/deva/Documents/dps/spreadsheets"

# while true; do
#     read -p "need to open dps.ods?" yn
#     case $yn in
#         [Yy]* ) libreoffice dps.ods 2>/dev/null; break;;
#         [Nn]* ) break;;
#         *  ) echo "only yes or no";;
#     esac
# done

# cd "/home/deva/Documents/dps/pāli-course"

# while true; do
#     read -p "need to open grammar.xlsx?" yn
#     case $yn in
#         [Yy]* ) libreoffice grammar.xlsx 2>/dev/null; break;;
#         [Nn]* ) break;;
#         *  ) echo "only yes or no";;
#     esac
# done

# while true; do
#     read -p "DPS & grammar updated?" yn
#     case $yn in
#         [Yy]* ) break;;
#         [Nn]* ) exit;;
#         *  ) echo "only yes or no";;
#     esac
# done

cd "/home/deva/Documents/dps/scripts"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "making csv with bold and sorted by pāli alphabet"

while true; do
    read -p "need make upadted dps-full?" yn
    case $yn in
        [Yy]* ) python3 ods2csv-sort.py "../spreadsheets/dps.ods" PALI; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done


# python3 ods2csv-sort.py "../spreadsheets/dps.ods" PALI


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

cp "../spreadsheets/dps-full.csv" "/home/deva/Documents/dpd-db/dps/dps.tsv"

while true; do
    read -p "need make upadted dpd?" yn
    case $yn in
        [Yy]* ) bash nidh.sh; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done

python3 DPD-ex-insert.py

echo "dps-dpd-ex.csv has been updated"

while true; do
    read -p "need csvs for anki?" yn
    case $yn in
        [Yy]* ) bash anki.sh; break;;
        [Nn]* ) break;;
        *  ) echo "only yes or no";;
    esac
done






