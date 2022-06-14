#!/usr/bin/env python
# coding: utf-8

# In[2]:



from datetime import date

today = date.today()

from zipfile import ZipFile

with ZipFile(f'/home/deva/Documents/dps/exporter/share/dps-{today}.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall('/home/deva/Documents/dps/dictionary')

