
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
# df['source_1'] = df['source_1'].str.replace(' ', '_')
# df['source_2'] = df['source_2'].str.replace(' ', '_')
# df['sbs_source_3'] = df['sbs_source_3'].str.replace(' ', '_')

# filter all DHP from source_1
test2 = df['source_1'].str.contains('DHP')
test3 = df['sutta_1'].str.contains('vaggo')
filter = test2 & test3
df_DHP1 = df.loc[filter]

# filter all DHP from source_1
test2 = df['source_2'].str.contains('DHP')
test3 = df['sutta_2'].str.contains('vaggo')
# test4 = ~df['source_1'].str.contains('DHP')
filter = test2 & test3
df_DHP2 = df.loc[filter]

# # move examples from 2 to 1
# df_sutta2["source_1"] = df_sutta2["source_2"]
# df_sutta2["sutta_1"] = df_sutta2["sutta_2"]
# df_sutta2["example_1"] = df_sutta2["example_2"]

# df_sutta2["source_2"] = ""
# df_sutta2["sutta_2"] = ""
# df_sutta2["example_2"] = ""


# # move examples from 3 to 1
# df_sutta3["source_1"] = df_sutta3["sbs_source_3"]
# df_sutta3["sutta_1"] = df_sutta3["sbs_sutta_3"]
# df_sutta3["example_1"] = df_sutta3["sbs_example_3"]

# df_sutta2["sbs_source_3"] = ""
# df_sutta2["sbs_sutta_3"] = ""
# df_sutta2["sbs_example_3"] = ""



# if headword from df_sutta2 is in df_sutta1, then delete whole row from df_sutta2

# logix = df_sutta2['pali_1'].isin(df_sutta1['pali_1'])

# df_sutta4 = df_sutta2.drop(df_sutta2[logix].index)

# if headword from df is in df_sutta1, then delete whole row from df

logix = df['pali_1'].isin(df_DHP1['pali_1'])

df = df.drop(df[logix].index)

# save csv
# df.to_csv("../spreadsheets/df_without_1.csv", sep="\t", index=None)

# if headword from df is in df_sutta2, then delete whole row from df

logix = df['pali_1'].isin(df_DHP2['pali_1'])

df = df.drop(df[logix].index)

# save csv
df.to_csv("../spreadsheets/df_without_dhp.csv", sep="\t", index=None)

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("", inplace=True)

df = df[['id', 'Test-s']]

# df_dps_merged = pd.merge(df_dps, df_nid, how='left')
df_dps_merged = pd.merge(df_dps, df, how='left')

df_dps_merged.to_csv("../spreadsheets/dpd-without-dhp.csv", sep="\t", index=None)
