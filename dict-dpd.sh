cd '/home/deva/Documents/dpd-db'

poetry run bash bash/makedict.sh

cd '/home/deva/Documents/dps/scripts'

poetry run python unzip-dpd.py

echo "dpd has been copied"
