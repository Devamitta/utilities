# cd "/home/deva/Downloads"

# mv -f "dpd.ods" "/home/deva/Documents/dpd-br/dpd.ods"

cd "/home/deva/Documents/dpd-db"

git pull

poetry install

poetry run bash bash/build_db.sh

poetry run python scripts/sbs_russian_from_tsv.py

echo "db has been updated"

poetry run python scripts/anki_csvs.py

echo "dpd-full.csv has been updated"

poetry run python scripts/dpd_dps_csv.py

echo "dpd_dps.csv has been updated"

cd "/home/deva/Documents/dps/scripts"

poetry run python "nidhi_bold.py"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "nidh_bold.csv has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

poetry run python "DPD-freq-insert.py"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "dpd-dps-freq.csv has been updated"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
