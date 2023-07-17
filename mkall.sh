#!/usr/bin/env bash

exec &> '/home/deva/.mkall-errors.txt'

cd "/home/deva/Documents/dps/scripts"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "making csv with bold and sorted by pāli alphabet"


poetry run python ods2csv-sort.py "../spreadsheets/dps.ods" PALI

mv "../spreadsheets/dps.ods-pali-s.csv" "../spreadsheets/dps-full.csv"

# poetry run python DPD-ex-insert.py

# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# echo "dps-dpd-ex.csv has been updated"
# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
# date
# echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


# cd "/home/deva/Documents/dps/scripts"
poetry run python "sbs-pd-filter.py"

echo "filter SBS words from DPS"



cd "../inflection"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
poetry run python "inflection generator.py"

cd "../inflection-en"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
poetry run python "inflection generator.py"


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
cd "../exporter"
poetry run python exporter.py run-generate-html-and-json
poetry run python exporter.py run-generate-goldendict
poetry run python exporter.py run-generate-html-and-json-sbs
poetry run python exporter.py run-generate-goldendict-sbs
# poetry run python exporter.py run-generate-html-and-json-dps-en
# poetry run python exporter.py run-generate-goldendict-dps-en


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "Ru-Pāli-Dict & SBS_PD generated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "unzip and copy to GoldenDict"
cd "../scripts"
poetry run python "unzip-dps.py"


