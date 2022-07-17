echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date

node --max-old-space-size=8192 /home/deva/Documents/dps/scripts/dpdods2csv.js ods2csv "/home/deva/Documents/dps/spreadsheets/dps.ods" PALI 39 dps

cd "/home/deva/Documents/dps/spreadsheets"
rm -R '/home/deva/Documents/dps/spreadsheets/dps-vocab.csv'
rm -R '/home/deva/Documents/dps/spreadsheets/dps-root.csv'

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "dps-full.csv updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd "/home/deva/Documents/dps"


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
cd "inflection/"
python3.10 "test if inflection exists in sutta.py"
