#!/usr/bin/env python
# coding: utf-8

# In[1]:



from datetime import date

today = date.today()

from zipfile import ZipFile

with ZipFile(f'/home/deva/Documents/dps/exporter/share/sbs-pd.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall('/home/deva/Documents/GoldenDict')

