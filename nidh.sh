cd "/home/deva/Downloads"

mv -f "dpd.ods" "/home/deva/Documents/dpd-br/dpd.ods"

cd "/home/deva/Documents/dpd-br"

python3.10 "utilities/ods2csv.py"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "dpd-pali.csv updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd "/home/deva/Documents/dps/scripts"

python3 "nidhi_bold.py"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "nidh_bold.csv updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd "/home/deva/Documents/dps/spreadsheets"

libreoffice nidh_bold.csv
