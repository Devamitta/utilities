echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "making filtered_csv"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cd "/home/deva/Documents/dps/scripts"

poetry run python comparing_dpd_dps.py

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "moving them to dpd-db"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cp -rf "/home/deva/Documents/dps/spreadsheets/to-merge" "/home/deva/Documents/dpd-db/dps/"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "moving dps-full to dpd-db"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

cp -f "/home/deva/Documents/dps/spreadsheets/dps-full.csv" "/home/deva/Documents/dpd-db/dps/dps.tsv"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "push in vscode"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

code '/home/deva/Documents/dpd-db'