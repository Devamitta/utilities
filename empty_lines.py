#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re

df_dps = pd.read_csv("/home/deva/Documents/dps/spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("", inplace=True)
df_dps.drop([0], inplace = True)
df_dps.drop([1], inplace = True)


# In[2]:


# save csv
df_dps.to_csv(f"/home/deva/Documents/dps/spreadsheets/dps-full.csv", sep="\t", index=None)

