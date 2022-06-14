#!/usr/bin/env python
# coding: utf-8

# In[149]:


import pandas as pd
import random

df = pd.read_csv("/home/deva/Documents/dps/spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)


# In[150]:


# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""


# In[151]:


ran = random.sample(range(1, 100), 1)
ran = str(ran[0])


# In[152]:


# change Test
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Test']] = ran


# In[153]:


# filter all SBS words
test2 = df['Fin'].str.contains('s')
filter = test2
df = df.loc[filter]


# In[154]:


# make Feedback
df.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500="+df['Pāli1']+"\">feedback</a>")


# In[155]:


# make double tags
df.insert(40, 'Tags', None)

df["Tags"] = df["Pali chant 2"]

test3 = df['Pali chant 3'] != ""
filter = test3
df.loc[filter, ['Tags']] = df['Pali chant 2'] + " " + df['Pali chant 3']


# In[156]:


# sort by Index
df = df.sort_values(by=['Index', 'Example 2'])


# In[157]:


# save csv
df.to_csv("/home/deva/Documents/dps/spreadsheets/sbs-pd.csv", sep="\t", index=None)


# In[158]:


import markdown
result_markdown = markdown.markdown(f"""
# DHP Vocab

UNDER DEVELOPMENT

Made for memorization of words from DHP. It is available for public testing and [feedback](https://docs.google.com/forms/d/e/1FAIpQLSf9boBe7k5tCwq7LdWgBHHGIPVc4ROO5yjVDo1X5LDAxkmGWQ/viewform?usp=pp_url&amp;entry.1433863141=DHP). Be sure to regularly download the latest content here.

This tool is recommended to use together with the [DHP grammatical analysis](https://buddhism.lib.ntu.edu.tw/DLMBS/en/lesson/pali/lesson_pali3.jsp)

- **[Download the latest update](https://github.com/sasanarakkha/study-tools/raw/main/Anki_Decks/DHP_Vocab/DHP%20vocab.apkg)**

- Install [Anki](https://apps.ankiweb.net/)

- Double-click on the downloaded file SBS Pāli-English Vocab.apkg, and it will appear in your Anki.

# Recomended way of studying this deck:

- first read some vagga from DHP in the Pāli and in [the analysis](https://buddhism.lib.ntu.edu.tw/DLMBS/en/lesson/pali/lesson_pali3.jsp)

- in Anki go to **Browse**

![2022-04-17_20-04](https://user-images.githubusercontent.com/39419221/163944779-ad73b9a5-4478-410c-abf6-466e03b9b777.png)

- Select deck **DHP Vocab** in the left panel
- Select all card by **Ctrl + A**
- Right click and choose **Toggle Suspend** (Ctrl + J)

Now all cards are inactive for study.

![2022-04-19_15-03](https://user-images.githubusercontent.com/39419221/163945216-713c1d2e-ce3f-4f28-ac49-93e7fdb56033.png)


- Select deck **DHP Vocab** in the left panel
- Select vagga by searching name of the vagga (e.g. appamādavaggo) in this deck
- Select all card by **Ctrl + A**
- Right click and choose **Toggle Suspend** (Ctrl + J) 


Now all cards from selected vagga will appear in your Anki daily routine. After you finish them, you may repeat the process with another vagga and so on.


# Update existing deck with keeping statistic

This work is based on the [DPD](https://digitalpalidictionary.github.io/) which is the work in progress and updating regularly. Because of this, time after time may be added or edited some words (for example: the word 'pada' become 'pada 1', because has been found another meaning of this word in another context). We need time after time to remove those duplicated words, which are not existing any more. For this reason, we have a field **"Test"**
After you updated your Anki Deck (same way, just by double-clicking on the latest downloaded file). In **Browse** type:

`"deck:DHP vocab" -test:`{ran}

It will show all cards which do not have number '{ran}' in field "Test". And you can easily delate all of this old words, by selecting all (**Ctrl + A**) and deleting (**Ctrl + Delete**). 

Now you are up-to-date.

With every next update, this 'test number' will be different.

- If English is not your first language, it is always recommended to translate words to your native language. For this, we have empty field "native". You can feel it. And even with next update, this field still will keep all your info.
""")

with open('/home/deva/Documents/sasanarakkha/study-tools/Anki_Decks/DHP_Vocab/DHP_Vocab.md', 'w') as f:
    f.write(result_markdown)
f.close()

