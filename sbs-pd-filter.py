
import pandas as pd

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

# filter all SBS words
test2 = df['Fin'].str.contains('s')
filter = test2
df_sbs = df.loc[filter]

# # save csv
# df_sbs.to_csv("../csv-for-anki/sbs-pd.csv", sep="\t", index=None)

# filter all class
test2 = df['ex'] != ""
filter = test2
df_class = df.loc[filter]

# if headword from df2 is in df1, then delete whole row from df2

logix = df_class['Pāli1'].isin(df_sbs['Pāli1'])

df_uniq = df_class.drop(df_class[logix].index)

df_combined = pd.concat([df_sbs, df_uniq])

# save csv
df_combined.to_csv("../spreadsheets/sbs-pd.csv", sep="\t", index=None)




