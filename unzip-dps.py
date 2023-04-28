from datetime import date

today = date.today()

from zipfile import ZipFile

with ZipFile(f'../exporter/share/sbs-pd.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall('/home/deva/Documents/GoldenDict')

with ZipFile(f'../exporter/share/ru-pali-dictionary.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall('/home/deva/Documents/GoldenDict')

# with ZipFile(f'../exporter/share/dps.zip', 'r') as zipObj:
#    # Extract all the contents of zip file in current directory
#    zipObj.extractall('/home/deva/Documents/GoldenDict')
