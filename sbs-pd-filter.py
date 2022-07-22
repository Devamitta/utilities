
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

# filter all SBS words
test2 = df['Fin'].str.contains('s')
filter = test2
df = df.loc[filter]


# save csv
df.to_csv("../spreadsheets/sbs-pd.csv", sep="\t", index=None)

