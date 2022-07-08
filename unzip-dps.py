from datetime import date

today = date.today()

from zipfile import ZipFile

with ZipFile(f'/home/deva/Documents/dps/exporter/share/sbs-pd.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall('/home/deva/Documents/GoldenDict')

with ZipFile(f'/home/deva/Documents/dps/exporter/share/ПалиСловарь.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall('/home/deva/Documents/GoldenDict')
