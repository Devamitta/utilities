from datetime import date

today = date.today()

from zipfile import ZipFile

with ZipFile(f'../exporter/share/dps-test.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall('/home/deva/Documents/GoldenDict')
