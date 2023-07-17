
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Please update Pātimokkha Word by Word.ods" 
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


cd "/home/deva/Documents/dps/patimokkha_dict"

while true; do
    read -p "Pātimokkha ODS is up-to-date?" yn
    case $yn in
        [Yy]* ) bash makecsv.sh; break;;
        [Nn]* ) exit;;
        *  ) echo "only yes or no";;
    esac
done

echo "Pātimokkha generated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


cd "/home/deva/Documents/dps/scripts"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "making csv with bold and sorted by pāli alphabet"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

poetry run python ods2csv-sort.py "../spreadsheets/dps.ods" PALI

mv "../spreadsheets/dps.ods-pali-s.csv" "../spreadsheets/dps-full.csv"

poetry run python "random-test.py"

echo "dps-test.csv has been made"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date

poetry run python "sbs-pd-feedback.py"

echo "sbs-pd-feedback.csv has been made"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date

poetry run python "dhp-feedback.py"

echo "filter DHP words from DPS"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date

poetry run python "feedback-dps.py"

echo "add feedback to DPS"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date

poetry run python "sutta-pitaka-feedback.py"

echo "filter sutta-pitaka words from DPS"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date

poetry run python "roots-feedback.py"

echo "roots"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date

poetry run python "sbs-pd-filter.py"

echo "filter SBS words from DPS"

cd "../inflection"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
poetry run python "inflection generator.py"

cd "../inflection-en"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
poetry run python "inflection generator.py"

date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
cd "../exporter"

# source /home/deva/.cache/pypoetry/virtualenvs/exporter-uJ6yRP2M-py3.10/bin/activate
# poetry shell
poetry run python exporter.py run-generate-html-and-json
poetry run python exporter.py run-generate-goldendict
poetry run python exporter.py run-generate-html-and-json-sbs
poetry run python exporter.py run-generate-goldendict-sbs
# poetry run python exporter.py run-generate-html-and-json-dps-en
# poetry run python exporter.py run-generate-goldendict-dps-en


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
date
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "SBS PED generated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Пали-Русско-Пали Словарь создан"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


echo "unzip and copy to GoldenDict"
cd "../scripts"
poetry run python "unzip-dps.py"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Please open GoldenDict > press Alt+Z > F3 > Rescan now"



# cp '/home/deva/Documents/dps/patimokkha_dict/curated_sources/Pātimokkha Word by Word.csv' '/home/deva/Documents/dps/csv-for-anki/patimokkha-anki.csv'


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Please open Anki and import SBS-PED ; PAT ; DHP; Sutta & DPS & Roots" 
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Analisis up-to-date?"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd "../scripts"

while true; do
    read -p "Move decks to share?" yn
    case $yn in
        [Yy]* ) bash move.sh; break;;
        [Nn]* ) exit;;
        *  ) echo "only yes or no";;
    esac
done

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Anki decks and csv of SBS-PED ; PAT ; DHP & DPS moved for share"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# bash push-all.sh

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "DPD SBS-PD & pali-ru-dict replased on the server"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd "/home/deva/Documents/sasanarakkha/study-tools/temp-push"

while true; do
    read -p "push?" yn
    case $yn in
        [Yy]* ) bash github-assets-uploader.sh; break;;
        [Nn]* ) exit;;
        *  ) echo "only yes or no";;
    esac
done

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "the job is done"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "please push test.md & ru-test.md via VSCode"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd '/home/deva'

code sbs.code-workspace


echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "please change all artifacts in dps via VSCode"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

code dps.code-workspace

cd "/home/deva/Documents/dps/scripts"

google-chrome study-tools-releases.html