exec &> ~/mkall-errors.txt

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

node --max-old-space-size=8192 /home/deva/Documents/dps/scripts/dpdods2csv.js ods2csv "/home/deva/Documents/dps/spreadsheets/dps.ods" PALI 39 dps
echo "dps-full.csv updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd "/home/deva/Documents/dps/spreadsheets"
rm -R '/home/deva/Documents/dps/spreadsheets/dps-vocab.csv'
rm -R '/home/deva/Documents/dps/spreadsheets/dps-root.csv'

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date


cd "/home/deva/Documents/dps/scripts"
python3 "sbs-pd-filter.py"

echo "filter SBS words from DPS"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date


cd "/home/deva/Documents/dps"


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
cd "inflection/"
python3.10 "inflection generator.py"

date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
cd "../exporter"
source /home/deva/.cache/pypoetry/virtualenvs/exporter-uJ6yRP2M-py3.10/bin/activate
poetry shell
python3.10 exporter.py run-generate-html-and-json
python3.10 exporter.py run-generate-goldendict
python3.10 exporter.py run-generate-html-and-json-sbs
python3.10 exporter.py run-generate-goldendict-sbs



echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Пали-Русско-Пали Словарь создан"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "unzip and copy to GoldenDict"
cd "/home/deva/Documents/dps/scripts"
python3 "unzip-dps.py"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Please open GoldenDict > press Alt+Z > F3 > Rescan now"

xed ~/mkall-errors.txt

