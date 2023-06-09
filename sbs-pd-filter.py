
import pandas as pd

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change ru_meaning
test1 = df['pali_1'] != ""
filter = test1
df.loc[filter, ['ru_meaning']] = ""

# filter all SBS words
test2 = df['Fin'].str.contains('s')
filter = test2
df_sbs = df.loc[filter]

# # save csv
# df_sbs.to_csv("../csv-for-anki/sbs-pd.csv", sep="\t", index=None)

# filter all class
test2 = df['sbs_class_anki'] != ""
filter = test2
df_class = df.loc[filter]

# if headword from df2 is in df1, then delete whole row from df2

logix = df_class['pali_1'].isin(df_sbs['pali_1'])

df_uniq = df_class.drop(df_class[logix].index)

df_combined = pd.concat([df_sbs, df_uniq])

# filter all suttas
test3 = df['sbs_category'] != ""
filter = test3
df_sutta = df.loc[filter]

# if headword from df2 is in df1, then delete whole row from df2

logix = df_sutta['pali_1'].isin(df_combined['pali_1'])

df_uniq_s = df_sutta.drop(df_sutta[logix].index)

df_combined_final = pd.concat([df_combined, df_uniq_s])

# save csv
df_combined_final.to_csv("../spreadsheets/sbs-pd.csv", sep="\t", index=None)




