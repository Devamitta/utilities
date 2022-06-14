#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("/home/deva/Documents/dps/spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)


# In[3]:


# change Test
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Test']] = "4"


# In[5]:


# make Feedback
df.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/1iMD9sCSWFfJAFCFYuG9HRIyrr9KFRy0nAOVApM998wM/viewform?usp=pp_url&entry.438735500="+df['Pāli1']+"\">feedback</a>")


# In[8]:


# save csv
df.to_csv("/home/deva/Documents/dps/spreadsheets/dps-feedback.csv", sep="\t", index=None)

