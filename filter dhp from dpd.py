
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dpd+sbs.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# filter all DHP words
test2 = df['Test-s'].str.contains('d')
filter = test2
df = df.loc[filter]

# save csv
# df.to_csv("../spreadsheets/df.csv", sep="\t", index=None)


# replace all sutta numbers with '_'
# df['Source1'] = df['Source1'].str.replace(' ', '_')
# df['Source2'] = df['Source2'].str.replace(' ', '_')
# df['Source3'] = df['Source3'].str.replace(' ', '_')

# filter all DHP from Source1
test2 = df['Source1'].str.contains('DHP')
test3 = df['Sutta1'].str.contains('vaggo')
filter = test2 & test3
df_DHP1 = df.loc[filter]

# filter all DHP from Source1
test2 = df['Source 2'].str.contains('DHP')
test3 = df['Sutta2'].str.contains('vaggo')
# test4 = ~df['Source1'].str.contains('DHP')
filter = test2 & test3
df_DHP2 = df.loc[filter]

# # move examples from 2 to 1
# df_sutta2["Source1"] = df_sutta2["Source2"]
# df_sutta2["Sutta1"] = df_sutta2["Sutta2"]
# df_sutta2["Example1"] = df_sutta2["Example2"]

# df_sutta2["Source2"] = ""
# df_sutta2["Sutta2"] = ""
# df_sutta2["Example2"] = ""


# # move examples from 3 to 1
# df_sutta3["Source1"] = df_sutta3["Source3"]
# df_sutta3["Sutta1"] = df_sutta3["Sutta3"]
# df_sutta3["Example1"] = df_sutta3["Example3"]

# df_sutta2["Source3"] = ""
# df_sutta2["Sutta3"] = ""
# df_sutta2["Example3"] = ""



# if headword from df_sutta2 is in df_sutta1, then delete whole row from df_sutta2

# logix = df_sutta2['Pāli1'].isin(df_sutta1['Pāli1'])

# df_sutta4 = df_sutta2.drop(df_sutta2[logix].index)

# if headword from df is in df_sutta1, then delete whole row from df

logix = df['Pāli1'].isin(df_DHP1['Pāli1'])

df = df.drop(df[logix].index)

# save csv
# df.to_csv("../spreadsheets/df_without_1.csv", sep="\t", index=None)

# if headword from df is in df_sutta2, then delete whole row from df

logix = df['Pāli1'].isin(df_DHP2['Pāli1'])

df = df.drop(df[logix].index)

# save csv
df.to_csv("../spreadsheets/df_without_dhp.csv", sep="\t", index=None)

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("", inplace=True)

df = df[['ID', 'Test-s']]

# df_dps_merged = pd.merge(df_dps, df_nid, how='left')
df_dps_merged = pd.merge(df_dps, df, how='left')

df_dps_merged.to_csv("../spreadsheets/dpd-without-dhp.csv", sep="\t", index=None)
