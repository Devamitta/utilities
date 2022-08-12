
import pandas as pd

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

df_anki = df.drop(['class', 'count'], axis=1)

print("columns 'class', 'count' has been dropped")

# # change Meaning in native language
# test1 = df['Pāli1'] != ""
# filter = test1
# df.loc[filter, ['Meaning in native language']] = ""

# # filter all SBS words
# test2 = df['Fin'].str.contains('s')
# filter = test2
# df = df.loc[filter]


# save csv
df_anki.to_csv("../spreadsheets/dps-anki.csv", sep="\t", index=None)

