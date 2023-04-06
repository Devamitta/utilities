import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

# df_nid = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
# df_nid.fillna("")

# df_nid["DPD-Source1"] = df_nid["Source1"]
# df_nid["DPD-Sutta1"] = df_nid["Sutta1"]
# df_nid["DPD-Example1"] = df_nid["Example1"]
# df_nid["DPD-Source2"] = df_nid["Source 2"]
# df_nid["DPD-Sutta2"] = df_nid["Sutta2"]
# df_nid["DPD-Example2"] = df_nid["Example 2"]

# df_nid = df_nid[['ID', 'DPD-Source1', 'DPD-Sutta1', 'DPD-Example1', 'DPD-Source2', 'DPD-Sutta2', 'DPD-Example2']]

df = pd.read_csv("../spreadsheets/dps-dpd-ex.csv", sep="\t", dtype= str)
df.fillna("")

df = df.drop(['sync'], axis=1)

# df_dps = df_dps[['ID', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# choosing order of columns

# df_dps = df_dps[['ID', 'Meaning in native language', 'Fin-s', 'Test-s', 'ex']]

# df = pd.merge(df_dps, df_nid, how='left')
# df = pd.merge(df_dps, df_nid, how='left')

# df.to_csv("../spreadsheets/temp.csv", sep="\t", index=None)

# test1 = df['Chapter 1'] != ""
test2 = df['Example1'] == df['DPD-Example1']
filter = test2
df_ex1_1 = df.loc[filter]
df_ex1_1['sync'] = "11"

# df_ex1_1.to_csv("../spreadsheets/df_ex1_1.csv", sep="\t", index=None)

# test1 = df['Chapter 1'] != ""
test2 = df['Example1'] == df['DPD-Example2']
filter = test2
df_ex1_2 = df.loc[filter]
df_ex1_2['sync'] = "12"

# df_ex1_2.to_csv("../spreadsheets/df_ex1_2.csv", sep="\t", index=None)

# test1 = df['Chapter 2'] != ""
test2 = df['Example2'] == df['DPD-Example2']
filter = test2
df_ex2_2 = df.loc[filter]
df_ex2_2['sync'] = "22"

# df_ex2_2.to_csv("../spreadsheets/df_ex2_2.csv", sep="\t", index=None)

# test1 = df['Chapter 2'] != ""
test2 = df['Example2'] == df['DPD-Example1']
filter = test2
df_ex2_1 = df.loc[filter]
df_ex2_1['sync'] = "21"

# df_ex2_1.to_csv("../spreadsheets/df_ex2_1.csv", sep="\t", index=None)

# test1 = df['Chapter 2'] != ""
test2 = df['Example3'] == df['DPD-Example2']
filter = test2
df_ex3_2 = df.loc[filter]
df_ex3_2['sync'] = "32"

# df_ex3_2.to_csv("../spreadsheets/df_ex3_2.csv", sep="\t", index=None)

# test1 = df['Chapter 2'] != ""
test2 = df['Example3'] == df['DPD-Example1']
filter = test2
df_ex3_1 = df.loc[filter]
df_ex3_1['sync'] = "31"

# df_ex3_1.to_csv("../spreadsheets/df_ex3_1.csv", sep="\t", index=None)

# test1 = df['Chapter 2'] != ""
test2 = df['Example4'] == df['DPD-Example1']
filter = test2
df_ex4_1 = df.loc[filter]
df_ex4_1['sync'] = "41"

# df_ex4_1.to_csv("../spreadsheets/df_ex4_1.csv", sep="\t", index=None)

# test1 = df['Chapter 2'] != ""
test2 = df['Example4'] == df['DPD-Example2']
filter = test2
df_ex4_2 = df.loc[filter]
df_ex4_2['sync'] = "42"

# df_ex4_2.to_csv("../spreadsheets/df_ex4_2.csv", sep="\t", index=None)


# if headword from df2 is in df1, then delete whole row from df2

# logix = df_DHP2['Pāli1'].isin(df_DHP1['Pāli1'])

# df_DHP4 = df_DHP2.drop(df_DHP2[logix].index)

# if headword from df_ex1_2 is in df_ex1_1, then delete whole row from df_ex1_2

logix = df_ex1_2['ID'].isin(df_ex1_1['ID'])

df_ex1_2 = df_ex1_2.drop(df_ex1_2[logix].index)

df_ex1 = pd.concat([df_ex1_1, df_ex1_2])

# if headword from df_ex2_1 is in df_ex1, then delete whole row from df_ex2_1

logix = df_ex2_1['ID'].isin(df_ex1['ID'])

df_ex2_1 = df_ex2_1.drop(df_ex2_1[logix].index)

df_ex1 = pd.concat([df_ex1, df_ex2_1])

# if headword from df_ex2_2 is in df_ex1, then delete whole row from df_ex2_2

logix = df_ex2_2['ID'].isin(df_ex1['ID'])

df_ex2_2 = df_ex2_2.drop(df_ex2_2[logix].index)

df_ex1 = pd.concat([df_ex1, df_ex2_2])

# if headword from df_ex3_1 is in df_ex1, then delete whole row from df_ex3_1

logix = df_ex3_1['ID'].isin(df_ex1['ID'])

df_ex3_1 = df_ex3_1.drop(df_ex3_1[logix].index)

df_ex1 = pd.concat([df_ex1, df_ex3_1])

# if headword from df_ex3_2 is in df_ex1, then delete whole row from df_ex3_2

logix = df_ex3_2['ID'].isin(df_ex1['ID'])

df_ex3_2 = df_ex3_2.drop(df_ex3_2[logix].index)

df_ex1 = pd.concat([df_ex1, df_ex3_2])

# if headword from df_ex4_1 is in df_ex1, then delete whole row from df_ex4_1

logix = df_ex4_1['ID'].isin(df_ex1['ID'])

df_ex4_1 = df_ex4_1.drop(df_ex4_1[logix].index)

df_ex1 = pd.concat([df_ex1, df_ex4_1])

# if headword from df_ex4_2 is in df_ex1, then delete whole row from df_ex4_2

logix = df_ex4_2['ID'].isin(df_ex1['ID'])

df_ex4_2 = df_ex4_2.drop(df_ex4_2[logix].index)

df_combined = pd.concat([df_ex1, df_ex4_2])




# df_combined = pd.concat([df_ex1_1, df_ex1_2, df_ex2_1, df_ex2_2, df_ex3_1, df_ex3_2])

df_combined = df_combined[['ID', 'sync']]

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("")

df_dps = df_dps.drop(['sync'], axis=1)

df_sync = pd.merge(df_dps, df_combined, how='left')

df_sync.to_csv("../spreadsheets/df_sync.csv", sep="\t", index=None)




