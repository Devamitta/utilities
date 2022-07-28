# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# echo "making csv with bold"
# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# mv "../spreadsheets/dps.ods" "dps.ods"

# python3 ods-to-csv-headers.py "dps.ods" PALI 39

# mv "dps.ods" "../spreadsheets/dps.ods"

# mv "dps.csv" "../spreadsheets/dps-full.csv"

# echo "process completed"
# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


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