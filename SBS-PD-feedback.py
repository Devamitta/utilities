
import pandas as pd
import random

df = pd.read_csv("/home/deva/Documents/dps/spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

# filter all SBS words
test2 = df['Fin'].str.contains('s')
filter = test2
df = df.loc[filter]

# make Feedback
df.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500="+df['Pāli1']+"\">feedback</a>")


# save csv
df.to_csv("/home/deva/Documents/dps/spreadsheets/sbs-pd.csv", sep="\t", index=None)

