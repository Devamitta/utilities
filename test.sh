cd "/home/deva/Documents/dps/scripts"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "making csv with bold and sorted by pāli alphabet"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python3 ods2csv-sort.py "../spreadsheets/dps.ods" PALI

mv "../spreadsheets/dps.ods-pali-s.csv" "../spreadsheets/dps-full.csv"

echo "process completed"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


cd "/home/deva/Documents/dps"


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
cd "inflection/"
python3.10 "inflection generator.py"

date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
cd "../exporter"
source /home/deva/.cache/pypoetry/virtualenvs/exporter-uJ6yRP2M-py3.10/bin/activate
poetry shell
python3.10 exporter.py run-generate-html-and-json-test
python3.10 exporter.py run-generate-goldendict-test



echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Пали-Русско-Пали Словарь создан"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "unzip and copy to GoldenDict"
cd "/home/deva/Documents/dps/scripts"
python3 "unzip-dps-test.py"