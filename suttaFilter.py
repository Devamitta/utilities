#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import re

df_nid = pd.read_csv("/home/deva/Documents/dps/spreadsheets/nidh_bold.csv", sep="\t", dtype= str)
df_nid.fillna("", inplace=True)

df_dps = pd.read_csv("/home/deva/Documents/dps/spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("", inplace=True)


# In[ ]:


# which sutta searching
sutta = input("number of sutta to search: ")
# sutta = "SN 35.93"


# In[ ]:


# filter all words from Source1 (choose strictly fit or contain)
test1 = df_nid['Source1'] == sutta
# test1 = df_nid['Source1'].str.contains(sutta)
filter = test1
df1 = df_nid.loc[filter]


# In[ ]:


# filter all words from Source2 (choose strictly fit or contain)
test2 = df_nid['Source 2'] == sutta
# test2 = df_nid['Source 2'].str.contains(sutta)
filter = test2
df2 = df_nid.loc[filter]

# if headword from df2 is in df1, then delete whole row from df2

logix = df2['Pāli1'].isin(df1['Pāli1'])

df2 = df2.drop(df2[logix].index)


# In[ ]:


# move examples from 2 to 1
df2["Source1"] = df2["Source 2"]
df2["Sutta1"] = df2["Sutta2"]
df2["Example1"] = df2["Example 2"]


# In[ ]:


# combine two lists
# df_combined = df1 + df2
df_combined = df1.append(df2)

# make source2 sutta2 example2 empty
test0 = df_combined['Pāli1'] != ""
filter = test0
df_combined.loc[filter, ['Source 2']] = ""
df_combined.loc[filter, ['Sutta2']] = ""
df_combined.loc[filter, ['Example 2']] = ""


# In[ ]:


# if headword from df_combined is in df_dps, then delete whole row from df_combined

logix = df_combined['Pāli1'].isin(df_dps['Pāli1'])

df_final = df_combined.drop(df_combined[logix].index)

# filter by alphabet
df_final = df_final.sort_values(by="Pāli1")


# In[ ]:


# save csv
df_final.to_csv(f"/home/deva/Documents/dps/spreadsheets/words_from/words_from_{sutta}.csv", sep="\t", index=None)


# In[ ]:


# print the result
print ("__________________")
print (f"done with sutta: {sutta}")
print ("see folder /home/deva/Documents/dps/spreadsheets/words_from/")

