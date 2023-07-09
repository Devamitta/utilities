exec &> ~/.mkall-errors.txt

cd "/home/deva/Documents/dps/scripts"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "making csv with bold and sorted by pāli alphabet"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python3 ods2csv-sort.py "../spreadsheets/dps.ods" PALI

mv "../spreadsheets/dps.ods-pali-s.csv" "../spreadsheets/dps-full.csv"

# python3 DPD-ex-insert.py

# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# echo "dps-dpd-ex.csv has been updated"
# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# date
# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


# cd "/home/deva/Documents/dps/scripts"
python3 "sbs-pd-filter.py"

echo "filter SBS words from DPS"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date


cd "../inflection"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
python3 "inflection generator.py"

cd "../inflection-en"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
python3 "inflection generator.py"

date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
cd "../exporter"
# source /home/deva/.cache/pypoetry/virtualenvs/exporter-uJ6yRP2M-py3.10/bin/activate
# poetry shell
python3 exporter.py run-generate-html-and-json
python3 exporter.py run-generate-goldendict
python3 exporter.py run-generate-html-and-json-sbs
python3 exporter.py run-generate-goldendict-sbs
# python3 exporter.py run-generate-html-and-json-dps-en
# python3 exporter.py run-generate-goldendict-dps-en



echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Ru-Pāli-Dict & SBS_PD generated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "unzip and copy to GoldenDict"
cd "../scripts"
python3 "unzip-dps.py"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Please open GoldenDict > press Alt+Z > F3 > Rescan now"

cd

txt ~/.mkall-errors.txt

