
import pandas as pd

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

df_anki = df.drop(['sbs_class', 'count'], axis=1)

print("columns 'sbs_class', 'count' has been dropped")

# # change ru_meaning
# test1 = df['pali_1'] != ""
# filter = test1
# df.loc[filter, ['ru_meaning']] = ""

# # filter all SBS words
# test2 = df['Fin'].str.contains('s')
# filter = test2
# df = df.loc[filter]


# save csv
df_anki.to_csv("../csv-for-anki/dps-anki.csv", sep="\t", index=None)

