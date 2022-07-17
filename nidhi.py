#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas_ods_reader import read_ods 
import re

df = read_ods("/home/deva/Documents/dpd/spreadsheets/dpd.ods")
df.fillna("", inplace=True)
df = df.astype(str)
df.rename(columns=df.iloc[0], inplace = True)
df.drop([0], inplace = True)
# saving csv file
df.to_csv("/home/deva/Documents/dpd/spreadsheets/dpd.csv", sep="\t", index=None)


# In[2]:


# convert dpd root list to csv
df_root = read_ods("/home/deva/Documents/dpd/spreadsheets/dpd.ods", sheet=2)
df_root.fillna("", inplace=True)
df_root = df_root.astype(str)
df_root.rename(columns=df_root.iloc[0], inplace = True)
df_root.drop([0], inplace = True)
df_root.to_csv("/home/deva/Documents/dpd/spreadsheets/roots.csv", sep="\t", index=None)


# In[3]:


# concat Pali Root
test1 = df['Pāli Root'] != ""
test2 = df['Pāli1'] != ""
filter = test1 & test2
df.loc[filter, ['Pāli Root']] = df['Pāli Root'] + " " + df['Grp'] + " " + df['Sgn'] + " " + "(" + "to " + df['Root Meaning'] + ")"


# In[4]:


# concat English Meaning
test3 = df['Literal Meaning'] != ""
filter = test3 & test2
df.loc[filter, ['Meaning IN CONTEXT']] = df['Meaning IN CONTEXT'] + "; lit. " + df['Literal Meaning']


# In[5]:


# change FIN
filter = test2
df.loc[filter, ['Fin']] = "p"


# In[6]:


# managing Grammar
test4 = df['POS'] == df['Grammar']
# test4 = df['POS'].str.contains(fr"{df['Grammar']}")
filter = test4
df.loc[filter, ['Grammar']] = ""


# In[7]:


# # filter for easy to open csv
# df_5000 = df.tail(3000)
# df = df_5000


# In[8]:


# # if pos in grammar then remove pos from nothing in grammar
df['Grammar']=df.apply(lambda x: x['Grammar'].replace(x['Derived from'], ""), axis=1)

df['Grammar']=df.apply(lambda x: x['Grammar'].replace(x['POS'], ""), axis=1)

df['Grammar']=df.apply(lambda x: x['Grammar'].replace("na", ""), axis=1)


# In[9]:


# # # cleaning Grammar
df['Grammar'] = df['Grammar'].replace(' of ', '', regex=True)

df['Grammar'] = df['Grammar'].replace('of', '', regex=True)

df['Grammar'] = df['Grammar'].replace(' from ', '', regex=True)

df['Grammar'] = df['Grammar'].replace({r'^(,)'}, '',  regex=True)

df['Grammar'] = df['Grammar'].replace({r'^( )'}, '',  regex=True)

df['Grammar'] = df['Grammar'].replace({r'( )$'}, '',  regex=True)

df['Grammar'] = df['Grammar'].replace({r'(,)$'}, '',  regex=True)

df['Grammar'] = df['Grammar'].replace({r'^(, )'}, '',  regex=True)

# choosing order of columns

df = df[['Pāli1', 'Fin', 'POS', 'Grammar', 'Derived from', 'Neg', 
       'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Pāli Root', 'Base',  
       'Construction', 'Sanskrit', 'Sk Root', 
       'Variant – same constr or diff reading', 'Commentary', 'Notes', 
       'Source1', 'Sutta1', 'Example1', 'Source 2', 'Sutta2', 'Example 2',
       'Stem', 'Pattern', 'Category']]
df.insert(10, 'Ru', None)
df.insert(11, 'SBS Meaning', None)
df.insert(26, 'SBS Pali chant name', None)
df.insert(27, 'SBS English chant name', None)
df.insert(28, 'SBS Chapter', None)
df.insert(29, 'Source 3', None)
df.insert(30, 'Sutta 3', None)
df.insert(31, 'Example 3', None)
df.insert(32, 'SBS Pali chant name 3', None)
df.insert(33, 'SBS English chant name 3', None)
df.insert(34, 'SBS Chapter 3', None)
df.insert(35, 'SBS index', None)


# In[10]:


# saving csv file
df.to_csv("/home/deva/Documents/dpd/spreadsheets/nidh.csv", sep="\t", index=None)

