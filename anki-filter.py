
import pandas as pd

df = pd.read_csv("/home/deva/Documents/dpd-db/csvs/dpd-dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

df_anki = df.drop(['pali_2', 'Fin', 'Non IA', 'Family', 'Word Family', 'Family2', 'Non-Root In Comps', 'Cognate', 'Category', 'Link', 'Buddhadatta', 'sbs_class'], axis=1)

# print("columns 'sbs_class', 'count' has been dropped")

# filter all dps words
test1 = df_anki['ru_meaning'] != ""
filter = test1
df_anki = df_anki.loc[filter]

# # filter all SBS words
# test2 = df['Fin'].str.contains('s')
# filter = test2
# df = df.loc[filter]


# save csv
df_anki.to_csv("../spreadsheets/dps-full.csv", sep="\t", index=None)

