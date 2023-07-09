cd '/home/deva/Documents/dpd-db'

poetry run bash bash/makedict.sh

cd '/home/deva/Documents/dps/scripts'

python3 unzip-dpd.py

echo "dpd has been copied"
