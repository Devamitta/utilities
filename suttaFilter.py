#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import re

df_nid = pd.read_csv("../spreadsheets/nidh_bold.csv", sep="\t", dtype= str)
df_nid.fillna("", inplace=True)

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("", inplace=True)


# In[ ]:


# which sutta searching
sutta = input("number of sutta to search: ")
# sutta = "SN 35.93"


# In[ ]:


# filter all words from source_1 (choose strictly fit or contain)
test1 = df_nid['source_1'] == sutta
# test1 = df_nid['source_1'].str.contains(sutta)
filter = test1
df1 = df_nid.loc[filter]


# In[ ]:


# filter all words from source_2 (choose strictly fit or contain)
test2 = df_nid['source_2'] == sutta
# test2 = df_nid['source_2'].str.contains(sutta)
filter = test2
df2 = df_nid.loc[filter]

# if headword from df2 is in df1, then delete whole row from df2

logix = df2['pali_1'].isin(df1['pali_1'])

df2 = df2.drop(df2[logix].index)


# In[ ]:


# move examples from 2 to 1
df2["source_1"] = df2["source_2"]
df2["sutta_1"] = df2["sutta_2"]
df2["example_1"] = df2["example_2"]


# In[ ]:


# combine two lists
# df_combined = df1 + df2
# df_combined = df1.append(df2)
df_combined = pd.concat([df1, df2])


# make source2 sutta2 example2 empty
test0 = df_combined['pali_1'] != ""
filter = test0
df_combined.loc[filter, ['source_2']] = ""
df_combined.loc[filter, ['sutta_2']] = ""
df_combined.loc[filter, ['example_2']] = ""


# In[ ]:


# if headword from df_combined is in df_dps, then delete whole row from df_combined

logix = df_combined['pali_1'].isin(df_dps['pali_1'])

df_final = df_combined.drop(df_combined[logix].index)

# filter by alphabet
df_final = df_final.sort_values(by='pali_1')


# In[ ]:


# save csv
df_final.to_csv(f"../spreadsheets/words_from/words_from_{sutta}.csv", sep="\t", index=None)


# In[ ]:


# print the result
print ("__________________")
print (f"done with sutta: {sutta}")
print ("see folder ../spreadsheets/words_from/")

