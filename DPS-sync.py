import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

# df_nid = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
# df_nid.fillna("")

# df_nid["DPD_source_1"] = df_nid["source_1"]
# df_nid["DPD_sutta_1"] = df_nid["sutta_1"]
# df_nid["DPD_example_1"] = df_nid["example_1"]
# df_nid["DPD_source_2"] = df_nid["source_2"]
# df_nid["DPD_sutta_2"] = df_nid["sutta_2"]
# df_nid["DPD_example_2"] = df_nid["example_2"]

# df_nid = df_nid[['id', 'DPD_source_1', 'DPD_sutta_1', 'DPD_example_1', 'DPD_source_2', 'DPD_sutta_2', 'DPD_example_2']]

df = pd.read_csv("../spreadsheets/dps-dpd-ex.csv", sep="\t", dtype= str)
df.fillna("")

df = df.drop(['sync'], axis=1)

# df_dps = df_dps[['id', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# choosing order of columns

# df_dps = df_dps[['id', 'ru_meaning', 'Fin-s', 'Test-s', 'sbs_class_anki']]

# df = pd.merge(df_dps, df_nid, how='left')
# df = pd.merge(df_dps, df_nid, how='left')

# df.to_csv("../spreadsheets/temp.csv", sep="\t", index=None)

# test1 = df['sbs_chapter_1'] != ""
test2 = df['example_1'] == df['DPD_example_1']
filter = test2
df_ex1_1 = df.loc[filter]
df_ex1_1['sync'] = "11"

# df_ex1_1.to_csv("../spreadsheets/df_ex1_1.csv", sep="\t", index=None)

# test1 = df['sbs_chapter_1'] != ""
test2 = df['example_1'] == df['DPD_example_2']
filter = test2
df_ex1_2 = df.loc[filter]
df_ex1_2['sync'] = "12"

# df_ex1_2.to_csv("../spreadsheets/df_ex1_2.csv", sep="\t", index=None)

# test1 = df['sbs_chapter_2'] != ""
test2 = df['example_2'] == df['DPD_example_2']
filter = test2
df_ex2_2 = df.loc[filter]
df_ex2_2['sync'] = "22"

# df_ex2_2.to_csv("../spreadsheets/df_ex2_2.csv", sep="\t", index=None)

# test1 = df['sbs_chapter_2'] != ""
test2 = df['example_2'] == df['DPD_example_1']
filter = test2
df_ex2_1 = df.loc[filter]
df_ex2_1['sync'] = "21"

# df_ex2_1.to_csv("../spreadsheets/df_ex2_1.csv", sep="\t", index=None)

# test1 = df['sbs_chapter_2'] != ""
test2 = df['sbs_example_3'] == df['DPD_example_2']
filter = test2
df_ex3_2 = df.loc[filter]
df_ex3_2['sync'] = "32"

# df_ex3_2.to_csv("../spreadsheets/df_ex3_2.csv", sep="\t", index=None)

# test1 = df['sbs_chapter_2'] != ""
test2 = df['sbs_example_3'] == df['DPD_example_1']
filter = test2
df_ex3_1 = df.loc[filter]
df_ex3_1['sync'] = "31"

# df_ex3_1.to_csv("../spreadsheets/df_ex3_1.csv", sep="\t", index=None)

# test1 = df['sbs_chapter_2'] != ""
test2 = df['sbs_example_4'] == df['DPD_example_1']
filter = test2
df_ex4_1 = df.loc[filter]
df_ex4_1['sync'] = "41"

# df_ex4_1.to_csv("../spreadsheets/df_ex4_1.csv", sep="\t", index=None)

# test1 = df['sbs_chapter_2'] != ""
test2 = df['sbs_example_4'] == df['DPD_example_2']
filter = test2
df_ex4_2 = df.loc[filter]
df_ex4_2['sync'] = "42"

# df_ex4_2.to_csv("../spreadsheets/df_ex4_2.csv", sep="\t", index=None)


# if headword from df2 is in df1, then delete whole row from df2

# logix = df_DHP2['pali_1'].isin(df_DHP1['pali_1'])

# df_DHP4 = df_DHP2.drop(df_DHP2[logix].index)

# if headword from df_ex1_2 is in df_ex1_1, then delete whole row from df_ex1_2

logix = df_ex1_2['id'].isin(df_ex1_1['id'])

df_ex1_2 = df_ex1_2.drop(df_ex1_2[logix].index)

df_ex1 = pd.concat([df_ex1_1, df_ex1_2])

# if headword from df_ex2_1 is in df_ex1, then delete whole row from df_ex2_1

logix = df_ex2_1['id'].isin(df_ex1['id'])

df_ex2_1 = df_ex2_1.drop(df_ex2_1[logix].index)

df_ex1 = pd.concat([df_ex1, df_ex2_1])

# if headword from df_ex2_2 is in df_ex1, then delete whole row from df_ex2_2

logix = df_ex2_2['id'].isin(df_ex1['id'])

df_ex2_2 = df_ex2_2.drop(df_ex2_2[logix].index)

df_ex1 = pd.concat([df_ex1, df_ex2_2])

# if headword from df_ex3_1 is in df_ex1, then delete whole row from df_ex3_1

logix = df_ex3_1['id'].isin(df_ex1['id'])

df_ex3_1 = df_ex3_1.drop(df_ex3_1[logix].index)

df_ex1 = pd.concat([df_ex1, df_ex3_1])

# if headword from df_ex3_2 is in df_ex1, then delete whole row from df_ex3_2

logix = df_ex3_2['id'].isin(df_ex1['id'])

df_ex3_2 = df_ex3_2.drop(df_ex3_2[logix].index)

df_ex1 = pd.concat([df_ex1, df_ex3_2])

# if headword from df_ex4_1 is in df_ex1, then delete whole row from df_ex4_1

logix = df_ex4_1['id'].isin(df_ex1['id'])

df_ex4_1 = df_ex4_1.drop(df_ex4_1[logix].index)

df_ex1 = pd.concat([df_ex1, df_ex4_1])

# if headword from df_ex4_2 is in df_ex1, then delete whole row from df_ex4_2

logix = df_ex4_2['id'].isin(df_ex1['id'])

df_ex4_2 = df_ex4_2.drop(df_ex4_2[logix].index)

df_combined = pd.concat([df_ex1, df_ex4_2])




# df_combined = pd.concat([df_ex1_1, df_ex1_2, df_ex2_1, df_ex2_2, df_ex3_1, df_ex3_2])

df_combined = df_combined[['id', 'sync']]

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("")

df_dps = df_dps.drop(['sync'], axis=1)

df_sync = pd.merge(df_dps, df_combined, how='left')

df_sync.to_csv("../spreadsheets/df_sync.csv", sep="\t", index=None)




