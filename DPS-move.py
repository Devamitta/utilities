import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("")

# df = df.drop(['sync'], axis=1)

# df = df[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4', 'move', 'sync']]


# filtering df_0000 and empty and df_extra

test1 = df['move'] == '0000'
filter = test1
df_0000 = df.loc[filter]

df_0000 = df_0000[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# df_0000.to_csv("../spreadsheets/df_0000.csv", sep="\t", index=None)

test1 = df['move'] == "empty"
filter = test1
df_empty = df.loc[filter]

df_empty = df_empty[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# df_empty.to_csv("../spreadsheets/df_empty.csv", sep="\t", index=None)

test1 = df['sync'] == 'e'
filter = test1
df_extra = df.loc[filter]

df_extra.to_csv("../spreadsheets/df_extra.csv", sep="\t", index=None)

# filtering 0001

test1 = df['move'] == '0001'
filter = test1
df_0001 = df.loc[filter]

df_0001["new-sbs_source_4"] = df_0001["source_1"]
df_0001["new-sbs_sutta_4"] = df_0001["sutta_1"]
df_0001["new-sbs_example_4"] = df_0001["example_1"]
df_0001["new-sbs_chant_pali_4"] = df_0001["sbs_chant_pali_1"]
df_0001["new-sbs_chant_eng_4"] = df_0001["sbs_chant_eng_1"]
df_0001["new-sbs_chapter_4"] = df_0001["sbs_chapter_1"]

df_0001["source_1"] = ""
df_0001["sutta_1"] = ""
df_0001["example_1"] = ""
df_0001["sbs_chant_pali_1"] = ""
df_0001["sbs_chant_eng_1"] = ""
df_0001["sbs_chapter_1"] = ""

df_0001["sbs_source_4"] = df_0001["new-sbs_source_4"]
df_0001["sbs_sutta_4"] = df_0001["new-sbs_sutta_4"]
df_0001["sbs_example_4"] = df_0001["new-sbs_example_4"]
df_0001["sbs_chant_pali_4"] = df_0001["new-sbs_chant_pali_4"]
df_0001["sbs_chant_eng_4"] = df_0001["new-sbs_chant_eng_4"]
df_0001["sbs_chapter_4"] = df_0001["new-sbs_chapter_4"]


df_0001 = df_0001[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0001)

# df_0001.to_csv("../spreadsheets/df_0001.csv", sep="\t", index=None)

# filtering 0002

test1 = df['move'] == '0002'
filter = test1
df_0002 = df.loc[filter]

df_0002["new-sbs_source_4"] = df_0002["source_2"]
df_0002["new-sbs_sutta_4"] = df_0002["sutta_2"]
df_0002["new-sbs_example_4"] = df_0002["example_2"]
df_0002["new-sbs_chant_pali_4"] = df_0002["sbs_chant_pali_2"]
df_0002["new-sbs_chant_eng_4"] = df_0002["sbs_chant_eng_2"]
df_0002["new-sbs_chapter_4"] = df_0002["sbs_chapter_2"]

df_0002["source_2"] = ""
df_0002["sutta_2"] = ""
df_0002["example_2"] = ""
df_0002["sbs_chant_pali_2"] = ""
df_0002["sbs_chant_eng_2"] = ""
df_0002["sbs_chapter_2"] = ""

df_0002["sbs_source_4"] = df_0002["new-sbs_source_4"]
df_0002["sbs_sutta_4"] = df_0002["new-sbs_sutta_4"]
df_0002["sbs_example_4"] = df_0002["new-sbs_example_4"]
df_0002["sbs_chant_pali_4"] = df_0002["new-sbs_chant_pali_4"]
df_0002["sbs_chant_eng_4"] = df_0002["new-sbs_chant_eng_4"]
df_0002["sbs_chapter_4"] = df_0002["new-sbs_chapter_4"]


df_0002 = df_0002[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0002)

# df_0002.to_csv("../spreadsheets/df_0002.csv", sep="\t", index=None)


# filtering 0003

test1 = df['move'] == '0003'
filter = test1
df_0003 = df.loc[filter]

df_0003["new-sbs_source_4"] = df_0003["sbs_source_3"]
df_0003["new-sbs_sutta_4"] = df_0003["sbs_sutta_3"]
df_0003["new-sbs_example_4"] = df_0003["sbs_example_3"]
df_0003["new-sbs_chant_pali_4"] = df_0003["sbs_chant_pali_3"]
df_0003["new-sbs_chant_eng_4"] = df_0003["sbs_chant_eng_3"]
df_0003["new-sbs_chapter_4"] = df_0003["sbs_chapter_3"]

df_0003["sbs_source_3"] = ""
df_0003["sbs_sutta_3"] = ""
df_0003["sbs_example_3"] = ""
df_0003["sbs_chant_pali_3"] = ""
df_0003["sbs_chant_eng_3"] = ""
df_0003["sbs_chapter_3"] = ""

df_0003["sbs_source_4"] = df_0003["new-sbs_source_4"]
df_0003["sbs_sutta_4"] = df_0003["new-sbs_sutta_4"]
df_0003["sbs_example_4"] = df_0003["new-sbs_example_4"]
df_0003["sbs_chant_pali_4"] = df_0003["new-sbs_chant_pali_4"]
df_0003["sbs_chant_eng_4"] = df_0003["new-sbs_chant_eng_4"]
df_0003["sbs_chapter_4"] = df_0003["new-sbs_chapter_4"]


df_0003 = df_0003[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0003)

# df_0003.to_csv("../spreadsheets/df_0003.csv", sep="\t", index=None)


# filtering 0010

test1 = df['move'] == '0010'
filter = test1
df_0010 = df.loc[filter]

df_0010["new-sbs_source_3"] = df_0010["source_1"]
df_0010["new-sbs_sutta_3"] = df_0010["sutta_1"]
df_0010["new-sbs_example_3"] = df_0010["example_1"]
df_0010["new-sbs_chant_pali_3"] = df_0010["sbs_chant_pali_1"]
df_0010["new-sbs_chant_eng_3"] = df_0010["sbs_chant_eng_1"]
df_0010["new-sbs_chapter_3"] = df_0010["sbs_chapter_1"]

df_0010["source_1"] = ""
df_0010["sutta_1"] = ""
df_0010["example_1"] = ""
df_0010["sbs_chant_pali_1"] = ""
df_0010["sbs_chant_eng_1"] = ""
df_0010["sbs_chapter_1"] = ""

df_0010["sbs_source_3"] = df_0010["new-sbs_source_3"]
df_0010["sbs_sutta_3"] = df_0010["new-sbs_sutta_3"]
df_0010["sbs_example_3"] = df_0010["new-sbs_example_3"]
df_0010["sbs_chant_pali_3"] = df_0010["new-sbs_chant_pali_3"]
df_0010["sbs_chant_eng_3"] = df_0010["new-sbs_chant_eng_3"]
df_0010["sbs_chapter_3"] = df_0010["new-sbs_chapter_3"]


df_0010 = df_0010[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0010)

# df_0010.to_csv("../spreadsheets/df_0010.csv", sep="\t", index=None)

# filtering 0012

test1 = df['move'] == '0012'
filter = test1
df_0012 = df.loc[filter]

df_0012["new-sbs_source_3"] = df_0012["source_1"]
df_0012["new-sbs_sutta_3"] = df_0012["sutta_1"]
df_0012["new-sbs_example_3"] = df_0012["example_1"]
df_0012["new-sbs_chant_pali_3"] = df_0012["sbs_chant_pali_1"]
df_0012["new-sbs_chant_eng_3"] = df_0012["sbs_chant_eng_1"]
df_0012["new-sbs_chapter_3"] = df_0012["sbs_chapter_1"]

df_0012["source_1"] = ""
df_0012["sutta_1"] = ""
df_0012["example_1"] = ""
df_0012["sbs_chant_pali_1"] = ""
df_0012["sbs_chant_eng_1"] = ""
df_0012["sbs_chapter_1"] = ""

df_0012["new-sbs_source_4"] = df_0012["source_2"]
df_0012["new-sbs_sutta_4"] = df_0012["sutta_2"]
df_0012["new-sbs_example_4"] = df_0012["example_2"]
df_0012["new-sbs_chant_pali_4"] = df_0012["sbs_chant_pali_2"]
df_0012["new-sbs_chant_eng_4"] = df_0012["sbs_chant_eng_2"]
df_0012["new-sbs_chapter_4"] = df_0012["sbs_chapter_2"]

df_0012["source_2"] = ""
df_0012["sutta_2"] = ""
df_0012["example_2"] = ""
df_0012["sbs_chant_pali_2"] = ""
df_0012["sbs_chant_eng_2"] = ""
df_0012["sbs_chapter_2"] = ""

df_0012["sbs_source_4"] = df_0012["new-sbs_source_4"]
df_0012["sbs_sutta_4"] = df_0012["new-sbs_sutta_4"]
df_0012["sbs_example_4"] = df_0012["new-sbs_example_4"]
df_0012["sbs_chant_pali_4"] = df_0012["new-sbs_chant_pali_4"]
df_0012["sbs_chant_eng_4"] = df_0012["new-sbs_chant_eng_4"]
df_0012["sbs_chapter_4"] = df_0012["new-sbs_chapter_4"]

df_0012["sbs_source_3"] = df_0012["new-sbs_source_3"]
df_0012["sbs_sutta_3"] = df_0012["new-sbs_sutta_3"]
df_0012["sbs_example_3"] = df_0012["new-sbs_example_3"]
df_0012["sbs_chant_pali_3"] = df_0012["new-sbs_chant_pali_3"]
df_0012["sbs_chant_eng_3"] = df_0012["new-sbs_chant_eng_3"]
df_0012["sbs_chapter_3"] = df_0012["new-sbs_chapter_3"]


df_0012 = df_0012[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0012)

# df_0012.to_csv("../spreadsheets/df_0012.csv", sep="\t", index=None)


# filtering 0013

test1 = df['move'] == '0013'
filter = test1
df_0013 = df.loc[filter]

df_0013["new-sbs_source_3"] = df_0013["source_1"]
df_0013["new-sbs_sutta_3"] = df_0013["sutta_1"]
df_0013["new-sbs_example_3"] = df_0013["example_1"]
df_0013["new-sbs_chant_pali_3"] = df_0013["sbs_chant_pali_1"]
df_0013["new-sbs_chant_eng_3"] = df_0013["sbs_chant_eng_1"]
df_0013["new-sbs_chapter_3"] = df_0013["sbs_chapter_1"]

df_0013["source_1"] = ""
df_0013["sutta_1"] = ""
df_0013["example_1"] = ""
df_0013["sbs_chant_pali_1"] = ""
df_0013["sbs_chant_eng_1"] = ""
df_0013["sbs_chapter_1"] = ""

df_0013["new-sbs_source_4"] = df_0013["sbs_source_3"]
df_0013["new-sbs_sutta_4"] = df_0013["sbs_sutta_3"]
df_0013["new-sbs_example_4"] = df_0013["sbs_example_3"]
df_0013["new-sbs_chant_pali_4"] = df_0013["sbs_chant_pali_3"]
df_0013["new-sbs_chant_eng_4"] = df_0013["sbs_chant_eng_3"]
df_0013["new-sbs_chapter_4"] = df_0013["sbs_chapter_3"]

df_0013["sbs_source_3"] = ""
df_0013["sbs_sutta_3"] = ""
df_0013["sbs_example_3"] = ""
df_0013["sbs_chant_pali_3"] = ""
df_0013["sbs_chant_eng_3"] = ""
df_0013["sbs_chapter_3"] = ""

df_0013["sbs_source_4"] = df_0013["new-sbs_source_4"]
df_0013["sbs_sutta_4"] = df_0013["new-sbs_sutta_4"]
df_0013["sbs_example_4"] = df_0013["new-sbs_example_4"]
df_0013["sbs_chant_pali_4"] = df_0013["new-sbs_chant_pali_4"]
df_0013["sbs_chant_eng_4"] = df_0013["new-sbs_chant_eng_4"]
df_0013["sbs_chapter_4"] = df_0013["new-sbs_chapter_4"]

df_0013["sbs_source_3"] = df_0013["new-sbs_source_3"]
df_0013["sbs_sutta_3"] = df_0013["new-sbs_sutta_3"]
df_0013["sbs_example_3"] = df_0013["new-sbs_example_3"]
df_0013["sbs_chant_pali_3"] = df_0013["new-sbs_chant_pali_3"]
df_0013["sbs_chant_eng_3"] = df_0013["new-sbs_chant_eng_3"]
df_0013["sbs_chapter_3"] = df_0013["new-sbs_chapter_3"]


df_0013 = df_0013[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0013)

# df_0013.to_csv("../spreadsheets/df_0013.csv", sep="\t", index=None)

# filtering 0020

test1 = df['move'] == '0020'
filter = test1
df_0020 = df.loc[filter]

df_0020["new-sbs_source_3"] = df_0020["source_2"]
df_0020["new-sbs_sutta_3"] = df_0020["sutta_2"]
df_0020["new-sbs_example_3"] = df_0020["example_2"]
df_0020["new-sbs_chant_pali_3"] = df_0020["sbs_chant_pali_2"]
df_0020["new-sbs_chant_eng_3"] = df_0020["sbs_chant_eng_2"]
df_0020["new-sbs_chapter_3"] = df_0020["sbs_chapter_2"]

df_0020["source_2"] = ""
df_0020["sutta_2"] = ""
df_0020["example_2"] = ""
df_0020["sbs_chant_pali_2"] = ""
df_0020["sbs_chant_eng_2"] = ""
df_0020["sbs_chapter_2"] = ""

df_0020["sbs_source_3"] = df_0020["new-sbs_source_3"]
df_0020["sbs_sutta_3"] = df_0020["new-sbs_sutta_3"]
df_0020["sbs_example_3"] = df_0020["new-sbs_example_3"]
df_0020["sbs_chant_pali_3"] = df_0020["new-sbs_chant_pali_3"]
df_0020["sbs_chant_eng_3"] = df_0020["new-sbs_chant_eng_3"]
df_0020["sbs_chapter_3"] = df_0020["new-sbs_chapter_3"]


df_0020 = df_0020[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0020)

# df_0020.to_csv("../spreadsheets/df_0020.csv", sep="\t", index=None)


# filtering 0021

test1 = df['move'] == '0021'
filter = test1
df_0021 = df.loc[filter]

df_0021["new-sbs_source_3"] = df_0021["source_2"]
df_0021["new-sbs_sutta_3"] = df_0021["sutta_2"]
df_0021["new-sbs_example_3"] = df_0021["example_2"]
df_0021["new-sbs_chant_pali_3"] = df_0021["sbs_chant_pali_2"]
df_0021["new-sbs_chant_eng_3"] = df_0021["sbs_chant_eng_2"]
df_0021["new-sbs_chapter_3"] = df_0021["sbs_chapter_2"]

df_0021["source_2"] = ""
df_0021["sutta_2"] = ""
df_0021["example_2"] = ""
df_0021["sbs_chant_pali_2"] = ""
df_0021["sbs_chant_eng_2"] = ""
df_0021["sbs_chapter_2"] = ""

df_0021["new-sbs_source_4"] = df_0021["source_1"]
df_0021["new-sbs_sutta_4"] = df_0021["sutta_1"]
df_0021["new-sbs_example_4"] = df_0021["example_1"]
df_0021["new-sbs_chant_pali_4"] = df_0021["sbs_chant_pali_1"]
df_0021["new-sbs_chant_eng_4"] = df_0021["sbs_chant_eng_1"]
df_0021["new-sbs_chapter_4"] = df_0021["sbs_chapter_1"]

df_0021["source_1"] = ""
df_0021["sutta_1"] = ""
df_0021["example_1"] = ""
df_0021["sbs_chant_pali_1"] = ""
df_0021["sbs_chant_eng_1"] = ""
df_0021["sbs_chapter_1"] = ""

df_0021["sbs_source_4"] = df_0021["new-sbs_source_4"]
df_0021["sbs_sutta_4"] = df_0021["new-sbs_sutta_4"]
df_0021["sbs_example_4"] = df_0021["new-sbs_example_4"]
df_0021["sbs_chant_pali_4"] = df_0021["new-sbs_chant_pali_4"]
df_0021["sbs_chant_eng_4"] = df_0021["new-sbs_chant_eng_4"]
df_0021["sbs_chapter_4"] = df_0021["new-sbs_chapter_4"]

df_0021["sbs_source_3"] = df_0021["new-sbs_source_3"]
df_0021["sbs_sutta_3"] = df_0021["new-sbs_sutta_3"]
df_0021["sbs_example_3"] = df_0021["new-sbs_example_3"]
df_0021["sbs_chant_pali_3"] = df_0021["new-sbs_chant_pali_3"]
df_0021["sbs_chant_eng_3"] = df_0021["new-sbs_chant_eng_3"]
df_0021["sbs_chapter_3"] = df_0021["new-sbs_chapter_3"]


df_0021 = df_0021[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]
# print(df_0021)

# df_0021.to_csv("../spreadsheets/df_0021.csv", sep="\t", index=None)

# filtering 0023

test1 = df['move'] == '0023'
filter = test1
df_0023 = df.loc[filter]

df_0023["new-sbs_source_3"] = df_0023["source_2"]
df_0023["new-sbs_sutta_3"] = df_0023["sutta_2"]
df_0023["new-sbs_example_3"] = df_0023["example_2"]
df_0023["new-sbs_chant_pali_3"] = df_0023["sbs_chant_pali_2"]
df_0023["new-sbs_chant_eng_3"] = df_0023["sbs_chant_eng_2"]
df_0023["new-sbs_chapter_3"] = df_0023["sbs_chapter_2"]

df_0023["source_2"] = ""
df_0023["sutta_2"] = ""
df_0023["example_2"] = ""
df_0023["sbs_chant_pali_2"] = ""
df_0023["sbs_chant_eng_2"] = ""
df_0023["sbs_chapter_2"] = ""

df_0023["new-sbs_source_4"] = df_0023["sbs_source_3"]
df_0023["new-sbs_sutta_4"] = df_0023["sbs_sutta_3"]
df_0023["new-sbs_example_4"] = df_0023["sbs_example_3"]
df_0023["new-sbs_chant_pali_4"] = df_0023["sbs_chant_pali_3"]
df_0023["new-sbs_chant_eng_4"] = df_0023["sbs_chant_eng_3"]
df_0023["new-sbs_chapter_4"] = df_0023["sbs_chapter_3"]

df_0023["sbs_source_3"] = ""
df_0023["sbs_sutta_3"] = ""
df_0023["sbs_example_3"] = ""
df_0023["sbs_chant_pali_3"] = ""
df_0023["sbs_chant_eng_3"] = ""
df_0023["sbs_chapter_3"] = ""

df_0023["sbs_source_4"] = df_0023["new-sbs_source_4"]
df_0023["sbs_sutta_4"] = df_0023["new-sbs_sutta_4"]
df_0023["sbs_example_4"] = df_0023["new-sbs_example_4"]
df_0023["sbs_chant_pali_4"] = df_0023["new-sbs_chant_pali_4"]
df_0023["sbs_chant_eng_4"] = df_0023["new-sbs_chant_eng_4"]
df_0023["sbs_chapter_4"] = df_0023["new-sbs_chapter_4"]

df_0023["sbs_source_3"] = df_0023["new-sbs_source_3"]
df_0023["sbs_sutta_3"] = df_0023["new-sbs_sutta_3"]
df_0023["sbs_example_3"] = df_0023["new-sbs_example_3"]
df_0023["sbs_chant_pali_3"] = df_0023["new-sbs_chant_pali_3"]
df_0023["sbs_chant_eng_3"] = df_0023["new-sbs_chant_eng_3"]
df_0023["sbs_chapter_3"] = df_0023["new-sbs_chapter_3"]


df_0023 = df_0023[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]
# print(df_0023)

# df_0023.to_csv("../spreadsheets/df_0023.csv", sep="\t", index=None)


# filtering 0100

test1 = df['move'] == '0100'
filter = test1
df_0100 = df.loc[filter]

df_0100["new-source_2"] = df_0100["source_1"]
df_0100["new-sutta_2"] = df_0100["sutta_1"]
df_0100["new-example_2"] = df_0100["example_1"]
df_0100["new-sbs_chant_pali_2"] = df_0100["sbs_chant_pali_1"]
df_0100["new-sbs_chant_eng_2"] = df_0100["sbs_chant_eng_1"]
df_0100["new-sbs_chapter_2"] = df_0100["sbs_chapter_1"]

df_0100["source_1"] = ""
df_0100["sutta_1"] = ""
df_0100["example_1"] = ""
df_0100["sbs_chant_pali_1"] = ""
df_0100["sbs_chant_eng_1"] = ""
df_0100["sbs_chapter_1"] = ""

df_0100["source_2"] = df_0100["new-source_2"]
df_0100["sutta_2"] = df_0100["new-sutta_2"]
df_0100["example_2"] = df_0100["new-example_2"]
df_0100["sbs_chant_pali_2"] = df_0100["new-sbs_chant_pali_2"]
df_0100["sbs_chant_eng_2"] = df_0100["new-sbs_chant_eng_2"]
df_0100["sbs_chapter_2"] = df_0100["new-sbs_chapter_2"]


df_0100 = df_0100[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0100)

# df_0100.to_csv("../spreadsheets/df_0100.csv", sep="\t", index=None)

# filtering 0102

test1 = df['move'] == '0102'
filter = test1
df_0102 = df.loc[filter]

df_0102["new-source_2"] = df_0102["source_1"]
df_0102["new-sutta_2"] = df_0102["sutta_1"]
df_0102["new-example_2"] = df_0102["example_1"]
df_0102["new-sbs_chant_pali_2"] = df_0102["sbs_chant_pali_1"]
df_0102["new-sbs_chant_eng_2"] = df_0102["sbs_chant_eng_1"]
df_0102["new-sbs_chapter_2"] = df_0102["sbs_chapter_1"]

df_0102["source_1"] = ""
df_0102["sutta_1"] = ""
df_0102["example_1"] = ""
df_0102["sbs_chant_pali_1"] = ""
df_0102["sbs_chant_eng_1"] = ""
df_0102["sbs_chapter_1"] = ""

df_0102["new-sbs_source_4"] = df_0102["source_2"]
df_0102["new-sbs_sutta_4"] = df_0102["sutta_2"]
df_0102["new-sbs_example_4"] = df_0102["example_2"]
df_0102["new-sbs_chant_pali_4"] = df_0102["sbs_chant_pali_2"]
df_0102["new-sbs_chant_eng_4"] = df_0102["sbs_chant_eng_2"]
df_0102["new-sbs_chapter_4"] = df_0102["sbs_chapter_2"]

df_0102["source_2"] = ""
df_0102["sutta_2"] = ""
df_0102["example_2"] = ""
df_0102["sbs_chant_pali_2"] = ""
df_0102["sbs_chant_eng_2"] = ""
df_0102["sbs_chapter_2"] = ""

df_0102["sbs_source_4"] = df_0102["new-sbs_source_4"]
df_0102["sbs_sutta_4"] = df_0102["new-sbs_sutta_4"]
df_0102["sbs_example_4"] = df_0102["new-sbs_example_4"]
df_0102["sbs_chant_pali_4"] = df_0102["new-sbs_chant_pali_4"]
df_0102["sbs_chant_eng_4"] = df_0102["new-sbs_chant_eng_4"]
df_0102["sbs_chapter_4"] = df_0102["new-sbs_chapter_4"]

df_0102["source_2"] = df_0102["new-source_2"]
df_0102["sutta_2"] = df_0102["new-sutta_2"]
df_0102["example_2"] = df_0102["new-example_2"]
df_0102["sbs_chant_pali_2"] = df_0102["new-sbs_chant_pali_2"]
df_0102["sbs_chant_eng_2"] = df_0102["new-sbs_chant_eng_2"]
df_0102["sbs_chapter_2"] = df_0102["new-sbs_chapter_2"]


df_0102 = df_0102[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0102)

# df_0102.to_csv("../spreadsheets/df_0102.csv", sep="\t", index=None)

# filtering 0120

test1 = df['move'] == '0120'
filter = test1
df_0120 = df.loc[filter]

df_0120["new-source_2"] = df_0120["source_1"]
df_0120["new-sutta_2"] = df_0120["sutta_1"]
df_0120["new-example_2"] = df_0120["example_1"]
df_0120["new-sbs_chant_pali_2"] = df_0120["sbs_chant_pali_1"]
df_0120["new-sbs_chant_eng_2"] = df_0120["sbs_chant_eng_1"]
df_0120["new-sbs_chapter_2"] = df_0120["sbs_chapter_1"]

df_0120["source_1"] = ""
df_0120["sutta_1"] = ""
df_0120["example_1"] = ""
df_0120["sbs_chant_pali_1"] = ""
df_0120["sbs_chant_eng_1"] = ""
df_0120["sbs_chapter_1"] = ""

df_0120["new-sbs_source_3"] = df_0120["source_2"]
df_0120["new-sbs_sutta_3"] = df_0120["sutta_2"]
df_0120["new-sbs_example_3"] = df_0120["example_2"]
df_0120["new-sbs_chant_pali_3"] = df_0120["sbs_chant_pali_2"]
df_0120["new-sbs_chant_eng_3"] = df_0120["sbs_chant_eng_2"]
df_0120["new-sbs_chapter_3"] = df_0120["sbs_chapter_2"]

df_0120["source_2"] = ""
df_0120["sutta_2"] = ""
df_0120["example_2"] = ""
df_0120["sbs_chant_pali_2"] = ""
df_0120["sbs_chant_eng_2"] = ""
df_0120["sbs_chapter_2"] = ""

df_0120["sbs_source_3"] = df_0120["new-sbs_source_3"]
df_0120["sbs_sutta_3"] = df_0120["new-sbs_sutta_3"]
df_0120["sbs_example_3"] = df_0120["new-sbs_example_3"]
df_0120["sbs_chant_pali_3"] = df_0120["new-sbs_chant_pali_3"]
df_0120["sbs_chant_eng_3"] = df_0120["new-sbs_chant_eng_3"]
df_0120["sbs_chapter_3"] = df_0120["new-sbs_chapter_3"]

df_0120["source_2"] = df_0120["new-source_2"]
df_0120["sutta_2"] = df_0120["new-sutta_2"]
df_0120["example_2"] = df_0120["new-example_2"]
df_0120["sbs_chant_pali_2"] = df_0120["new-sbs_chant_pali_2"]
df_0120["sbs_chant_eng_2"] = df_0120["new-sbs_chant_eng_2"]
df_0120["sbs_chapter_2"] = df_0120["new-sbs_chapter_2"]


df_0120 = df_0120[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0120)

# df_0120.to_csv("../spreadsheets/df_0120.csv", sep="\t", index=None)

# filtering 0123

test1 = df['move'] == '0123'
filter = test1
df_0123 = df.loc[filter]

df_0123["new-source_2"] = df_0123["source_1"]
df_0123["new-sutta_2"] = df_0123["sutta_1"]
df_0123["new-example_2"] = df_0123["example_1"]
df_0123["new-sbs_chant_pali_2"] = df_0123["sbs_chant_pali_1"]
df_0123["new-sbs_chant_eng_2"] = df_0123["sbs_chant_eng_1"]
df_0123["new-sbs_chapter_2"] = df_0123["sbs_chapter_1"]

df_0123["source_1"] = ""
df_0123["sutta_1"] = ""
df_0123["example_1"] = ""
df_0123["sbs_chant_pali_1"] = ""
df_0123["sbs_chant_eng_1"] = ""
df_0123["sbs_chapter_1"] = ""

df_0123["new-sbs_source_3"] = df_0123["source_2"]
df_0123["new-sbs_sutta_3"] = df_0123["sutta_2"]
df_0123["new-sbs_example_3"] = df_0123["example_2"]
df_0123["new-sbs_chant_pali_3"] = df_0123["sbs_chant_pali_2"]
df_0123["new-sbs_chant_eng_3"] = df_0123["sbs_chant_eng_2"]
df_0123["new-sbs_chapter_3"] = df_0123["sbs_chapter_2"]

df_0123["source_2"] = ""
df_0123["sutta_2"] = ""
df_0123["example_2"] = ""
df_0123["sbs_chant_pali_2"] = ""
df_0123["sbs_chant_eng_2"] = ""
df_0123["sbs_chapter_2"] = ""

df_0123["new-sbs_source_4"] = df_0123["sbs_source_3"]
df_0123["new-sbs_sutta_4"] = df_0123["sbs_sutta_3"]
df_0123["new-sbs_example_4"] = df_0123["sbs_example_3"]
df_0123["new-sbs_chant_pali_4"] = df_0123["sbs_chant_pali_3"]
df_0123["new-sbs_chant_eng_4"] = df_0123["sbs_chant_eng_3"]
df_0123["new-sbs_chapter_4"] = df_0123["sbs_chapter_3"]

df_0123["sbs_source_3"] = ""
df_0123["sbs_sutta_3"] = ""
df_0123["sbs_example_3"] = ""
df_0123["sbs_chant_pali_3"] = ""
df_0123["sbs_chant_eng_3"] = ""
df_0123["sbs_chapter_3"] = ""

df_0123["sbs_source_4"] = df_0123["new-sbs_source_4"]
df_0123["sbs_sutta_4"] = df_0123["new-sbs_sutta_4"]
df_0123["sbs_example_4"] = df_0123["new-sbs_example_4"]
df_0123["sbs_chant_pali_4"] = df_0123["new-sbs_chant_pali_4"]
df_0123["sbs_chant_eng_4"] = df_0123["new-sbs_chant_eng_4"]
df_0123["sbs_chapter_4"] = df_0123["new-sbs_chapter_4"]

df_0123["sbs_source_3"] = df_0123["new-sbs_source_3"]
df_0123["sbs_sutta_3"] = df_0123["new-sbs_sutta_3"]
df_0123["sbs_example_3"] = df_0123["new-sbs_example_3"]
df_0123["sbs_chant_pali_3"] = df_0123["new-sbs_chant_pali_3"]
df_0123["sbs_chant_eng_3"] = df_0123["new-sbs_chant_eng_3"]
df_0123["sbs_chapter_3"] = df_0123["new-sbs_chapter_3"]

df_0123["source_2"] = df_0123["new-source_2"]
df_0123["sutta_2"] = df_0123["new-sutta_2"]
df_0123["example_2"] = df_0123["new-example_2"]
df_0123["sbs_chant_pali_2"] = df_0123["new-sbs_chant_pali_2"]
df_0123["sbs_chant_eng_2"] = df_0123["new-sbs_chant_eng_2"]
df_0123["sbs_chapter_2"] = df_0123["new-sbs_chapter_2"]

df_0123 = df_0123[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0123)

# df_0123.to_csv("../spreadsheets/df_0123.csv", sep="\t", index=None)

# filtering 0300

test1 = df['move'] == '0300'
filter = test1
df_0300 = df.loc[filter]

df_0300["new-source_2"] = df_0300["sbs_source_3"]
df_0300["new-sutta_2"] = df_0300["sbs_sutta_3"]
df_0300["new-example_2"] = df_0300["sbs_example_3"]
df_0300["new-sbs_chant_pali_2"] = df_0300["sbs_chant_pali_3"]
df_0300["new-sbs_chant_eng_2"] = df_0300["sbs_chant_eng_3"]
df_0300["new-sbs_chapter_2"] = df_0300["sbs_chapter_3"]

df_0300["sbs_source_3"] = ""
df_0300["sbs_sutta_3"] = ""
df_0300["sbs_example_3"] = ""
df_0300["sbs_chant_pali_3"] = ""
df_0300["sbs_chant_eng_3"] = ""
df_0300["sbs_chapter_3"] = ""

df_0300["source_2"] = df_0300["new-source_2"]
df_0300["sutta_2"] = df_0300["new-sutta_2"]
df_0300["example_2"] = df_0300["new-example_2"]
df_0300["sbs_chant_pali_2"] = df_0300["new-sbs_chant_pali_2"]
df_0300["sbs_chant_eng_2"] = df_0300["new-sbs_chant_eng_2"]
df_0300["sbs_chapter_2"] = df_0300["new-sbs_chapter_2"]


df_0300 = df_0300[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0300)

# df_0300.to_csv("../spreadsheets/df_0300.csv", sep="\t", index=None)

# filtering 0310

test1 = df['move'] == '0310'
filter = test1
df_0310 = df.loc[filter]

df_0310["new-source_2"] = df_0310["sbs_source_3"]
df_0310["new-sutta_2"] = df_0310["sbs_sutta_3"]
df_0310["new-example_2"] = df_0310["sbs_example_3"]
df_0310["new-sbs_chant_pali_2"] = df_0310["sbs_chant_pali_3"]
df_0310["new-sbs_chant_eng_2"] = df_0310["sbs_chant_eng_3"]
df_0310["new-sbs_chapter_2"] = df_0310["sbs_chapter_3"]

df_0310["sbs_source_3"] = ""
df_0310["sbs_sutta_3"] = ""
df_0310["sbs_example_3"] = ""
df_0310["sbs_chant_pali_3"] = ""
df_0310["sbs_chant_eng_3"] = ""
df_0310["sbs_chapter_3"] = ""

df_0310["new-sbs_source_3"] = df_0310["source_1"]
df_0310["new-sbs_sutta_3"] = df_0310["sutta_1"]
df_0310["new-sbs_example_3"] = df_0310["example_1"]
df_0310["new-sbs_chant_pali_3"] = df_0310["sbs_chant_pali_1"]
df_0310["new-sbs_chant_eng_3"] = df_0310["sbs_chant_eng_1"]
df_0310["new-sbs_chapter_3"] = df_0310["sbs_chapter_1"]

df_0310["source_1"] = ""
df_0310["sutta_1"] = ""
df_0310["example_1"] = ""
df_0310["sbs_chant_pali_1"] = ""
df_0310["sbs_chant_eng_1"] = ""
df_0310["sbs_chapter_1"] = ""

df_0310["sbs_source_3"] = df_0310["new-sbs_source_3"]
df_0310["sbs_sutta_3"] = df_0310["new-sbs_sutta_3"]
df_0310["sbs_example_3"] = df_0310["new-sbs_example_3"]
df_0310["sbs_chant_pali_3"] = df_0310["new-sbs_chant_pali_3"]
df_0310["sbs_chant_eng_3"] = df_0310["new-sbs_chant_eng_3"]
df_0310["sbs_chapter_3"] = df_0310["new-sbs_chapter_3"]

df_0310["source_2"] = df_0310["new-source_2"]
df_0310["sutta_2"] = df_0310["new-sutta_2"]
df_0310["example_2"] = df_0310["new-example_2"]
df_0310["sbs_chant_pali_2"] = df_0310["new-sbs_chant_pali_2"]
df_0310["sbs_chant_eng_2"] = df_0310["new-sbs_chant_eng_2"]
df_0310["sbs_chapter_2"] = df_0310["new-sbs_chapter_2"]


df_0310 = df_0310[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0310)

# df_0310.to_csv("../spreadsheets/df_0310.csv", sep="\t", index=None)

# filtering 0312

test1 = df['move'] == '0312'
filter = test1
df_0312 = df.loc[filter]

df_0312["new-source_2"] = df_0312["sbs_source_3"]
df_0312["new-sutta_2"] = df_0312["sbs_sutta_3"]
df_0312["new-example_2"] = df_0312["sbs_example_3"]
df_0312["new-sbs_chant_pali_2"] = df_0312["sbs_chant_pali_3"]
df_0312["new-sbs_chant_eng_2"] = df_0312["sbs_chant_eng_3"]
df_0312["new-sbs_chapter_2"] = df_0312["sbs_chapter_3"]

df_0312["sbs_source_3"] = ""
df_0312["sbs_sutta_3"] = ""
df_0312["sbs_example_3"] = ""
df_0312["sbs_chant_pali_3"] = ""
df_0312["sbs_chant_eng_3"] = ""
df_0312["sbs_chapter_3"] = ""

df_0312["new-sbs_source_3"] = df_0312["source_1"]
df_0312["new-sbs_sutta_3"] = df_0312["sutta_1"]
df_0312["new-sbs_example_3"] = df_0312["example_1"]
df_0312["new-sbs_chant_pali_3"] = df_0312["sbs_chant_pali_1"]
df_0312["new-sbs_chant_eng_3"] = df_0312["sbs_chant_eng_1"]
df_0312["new-sbs_chapter_3"] = df_0312["sbs_chapter_1"]

df_0312["source_1"] = ""
df_0312["sutta_1"] = ""
df_0312["example_1"] = ""
df_0312["sbs_chant_pali_1"] = ""
df_0312["sbs_chant_eng_1"] = ""
df_0312["sbs_chapter_1"] = ""

df_0312["new-sbs_source_4"] = df_0312["source_2"]
df_0312["new-sbs_sutta_4"] = df_0312["sutta_2"]
df_0312["new-sbs_example_4"] = df_0312["example_2"]
df_0312["new-sbs_chant_pali_4"] = df_0312["sbs_chant_pali_2"]
df_0312["new-sbs_chant_eng_4"] = df_0312["sbs_chant_eng_2"]
df_0312["new-sbs_chapter_4"] = df_0312["sbs_chapter_2"]

df_0312["source_2"] = ""
df_0312["sutta_2"] = ""
df_0312["example_2"] = ""
df_0312["sbs_chant_pali_2"] = ""
df_0312["sbs_chant_eng_2"] = ""
df_0312["sbs_chapter_2"] = ""

df_0312["sbs_source_4"] = df_0312["new-sbs_source_4"]
df_0312["sbs_sutta_4"] = df_0312["new-sbs_sutta_4"]
df_0312["sbs_example_4"] = df_0312["new-sbs_example_4"]
df_0312["sbs_chant_pali_4"] = df_0312["new-sbs_chant_pali_4"]
df_0312["sbs_chant_eng_4"] = df_0312["new-sbs_chant_eng_4"]
df_0312["sbs_chapter_4"] = df_0312["new-sbs_chapter_4"]

df_0312["sbs_source_3"] = df_0312["new-sbs_source_3"]
df_0312["sbs_sutta_3"] = df_0312["new-sbs_sutta_3"]
df_0312["sbs_example_3"] = df_0312["new-sbs_example_3"]
df_0312["sbs_chant_pali_3"] = df_0312["new-sbs_chant_pali_3"]
df_0312["sbs_chant_eng_3"] = df_0312["new-sbs_chant_eng_3"]
df_0312["sbs_chapter_3"] = df_0312["new-sbs_chapter_3"]

df_0312["source_2"] = df_0312["new-source_2"]
df_0312["sutta_2"] = df_0312["new-sutta_2"]
df_0312["example_2"] = df_0312["new-example_2"]
df_0312["sbs_chant_pali_2"] = df_0312["new-sbs_chant_pali_2"]
df_0312["sbs_chant_eng_2"] = df_0312["new-sbs_chant_eng_2"]
df_0312["sbs_chapter_2"] = df_0312["new-sbs_chapter_2"]

df_0312 = df_0312[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0312)

# df_0312.to_csv("../spreadsheets/df_0312.csv", sep="\t", index=None)


# filtering 0320

test1 = df['move'] == '0320'
filter = test1
df_0320 = df.loc[filter]

df_0320["new-source_2"] = df_0320["sbs_source_3"]
df_0320["new-sutta_2"] = df_0320["sbs_sutta_3"]
df_0320["new-example_2"] = df_0320["sbs_example_3"]
df_0320["new-sbs_chant_pali_2"] = df_0320["sbs_chant_pali_3"]
df_0320["new-sbs_chant_eng_2"] = df_0320["sbs_chant_eng_3"]
df_0320["new-sbs_chapter_2"] = df_0320["sbs_chapter_3"]

df_0320["sbs_source_3"] = ""
df_0320["sbs_sutta_3"] = ""
df_0320["sbs_example_3"] = ""
df_0320["sbs_chant_pali_3"] = ""
df_0320["sbs_chant_eng_3"] = ""
df_0320["sbs_chapter_3"] = ""

df_0320["new-sbs_source_3"] = df_0320["source_2"]
df_0320["new-sbs_sutta_3"] = df_0320["sutta_2"]
df_0320["new-sbs_example_3"] = df_0320["example_2"]
df_0320["new-sbs_chant_pali_3"] = df_0320["sbs_chant_pali_2"]
df_0320["new-sbs_chant_eng_3"] = df_0320["sbs_chant_eng_2"]
df_0320["new-sbs_chapter_3"] = df_0320["sbs_chapter_2"]

df_0320["source_2"] = ""
df_0320["sutta_2"] = ""
df_0320["example_2"] = ""
df_0320["sbs_chant_pali_2"] = ""
df_0320["sbs_chant_eng_2"] = ""
df_0320["sbs_chapter_2"] = ""

df_0320["sbs_source_3"] = df_0320["new-sbs_source_3"]
df_0320["sbs_sutta_3"] = df_0320["new-sbs_sutta_3"]
df_0320["sbs_example_3"] = df_0320["new-sbs_example_3"]
df_0320["sbs_chant_pali_3"] = df_0320["new-sbs_chant_pali_3"]
df_0320["sbs_chant_eng_3"] = df_0320["new-sbs_chant_eng_3"]
df_0320["sbs_chapter_3"] = df_0320["new-sbs_chapter_3"]

df_0320["source_2"] = df_0320["new-source_2"]
df_0320["sutta_2"] = df_0320["new-sutta_2"]
df_0320["example_2"] = df_0320["new-example_2"]
df_0320["sbs_chant_pali_2"] = df_0320["new-sbs_chant_pali_2"]
df_0320["sbs_chant_eng_2"] = df_0320["new-sbs_chant_eng_2"]
df_0320["sbs_chapter_2"] = df_0320["new-sbs_chapter_2"]


df_0320 = df_0320[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0320)

# df_0320.to_csv("../spreadsheets/df_0320.csv", sep="\t", index=None)


# filtering 0400

test1 = df['move'] == '0400'
filter = test1
df_0400 = df.loc[filter]

df_0400["new-source_2"] = df_0400["sbs_source_4"]
df_0400["new-sutta_2"] = df_0400["sbs_sutta_4"]
df_0400["new-example_2"] = df_0400["sbs_example_4"]
df_0400["new-sbs_chant_pali_2"] = df_0400["sbs_chant_pali_4"]
df_0400["new-sbs_chant_eng_2"] = df_0400["sbs_chant_eng_4"]
df_0400["new-sbs_chapter_2"] = df_0400["sbs_chapter_4"]

df_0400["sbs_source_4"] = ""
df_0400["sbs_sutta_4"] = ""
df_0400["sbs_example_4"] = ""
df_0400["sbs_chant_pali_4"] = ""
df_0400["sbs_chant_eng_4"] = ""
df_0400["sbs_chapter_4"] = ""

df_0400["source_2"] = df_0400["new-source_2"]
df_0400["sutta_2"] = df_0400["new-sutta_2"]
df_0400["example_2"] = df_0400["new-example_2"]
df_0400["sbs_chant_pali_2"] = df_0400["new-sbs_chant_pali_2"]
df_0400["sbs_chant_eng_2"] = df_0400["new-sbs_chant_eng_2"]
df_0400["sbs_chapter_2"] = df_0400["new-sbs_chapter_2"]


df_0400 = df_0400[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0400)

# df_0400.to_csv("../spreadsheets/df_0400.csv", sep="\t", index=None)


# filtering 0402

test1 = df['move'] == '0402'
filter = test1
df_0402 = df.loc[filter]

df_0402["new-source_2"] = df_0402["sbs_source_4"]
df_0402["new-sutta_2"] = df_0402["sbs_sutta_4"]
df_0402["new-example_2"] = df_0402["sbs_example_4"]
df_0402["new-sbs_chant_pali_2"] = df_0402["sbs_chant_pali_4"]
df_0402["new-sbs_chant_eng_2"] = df_0402["sbs_chant_eng_4"]
df_0402["new-sbs_chapter_2"] = df_0402["sbs_chapter_4"]

df_0402["sbs_source_4"] = ""
df_0402["sbs_sutta_4"] = ""
df_0402["sbs_example_4"] = ""
df_0402["sbs_chant_pali_4"] = ""
df_0402["sbs_chant_eng_4"] = ""
df_0402["sbs_chapter_4"] = ""

df_0402["new-sbs_source_4"] = df_0402["source_2"]
df_0402["new-sbs_sutta_4"] = df_0402["sutta_2"]
df_0402["new-sbs_example_4"] = df_0402["example_2"]
df_0402["new-sbs_chant_pali_4"] = df_0402["sbs_chant_pali_2"]
df_0402["new-sbs_chant_eng_4"] = df_0402["sbs_chant_eng_2"]
df_0402["new-sbs_chapter_4"] = df_0402["sbs_chapter_2"]

df_0402["source_2"] = ""
df_0402["sutta_2"] = ""
df_0402["example_2"] = ""
df_0402["sbs_chant_pali_2"] = ""
df_0402["sbs_chant_eng_2"] = ""
df_0402["sbs_chapter_2"] = ""

df_0402["sbs_source_4"] = df_0402["new-sbs_source_4"]
df_0402["sbs_sutta_4"] = df_0402["new-sbs_sutta_4"]
df_0402["sbs_example_4"] = df_0402["new-sbs_example_4"]
df_0402["sbs_chant_pali_4"] = df_0402["new-sbs_chant_pali_4"]
df_0402["sbs_chant_eng_4"] = df_0402["new-sbs_chant_eng_4"]
df_0402["sbs_chapter_4"] = df_0402["new-sbs_chapter_4"]

df_0402["source_2"] = df_0402["new-source_2"]
df_0402["sutta_2"] = df_0402["new-sutta_2"]
df_0402["example_2"] = df_0402["new-example_2"]
df_0402["sbs_chant_pali_2"] = df_0402["new-sbs_chant_pali_2"]
df_0402["sbs_chant_eng_2"] = df_0402["new-sbs_chant_eng_2"]
df_0402["sbs_chapter_2"] = df_0402["new-sbs_chapter_2"]


df_0402 = df_0402[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_0402)

# df_0402.to_csv("../spreadsheets/df_0402.csv", sep="\t", index=None)


# filtering 2000

test1 = df['move'] == '2000'
filter = test1
df_2000 = df.loc[filter]

df_2000["new-source_1"] = df_2000["source_2"]
df_2000["new-sutta_1"] = df_2000["sutta_2"]
df_2000["new-example_1"] = df_2000["example_2"]
df_2000["new-sbs_chant_pali_1"] = df_2000["sbs_chant_pali_2"]
df_2000["new-sbs_chant_eng_1"] = df_2000["sbs_chant_eng_2"]
df_2000["new-sbs_chapter_1"] = df_2000["sbs_chapter_2"]

df_2000["source_2"] = ""
df_2000["sutta_2"] = ""
df_2000["example_2"] = ""
df_2000["sbs_chant_pali_2"] = ""
df_2000["sbs_chant_eng_2"] = ""
df_2000["sbs_chapter_2"] = ""

df_2000["source_1"] = df_2000["new-source_1"]
df_2000["sutta_1"] = df_2000["new-sutta_1"]
df_2000["example_1"] = df_2000["new-example_1"]
df_2000["sbs_chant_pali_1"] = df_2000["new-sbs_chant_pali_1"]
df_2000["sbs_chant_eng_1"] = df_2000["new-sbs_chant_eng_1"]
df_2000["sbs_chapter_1"] = df_2000["new-sbs_chapter_1"]


df_2000 = df_2000[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_2000)

# df_2000.to_csv("../spreadsheets/df_2000.csv", sep="\t", index=None)


# filtering 2001

test1 = df['move'] == '2001'
filter = test1
df_2001 = df.loc[filter]

df_2001["new-source_1"] = df_2001["source_2"]
df_2001["new-sutta_1"] = df_2001["sutta_2"]
df_2001["new-example_1"] = df_2001["example_2"]
df_2001["new-sbs_chant_pali_1"] = df_2001["sbs_chant_pali_2"]
df_2001["new-sbs_chant_eng_1"] = df_2001["sbs_chant_eng_2"]
df_2001["new-sbs_chapter_1"] = df_2001["sbs_chapter_2"]

df_2001["source_2"] = ""
df_2001["sutta_2"] = ""
df_2001["example_2"] = ""
df_2001["sbs_chant_pali_2"] = ""
df_2001["sbs_chant_eng_2"] = ""
df_2001["sbs_chapter_2"] = ""

df_2001["new-sbs_source_4"] = df_2001["source_1"]
df_2001["new-sbs_sutta_4"] = df_2001["sutta_1"]
df_2001["new-sbs_example_4"] = df_2001["example_1"]
df_2001["new-sbs_chant_pali_4"] = df_2001["sbs_chant_pali_1"]
df_2001["new-sbs_chant_eng_4"] = df_2001["sbs_chant_eng_1"]
df_2001["new-sbs_chapter_4"] = df_2001["sbs_chapter_1"]

df_2001["source_1"] = ""
df_2001["sutta_1"] = ""
df_2001["example_1"] = ""
df_2001["sbs_chant_pali_1"] = ""
df_2001["sbs_chant_eng_1"] = ""
df_2001["sbs_chapter_1"] = ""

df_2001["sbs_source_4"] = df_2001["new-sbs_source_4"]
df_2001["sbs_sutta_4"] = df_2001["new-sbs_sutta_4"]
df_2001["sbs_example_4"] = df_2001["new-sbs_example_4"]
df_2001["sbs_chant_pali_4"] = df_2001["new-sbs_chant_pali_4"]
df_2001["sbs_chant_eng_4"] = df_2001["new-sbs_chant_eng_4"]
df_2001["sbs_chapter_4"] = df_2001["new-sbs_chapter_4"]

df_2001["source_1"] = df_2001["new-source_1"]
df_2001["sutta_1"] = df_2001["new-sutta_1"]
df_2001["example_1"] = df_2001["new-example_1"]
df_2001["sbs_chant_pali_1"] = df_2001["new-sbs_chant_pali_1"]
df_2001["sbs_chant_eng_1"] = df_2001["new-sbs_chant_eng_1"]
df_2001["sbs_chapter_1"] = df_2001["new-sbs_chapter_1"]

df_2001 = df_2001[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_2001)

# df_2001.to_csv("../spreadsheets/df_2001.csv", sep="\t", index=None)

# filtering 2010

test1 = df['move'] == '2010'
filter = test1
df_2010 = df.loc[filter]

df_2010["new-source_1"] = df_2010["source_2"]
df_2010["new-sutta_1"] = df_2010["sutta_2"]
df_2010["new-example_1"] = df_2010["example_2"]
df_2010["new-sbs_chant_pali_1"] = df_2010["sbs_chant_pali_2"]
df_2010["new-sbs_chant_eng_1"] = df_2010["sbs_chant_eng_2"]
df_2010["new-sbs_chapter_1"] = df_2010["sbs_chapter_2"]

df_2010["source_2"] = ""
df_2010["sutta_2"] = ""
df_2010["example_2"] = ""
df_2010["sbs_chant_pali_2"] = ""
df_2010["sbs_chant_eng_2"] = ""
df_2010["sbs_chapter_2"] = ""

df_2010["new-sbs_source_3"] = df_2010["source_1"]
df_2010["new-sbs_sutta_3"] = df_2010["sutta_1"]
df_2010["new-sbs_example_3"] = df_2010["example_1"]
df_2010["new-sbs_chant_pali_3"] = df_2010["sbs_chant_pali_1"]
df_2010["new-sbs_chant_eng_3"] = df_2010["sbs_chant_eng_1"]
df_2010["new-sbs_chapter_3"] = df_2010["sbs_chapter_1"]

df_2010["source_1"] = ""
df_2010["sutta_1"] = ""
df_2010["example_1"] = ""
df_2010["sbs_chant_pali_1"] = ""
df_2010["sbs_chant_eng_1"] = ""
df_2010["sbs_chapter_1"] = ""

df_2010["sbs_source_3"] = df_2010["new-sbs_source_3"]
df_2010["sbs_sutta_3"] = df_2010["new-sbs_sutta_3"]
df_2010["sbs_example_3"] = df_2010["new-sbs_example_3"]
df_2010["sbs_chant_pali_3"] = df_2010["new-sbs_chant_pali_3"]
df_2010["sbs_chant_eng_3"] = df_2010["new-sbs_chant_eng_3"]
df_2010["sbs_chapter_3"] = df_2010["new-sbs_chapter_3"]

df_2010["source_1"] = df_2010["new-source_1"]
df_2010["sutta_1"] = df_2010["new-sutta_1"]
df_2010["example_1"] = df_2010["new-example_1"]
df_2010["sbs_chant_pali_1"] = df_2010["new-sbs_chant_pali_1"]
df_2010["sbs_chant_eng_1"] = df_2010["new-sbs_chant_eng_1"]
df_2010["sbs_chapter_1"] = df_2010["new-sbs_chapter_1"]

df_2010 = df_2010[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_2010)

# df_2010.to_csv("../spreadsheets/df_2010.csv", sep="\t", index=None)

# filtering 2013

test1 = df['move'] == '2013'
filter = test1
df_2013 = df.loc[filter]

df_2013["new-source_1"] = df_2013["source_2"]
df_2013["new-sutta_1"] = df_2013["sutta_2"]
df_2013["new-example_1"] = df_2013["example_2"]
df_2013["new-sbs_chant_pali_1"] = df_2013["sbs_chant_pali_2"]
df_2013["new-sbs_chant_eng_1"] = df_2013["sbs_chant_eng_2"]
df_2013["new-sbs_chapter_1"] = df_2013["sbs_chapter_2"]

df_2013["source_2"] = ""
df_2013["sutta_2"] = ""
df_2013["example_2"] = ""
df_2013["sbs_chant_pali_2"] = ""
df_2013["sbs_chant_eng_2"] = ""
df_2013["sbs_chapter_2"] = ""

df_2013["new-sbs_source_3"] = df_2013["source_1"]
df_2013["new-sbs_sutta_3"] = df_2013["sutta_1"]
df_2013["new-sbs_example_3"] = df_2013["example_1"]
df_2013["new-sbs_chant_pali_3"] = df_2013["sbs_chant_pali_1"]
df_2013["new-sbs_chant_eng_3"] = df_2013["sbs_chant_eng_1"]
df_2013["new-sbs_chapter_3"] = df_2013["sbs_chapter_1"]

df_2013["source_1"] = ""
df_2013["sutta_1"] = ""
df_2013["example_1"] = ""
df_2013["sbs_chant_pali_1"] = ""
df_2013["sbs_chant_eng_1"] = ""
df_2013["sbs_chapter_1"] = ""

df_2013["new-sbs_source_4"] = df_2013["sbs_source_3"]
df_2013["new-sbs_sutta_4"] = df_2013["sbs_sutta_3"]
df_2013["new-sbs_example_4"] = df_2013["sbs_example_3"]
df_2013["new-sbs_chant_pali_4"] = df_2013["sbs_chant_pali_3"]
df_2013["new-sbs_chant_eng_4"] = df_2013["sbs_chant_eng_3"]
df_2013["new-sbs_chapter_4"] = df_2013["sbs_chapter_3"]

df_2013["sbs_source_3"] = ""
df_2013["sbs_sutta_3"] = ""
df_2013["sbs_example_3"] = ""
df_2013["sbs_chant_pali_3"] = ""
df_2013["sbs_chant_eng_3"] = ""
df_2013["sbs_chapter_3"] = ""

df_2013["sbs_source_4"] = df_2013["new-sbs_source_4"]
df_2013["sbs_sutta_4"] = df_2013["new-sbs_sutta_4"]
df_2013["sbs_example_4"] = df_2013["new-sbs_example_4"]
df_2013["sbs_chant_pali_4"] = df_2013["new-sbs_chant_pali_4"]
df_2013["sbs_chant_eng_4"] = df_2013["new-sbs_chant_eng_4"]
df_2013["sbs_chapter_4"] = df_2013["new-sbs_chapter_4"]

df_2013["sbs_source_3"] = df_2013["new-sbs_source_3"]
df_2013["sbs_sutta_3"] = df_2013["new-sbs_sutta_3"]
df_2013["sbs_example_3"] = df_2013["new-sbs_example_3"]
df_2013["sbs_chant_pali_3"] = df_2013["new-sbs_chant_pali_3"]
df_2013["sbs_chant_eng_3"] = df_2013["new-sbs_chant_eng_3"]
df_2013["sbs_chapter_3"] = df_2013["new-sbs_chapter_3"]

df_2013["source_1"] = df_2013["new-source_1"]
df_2013["sutta_1"] = df_2013["new-sutta_1"]
df_2013["example_1"] = df_2013["new-example_1"]
df_2013["sbs_chant_pali_1"] = df_2013["new-sbs_chant_pali_1"]
df_2013["sbs_chant_eng_1"] = df_2013["new-sbs_chant_eng_1"]
df_2013["sbs_chapter_1"] = df_2013["new-sbs_chapter_1"]

df_2013 = df_2013[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_2013)

# df_2013.to_csv("../spreadsheets/df_2013.csv", sep="\t", index=None)

# filtering 2100

test1 = df['move'] == '2100'
filter = test1
df_2100 = df.loc[filter]

df_2100["new-source_1"] = df_2100["source_2"]
df_2100["new-sutta_1"] = df_2100["sutta_2"]
df_2100["new-example_1"] = df_2100["example_2"]
df_2100["new-sbs_chant_pali_1"] = df_2100["sbs_chant_pali_2"]
df_2100["new-sbs_chant_eng_1"] = df_2100["sbs_chant_eng_2"]
df_2100["new-sbs_chapter_1"] = df_2100["sbs_chapter_2"]

df_2100["source_2"] = ""
df_2100["sutta_2"] = ""
df_2100["example_2"] = ""
df_2100["sbs_chant_pali_2"] = ""
df_2100["sbs_chant_eng_2"] = ""
df_2100["sbs_chapter_2"] = ""

df_2100["new-source_2"] = df_2100["source_1"]
df_2100["new-sutta_2"] = df_2100["sutta_1"]
df_2100["new-example_2"] = df_2100["example_1"]
df_2100["new-sbs_chant_pali_2"] = df_2100["sbs_chant_pali_1"]
df_2100["new-sbs_chant_eng_2"] = df_2100["sbs_chant_eng_1"]
df_2100["new-sbs_chapter_2"] = df_2100["sbs_chapter_1"]

df_2100["source_1"] = ""
df_2100["sutta_1"] = ""
df_2100["example_1"] = ""
df_2100["sbs_chant_pali_1"] = ""
df_2100["sbs_chant_eng_1"] = ""
df_2100["sbs_chapter_1"] = ""

df_2100["source_2"] = df_2100["new-source_2"]
df_2100["sutta_2"] = df_2100["new-sutta_2"]
df_2100["example_2"] = df_2100["new-example_2"]
df_2100["sbs_chant_pali_2"] = df_2100["new-sbs_chant_pali_2"]
df_2100["sbs_chant_eng_2"] = df_2100["new-sbs_chant_eng_2"]
df_2100["sbs_chapter_2"] = df_2100["new-sbs_chapter_2"]

df_2100["source_1"] = df_2100["new-source_1"]
df_2100["sutta_1"] = df_2100["new-sutta_1"]
df_2100["example_1"] = df_2100["new-example_1"]
df_2100["sbs_chant_pali_1"] = df_2100["new-sbs_chant_pali_1"]
df_2100["sbs_chant_eng_1"] = df_2100["new-sbs_chant_eng_1"]
df_2100["sbs_chapter_1"] = df_2100["new-sbs_chapter_1"]

df_2100 = df_2100[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_2100)

# df_2100.to_csv("../spreadsheets/df_2100.csv", sep="\t", index=None)

# filtering 2300

test1 = df['move'] == '2300'
filter = test1
df_2300 = df.loc[filter]

df_2300["new-source_1"] = df_2300["source_2"]
df_2300["new-sutta_1"] = df_2300["sutta_2"]
df_2300["new-example_1"] = df_2300["example_2"]
df_2300["new-sbs_chant_pali_1"] = df_2300["sbs_chant_pali_2"]
df_2300["new-sbs_chant_eng_1"] = df_2300["sbs_chant_eng_2"]
df_2300["new-sbs_chapter_1"] = df_2300["sbs_chapter_2"]

df_2300["source_2"] = ""
df_2300["sutta_2"] = ""
df_2300["example_2"] = ""
df_2300["sbs_chant_pali_2"] = ""
df_2300["sbs_chant_eng_2"] = ""
df_2300["sbs_chapter_2"] = ""

df_2300["new-source_2"] = df_2300["sbs_source_3"]
df_2300["new-sutta_2"] = df_2300["sbs_sutta_3"]
df_2300["new-example_2"] = df_2300["sbs_example_3"]
df_2300["new-sbs_chant_pali_2"] = df_2300["sbs_chant_pali_3"]
df_2300["new-sbs_chant_eng_2"] = df_2300["sbs_chant_eng_3"]
df_2300["new-sbs_chapter_2"] = df_2300["sbs_chapter_3"]

df_2300["sbs_source_3"] = ""
df_2300["sbs_sutta_3"] = ""
df_2300["sbs_example_3"] = ""
df_2300["sbs_chant_pali_3"] = ""
df_2300["sbs_chant_eng_3"] = ""
df_2300["sbs_chapter_3"] = ""

df_2300["source_2"] = df_2300["new-source_2"]
df_2300["sutta_2"] = df_2300["new-sutta_2"]
df_2300["example_2"] = df_2300["new-example_2"]
df_2300["sbs_chant_pali_2"] = df_2300["new-sbs_chant_pali_2"]
df_2300["sbs_chant_eng_2"] = df_2300["new-sbs_chant_eng_2"]
df_2300["sbs_chapter_2"] = df_2300["new-sbs_chapter_2"]

df_2300["source_1"] = df_2300["new-source_1"]
df_2300["sutta_1"] = df_2300["new-sutta_1"]
df_2300["example_1"] = df_2300["new-example_1"]
df_2300["sbs_chant_pali_1"] = df_2300["new-sbs_chant_pali_1"]
df_2300["sbs_chant_eng_1"] = df_2300["new-sbs_chant_eng_1"]
df_2300["sbs_chapter_1"] = df_2300["new-sbs_chapter_1"]


df_2300 = df_2300[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_2300)

# df_2300.to_csv("../spreadsheets/df_2300.csv", sep="\t", index=None)


# filtering 3000

test1 = df['move'] == '3000'
filter = test1
df_3000 = df.loc[filter]

df_3000["new-source_1"] = df_3000["sbs_source_3"]
df_3000["new-sutta_1"] = df_3000["sbs_sutta_3"]
df_3000["new-example_1"] = df_3000["sbs_example_3"]
df_3000["new-sbs_chant_pali_1"] = df_3000["sbs_chant_pali_3"]
df_3000["new-sbs_chant_eng_1"] = df_3000["sbs_chant_eng_3"]
df_3000["new-sbs_chapter_1"] = df_3000["sbs_chapter_3"]

df_3000["sbs_source_3"] = ""
df_3000["sbs_sutta_3"] = ""
df_3000["sbs_example_3"] = ""
df_3000["sbs_chant_pali_3"] = ""
df_3000["sbs_chant_eng_3"] = ""
df_3000["sbs_chapter_3"] = ""

df_3000["source_1"] = df_3000["new-source_1"]
df_3000["sutta_1"] = df_3000["new-sutta_1"]
df_3000["example_1"] = df_3000["new-example_1"]
df_3000["sbs_chant_pali_1"] = df_3000["new-sbs_chant_pali_1"]
df_3000["sbs_chant_eng_1"] = df_3000["new-sbs_chant_eng_1"]
df_3000["sbs_chapter_1"] = df_3000["new-sbs_chapter_1"]

df_3000 = df_3000[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_3000)

# df_3000.to_csv("../spreadsheets/df_3000.csv", sep="\t", index=None)

# filtering 3001

test1 = df['move'] == '3001'
filter = test1
df_3001 = df.loc[filter]

df_3001["new-source_1"] = df_3001["sbs_source_3"]
df_3001["new-sutta_1"] = df_3001["sbs_sutta_3"]
df_3001["new-example_1"] = df_3001["sbs_example_3"]
df_3001["new-sbs_chant_pali_1"] = df_3001["sbs_chant_pali_3"]
df_3001["new-sbs_chant_eng_1"] = df_3001["sbs_chant_eng_3"]
df_3001["new-sbs_chapter_1"] = df_3001["sbs_chapter_3"]

df_3001["sbs_source_3"] = ""
df_3001["sbs_sutta_3"] = ""
df_3001["sbs_example_3"] = ""
df_3001["sbs_chant_pali_3"] = ""
df_3001["sbs_chant_eng_3"] = ""
df_3001["sbs_chapter_3"] = ""

df_3001["new-sbs_source_4"] = df_3001["source_1"]
df_3001["new-sbs_sutta_4"] = df_3001["sutta_1"]
df_3001["new-sbs_example_4"] = df_3001["example_1"]
df_3001["new-sbs_chant_pali_4"] = df_3001["sbs_chant_pali_1"]
df_3001["new-sbs_chant_eng_4"] = df_3001["sbs_chant_eng_1"]
df_3001["new-sbs_chapter_4"] = df_3001["sbs_chapter_1"]

df_3001["source_1"] = ""
df_3001["sutta_1"] = ""
df_3001["example_1"] = ""
df_3001["sbs_chant_pali_1"] = ""
df_3001["sbs_chant_eng_1"] = ""
df_3001["sbs_chapter_1"] = ""

df_3001["sbs_source_4"] = df_3001["new-sbs_source_4"]
df_3001["sbs_sutta_4"] = df_3001["new-sbs_sutta_4"]
df_3001["sbs_example_4"] = df_3001["new-sbs_example_4"]
df_3001["sbs_chant_pali_4"] = df_3001["new-sbs_chant_pali_4"]
df_3001["sbs_chant_eng_4"] = df_3001["new-sbs_chant_eng_4"]
df_3001["sbs_chapter_4"] = df_3001["new-sbs_chapter_4"]

df_3001["source_1"] = df_3001["new-source_1"]
df_3001["sutta_1"] = df_3001["new-sutta_1"]
df_3001["example_1"] = df_3001["new-example_1"]
df_3001["sbs_chant_pali_1"] = df_3001["new-sbs_chant_pali_1"]
df_3001["sbs_chant_eng_1"] = df_3001["new-sbs_chant_eng_1"]
df_3001["sbs_chapter_1"] = df_3001["new-sbs_chapter_1"]

df_3001 = df_3001[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_3001)

# df_3001.to_csv("../spreadsheets/df_3001.csv", sep="\t", index=None)

# filtering 3010

test1 = df['move'] == '3010'
filter = test1
df_3010 = df.loc[filter]

df_3010["new-source_1"] = df_3010["sbs_source_3"]
df_3010["new-sutta_1"] = df_3010["sbs_sutta_3"]
df_3010["new-example_1"] = df_3010["sbs_example_3"]
df_3010["new-sbs_chant_pali_1"] = df_3010["sbs_chant_pali_3"]
df_3010["new-sbs_chant_eng_1"] = df_3010["sbs_chant_eng_3"]
df_3010["new-sbs_chapter_1"] = df_3010["sbs_chapter_3"]

df_3010["sbs_source_3"] = ""
df_3010["sbs_sutta_3"] = ""
df_3010["sbs_example_3"] = ""
df_3010["sbs_chant_pali_3"] = ""
df_3010["sbs_chant_eng_3"] = ""
df_3010["sbs_chapter_3"] = ""

df_3010["new-sbs_source_3"] = df_3010["source_1"]
df_3010["new-sbs_sutta_3"] = df_3010["sutta_1"]
df_3010["new-sbs_example_3"] = df_3010["example_1"]
df_3010["new-sbs_chant_pali_3"] = df_3010["sbs_chant_pali_1"]
df_3010["new-sbs_chant_eng_3"] = df_3010["sbs_chant_eng_1"]
df_3010["new-sbs_chapter_3"] = df_3010["sbs_chapter_1"]

df_3010["source_1"] = ""
df_3010["sutta_1"] = ""
df_3010["example_1"] = ""
df_3010["sbs_chant_pali_1"] = ""
df_3010["sbs_chant_eng_1"] = ""
df_3010["sbs_chapter_1"] = ""

df_3010["sbs_source_3"] = df_3010["new-sbs_source_3"]
df_3010["sbs_sutta_3"] = df_3010["new-sbs_sutta_3"]
df_3010["sbs_example_3"] = df_3010["new-sbs_example_3"]
df_3010["sbs_chant_pali_3"] = df_3010["new-sbs_chant_pali_3"]
df_3010["sbs_chant_eng_3"] = df_3010["new-sbs_chant_eng_3"]
df_3010["sbs_chapter_3"] = df_3010["new-sbs_chapter_3"]

df_3010["source_1"] = df_3010["new-source_1"]
df_3010["sutta_1"] = df_3010["new-sutta_1"]
df_3010["example_1"] = df_3010["new-example_1"]
df_3010["sbs_chant_pali_1"] = df_3010["new-sbs_chant_pali_1"]
df_3010["sbs_chant_eng_1"] = df_3010["new-sbs_chant_eng_1"]
df_3010["sbs_chapter_1"] = df_3010["new-sbs_chapter_1"]


df_3010 = df_3010[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_3010)

# df_3010.to_csv("../spreadsheets/df_3010.csv", sep="\t", index=None)

# filtering 3012

test1 = df['move'] == '3012'
filter = test1
df_3012 = df.loc[filter]

df_3012["new-source_1"] = df_3012["sbs_source_3"]
df_3012["new-sutta_1"] = df_3012["sbs_sutta_3"]
df_3012["new-example_1"] = df_3012["sbs_example_3"]
df_3012["new-sbs_chant_pali_1"] = df_3012["sbs_chant_pali_3"]
df_3012["new-sbs_chant_eng_1"] = df_3012["sbs_chant_eng_3"]
df_3012["new-sbs_chapter_1"] = df_3012["sbs_chapter_3"]

df_3012["sbs_source_3"] = ""
df_3012["sbs_sutta_3"] = ""
df_3012["sbs_example_3"] = ""
df_3012["sbs_chant_pali_3"] = ""
df_3012["sbs_chant_eng_3"] = ""
df_3012["sbs_chapter_3"] = ""

df_3012["new-sbs_source_3"] = df_3012["source_1"]
df_3012["new-sbs_sutta_3"] = df_3012["sutta_1"]
df_3012["new-sbs_example_3"] = df_3012["example_1"]
df_3012["new-sbs_chant_pali_3"] = df_3012["sbs_chant_pali_1"]
df_3012["new-sbs_chant_eng_3"] = df_3012["sbs_chant_eng_1"]
df_3012["new-sbs_chapter_3"] = df_3012["sbs_chapter_1"]

df_3012["source_1"] = ""
df_3012["sutta_1"] = ""
df_3012["example_1"] = ""
df_3012["sbs_chant_pali_1"] = ""
df_3012["sbs_chant_eng_1"] = ""
df_3012["sbs_chapter_1"] = ""

df_3012["new-sbs_source_4"] = df_3012["source_2"]
df_3012["new-sbs_sutta_4"] = df_3012["sutta_2"]
df_3012["new-sbs_example_4"] = df_3012["example_2"]
df_3012["new-sbs_chant_pali_4"] = df_3012["sbs_chant_pali_2"]
df_3012["new-sbs_chant_eng_4"] = df_3012["sbs_chant_eng_2"]
df_3012["new-sbs_chapter_4"] = df_3012["sbs_chapter_2"]

df_3012["source_2"] = ""
df_3012["sutta_2"] = ""
df_3012["example_2"] = ""
df_3012["sbs_chant_pali_2"] = ""
df_3012["sbs_chant_eng_2"] = ""
df_3012["sbs_chapter_2"] = ""

df_3012["sbs_source_4"] = df_3012["new-sbs_source_4"]
df_3012["sbs_sutta_4"] = df_3012["new-sbs_sutta_4"]
df_3012["sbs_example_4"] = df_3012["new-sbs_example_4"]
df_3012["sbs_chant_pali_4"] = df_3012["new-sbs_chant_pali_4"]
df_3012["sbs_chant_eng_4"] = df_3012["new-sbs_chant_eng_4"]
df_3012["sbs_chapter_4"] = df_3012["new-sbs_chapter_4"]

df_3012["sbs_source_3"] = df_3012["new-sbs_source_3"]
df_3012["sbs_sutta_3"] = df_3012["new-sbs_sutta_3"]
df_3012["sbs_example_3"] = df_3012["new-sbs_example_3"]
df_3012["sbs_chant_pali_3"] = df_3012["new-sbs_chant_pali_3"]
df_3012["sbs_chant_eng_3"] = df_3012["new-sbs_chant_eng_3"]
df_3012["sbs_chapter_3"] = df_3012["new-sbs_chapter_3"]

df_3012["source_1"] = df_3012["new-source_1"]
df_3012["sutta_1"] = df_3012["new-sutta_1"]
df_3012["example_1"] = df_3012["new-example_1"]
df_3012["sbs_chant_pali_1"] = df_3012["new-sbs_chant_pali_1"]
df_3012["sbs_chant_eng_1"] = df_3012["new-sbs_chant_eng_1"]
df_3012["sbs_chapter_1"] = df_3012["new-sbs_chapter_1"]


df_3012 = df_3012[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_3012)

# df_3012.to_csv("../spreadsheets/df_3012.csv", sep="\t", index=None)


# filtering 3020

test1 = df['move'] == '3020'
filter = test1
df_3020 = df.loc[filter]

df_3020["new-source_1"] = df_3020["sbs_source_3"]
df_3020["new-sutta_1"] = df_3020["sbs_sutta_3"]
df_3020["new-example_1"] = df_3020["sbs_example_3"]
df_3020["new-sbs_chant_pali_1"] = df_3020["sbs_chant_pali_3"]
df_3020["new-sbs_chant_eng_1"] = df_3020["sbs_chant_eng_3"]
df_3020["new-sbs_chapter_1"] = df_3020["sbs_chapter_3"]

df_3020["sbs_source_3"] = ""
df_3020["sbs_sutta_3"] = ""
df_3020["sbs_example_3"] = ""
df_3020["sbs_chant_pali_3"] = ""
df_3020["sbs_chant_eng_3"] = ""
df_3020["sbs_chapter_3"] = ""

df_3020["new-sbs_source_3"] = df_3020["source_2"]
df_3020["new-sbs_sutta_3"] = df_3020["sutta_2"]
df_3020["new-sbs_example_3"] = df_3020["example_2"]
df_3020["new-sbs_chant_pali_3"] = df_3020["sbs_chant_pali_2"]
df_3020["new-sbs_chant_eng_3"] = df_3020["sbs_chant_eng_2"]
df_3020["new-sbs_chapter_3"] = df_3020["sbs_chapter_2"]

df_3020["source_2"] = ""
df_3020["sutta_2"] = ""
df_3020["example_2"] = ""
df_3020["sbs_chant_pali_2"] = ""
df_3020["sbs_chant_eng_2"] = ""
df_3020["sbs_chapter_2"] = ""

df_3020["sbs_source_3"] = df_3020["new-sbs_source_3"]
df_3020["sbs_sutta_3"] = df_3020["new-sbs_sutta_3"]
df_3020["sbs_example_3"] = df_3020["new-sbs_example_3"]
df_3020["sbs_chant_pali_3"] = df_3020["new-sbs_chant_pali_3"]
df_3020["sbs_chant_eng_3"] = df_3020["new-sbs_chant_eng_3"]
df_3020["sbs_chapter_3"] = df_3020["new-sbs_chapter_3"]

df_3020["source_1"] = df_3020["new-source_1"]
df_3020["sutta_1"] = df_3020["new-sutta_1"]
df_3020["example_1"] = df_3020["new-example_1"]
df_3020["sbs_chant_pali_1"] = df_3020["new-sbs_chant_pali_1"]
df_3020["sbs_chant_eng_1"] = df_3020["new-sbs_chant_eng_1"]
df_3020["sbs_chapter_1"] = df_3020["new-sbs_chapter_1"]

df_3020 = df_3020[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_3020)

# df_3020.to_csv("../spreadsheets/df_3020.csv", sep="\t", index=None)

# filtering 3021

test1 = df['move'] == '3021'
filter = test1
df_3021 = df.loc[filter]

df_3021["new-source_1"] = df_3021["sbs_source_3"]
df_3021["new-sutta_1"] = df_3021["sbs_sutta_3"]
df_3021["new-example_1"] = df_3021["sbs_example_3"]
df_3021["new-sbs_chant_pali_1"] = df_3021["sbs_chant_pali_3"]
df_3021["new-sbs_chant_eng_1"] = df_3021["sbs_chant_eng_3"]
df_3021["new-sbs_chapter_1"] = df_3021["sbs_chapter_3"]

df_3021["sbs_source_3"] = ""
df_3021["sbs_sutta_3"] = ""
df_3021["sbs_example_3"] = ""
df_3021["sbs_chant_pali_3"] = ""
df_3021["sbs_chant_eng_3"] = ""
df_3021["sbs_chapter_3"] = ""

df_3021["new-sbs_source_3"] = df_3021["source_2"]
df_3021["new-sbs_sutta_3"] = df_3021["sutta_2"]
df_3021["new-sbs_example_3"] = df_3021["example_2"]
df_3021["new-sbs_chant_pali_3"] = df_3021["sbs_chant_pali_2"]
df_3021["new-sbs_chant_eng_3"] = df_3021["sbs_chant_eng_2"]
df_3021["new-sbs_chapter_3"] = df_3021["sbs_chapter_2"]

df_3021["source_2"] = ""
df_3021["sutta_2"] = ""
df_3021["example_2"] = ""
df_3021["sbs_chant_pali_2"] = ""
df_3021["sbs_chant_eng_2"] = ""
df_3021["sbs_chapter_2"] = ""

df_3021["new-sbs_source_4"] = df_3021["source_1"]
df_3021["new-sbs_sutta_4"] = df_3021["sutta_1"]
df_3021["new-sbs_example_4"] = df_3021["example_1"]
df_3021["new-sbs_chant_pali_4"] = df_3021["sbs_chant_pali_1"]
df_3021["new-sbs_chant_eng_4"] = df_3021["sbs_chant_eng_1"]
df_3021["new-sbs_chapter_4"] = df_3021["sbs_chapter_1"]

df_3021["source_1"] = ""
df_3021["sutta_1"] = ""
df_3021["example_1"] = ""
df_3021["sbs_chant_pali_1"] = ""
df_3021["sbs_chant_eng_1"] = ""
df_3021["sbs_chapter_1"] = ""

df_3021["sbs_source_4"] = df_3021["new-sbs_source_4"]
df_3021["sbs_sutta_4"] = df_3021["new-sbs_sutta_4"]
df_3021["sbs_example_4"] = df_3021["new-sbs_example_4"]
df_3021["sbs_chant_pali_4"] = df_3021["new-sbs_chant_pali_4"]
df_3021["sbs_chant_eng_4"] = df_3021["new-sbs_chant_eng_4"]
df_3021["sbs_chapter_4"] = df_3021["new-sbs_chapter_4"]

df_3021["sbs_source_3"] = df_3021["new-sbs_source_3"]
df_3021["sbs_sutta_3"] = df_3021["new-sbs_sutta_3"]
df_3021["sbs_example_3"] = df_3021["new-sbs_example_3"]
df_3021["sbs_chant_pali_3"] = df_3021["new-sbs_chant_pali_3"]
df_3021["sbs_chant_eng_3"] = df_3021["new-sbs_chant_eng_3"]
df_3021["sbs_chapter_3"] = df_3021["new-sbs_chapter_3"]

df_3021["source_1"] = df_3021["new-source_1"]
df_3021["sutta_1"] = df_3021["new-sutta_1"]
df_3021["example_1"] = df_3021["new-example_1"]
df_3021["sbs_chant_pali_1"] = df_3021["new-sbs_chant_pali_1"]
df_3021["sbs_chant_eng_1"] = df_3021["new-sbs_chant_eng_1"]
df_3021["sbs_chapter_1"] = df_3021["new-sbs_chapter_1"]

df_3021 = df_3021[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_3021)

# df_3021.to_csv("../spreadsheets/df_3021.csv", sep="\t", index=None)


# filtering 4000

test1 = df['move'] == '4000'
filter = test1
df_4000 = df.loc[filter]

df_4000["new-source_1"] = df_4000["sbs_source_3"]
df_4000["new-sutta_1"] = df_4000["sbs_sutta_3"]
df_4000["new-example_1"] = df_4000["sbs_example_3"]
df_4000["new-sbs_chant_pali_1"] = df_4000["sbs_chant_pali_3"]
df_4000["new-sbs_chant_eng_1"] = df_4000["sbs_chant_eng_3"]
df_4000["new-sbs_chapter_1"] = df_4000["sbs_chapter_3"]

df_4000["sbs_source_3"] = ""
df_4000["sbs_sutta_3"] = ""
df_4000["sbs_example_3"] = ""
df_4000["sbs_chant_pali_3"] = ""
df_4000["sbs_chant_eng_3"] = ""
df_4000["sbs_chapter_3"] = ""

df_4000["source_1"] = df_4000["new-source_1"]
df_4000["sutta_1"] = df_4000["new-sutta_1"]
df_4000["example_1"] = df_4000["new-example_1"]
df_4000["sbs_chant_pali_1"] = df_4000["new-sbs_chant_pali_1"]
df_4000["sbs_chant_eng_1"] = df_4000["new-sbs_chant_eng_1"]
df_4000["sbs_chapter_1"] = df_4000["new-sbs_chapter_1"]


df_4000 = df_4000[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_4000)

# df_4000.to_csv("../spreadsheets/df_4000.csv", sep="\t", index=None)


# filtering 4001

test1 = df['move'] == '4001'
filter = test1
df_4001 = df.loc[filter]

df_4001["new-source_1"] = df_4001["sbs_source_3"]
df_4001["new-sutta_1"] = df_4001["sbs_sutta_3"]
df_4001["new-example_1"] = df_4001["sbs_example_3"]
df_4001["new-sbs_chant_pali_1"] = df_4001["sbs_chant_pali_3"]
df_4001["new-sbs_chant_eng_1"] = df_4001["sbs_chant_eng_3"]
df_4001["new-sbs_chapter_1"] = df_4001["sbs_chapter_3"]

df_4001["sbs_source_3"] = ""
df_4001["sbs_sutta_3"] = ""
df_4001["sbs_example_3"] = ""
df_4001["sbs_chant_pali_3"] = ""
df_4001["sbs_chant_eng_3"] = ""
df_4001["sbs_chapter_3"] = ""

df_4001["new-sbs_source_4"] = df_4001["source_1"]
df_4001["new-sbs_sutta_4"] = df_4001["sutta_1"]
df_4001["new-sbs_example_4"] = df_4001["example_1"]
df_4001["new-sbs_chant_pali_4"] = df_4001["sbs_chant_pali_1"]
df_4001["new-sbs_chant_eng_4"] = df_4001["sbs_chant_eng_1"]
df_4001["new-sbs_chapter_4"] = df_4001["sbs_chapter_1"]

df_4001["source_1"] = ""
df_4001["sutta_1"] = ""
df_4001["example_1"] = ""
df_4001["sbs_chant_pali_1"] = ""
df_4001["sbs_chant_eng_1"] = ""
df_4001["sbs_chapter_1"] = ""

df_4001["sbs_source_4"] = df_4001["new-sbs_source_4"]
df_4001["sbs_sutta_4"] = df_4001["new-sbs_sutta_4"]
df_4001["sbs_example_4"] = df_4001["new-sbs_example_4"]
df_4001["sbs_chant_pali_4"] = df_4001["new-sbs_chant_pali_4"]
df_4001["sbs_chant_eng_4"] = df_4001["new-sbs_chant_eng_4"]
df_4001["sbs_chapter_4"] = df_4001["new-sbs_chapter_4"]

df_4001["source_1"] = df_4001["new-source_1"]
df_4001["sutta_1"] = df_4001["new-sutta_1"]
df_4001["example_1"] = df_4001["new-example_1"]
df_4001["sbs_chant_pali_1"] = df_4001["new-sbs_chant_pali_1"]
df_4001["sbs_chant_eng_1"] = df_4001["new-sbs_chant_eng_1"]
df_4001["sbs_chapter_1"] = df_4001["new-sbs_chapter_1"]


df_4001 = df_4001[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_4001)

# df_4001.to_csv("../spreadsheets/df_4001.csv", sep="\t", index=None)

# filtering 4010

test1 = df['move'] == '4010'
filter = test1
df_4010 = df.loc[filter]

df_4010["new-source_1"] = df_4010["sbs_source_3"]
df_4010["new-sutta_1"] = df_4010["sbs_sutta_3"]
df_4010["new-example_1"] = df_4010["sbs_example_3"]
df_4010["new-sbs_chant_pali_1"] = df_4010["sbs_chant_pali_3"]
df_4010["new-sbs_chant_eng_1"] = df_4010["sbs_chant_eng_3"]
df_4010["new-sbs_chapter_1"] = df_4010["sbs_chapter_3"]

df_4010["sbs_source_3"] = ""
df_4010["sbs_sutta_3"] = ""
df_4010["sbs_example_3"] = ""
df_4010["sbs_chant_pali_3"] = ""
df_4010["sbs_chant_eng_3"] = ""
df_4010["sbs_chapter_3"] = ""

df_4010["new-sbs_source_3"] = df_4010["source_1"]
df_4010["new-sbs_sutta_3"] = df_4010["sutta_1"]
df_4010["new-sbs_example_3"] = df_4010["example_1"]
df_4010["new-sbs_chant_pali_3"] = df_4010["sbs_chant_pali_1"]
df_4010["new-sbs_chant_eng_3"] = df_4010["sbs_chant_eng_1"]
df_4010["new-sbs_chapter_3"] = df_4010["sbs_chapter_1"]

df_4010["source_1"] = ""
df_4010["sutta_1"] = ""
df_4010["example_1"] = ""
df_4010["sbs_chant_pali_1"] = ""
df_4010["sbs_chant_eng_1"] = ""
df_4010["sbs_chapter_1"] = ""

df_4010["sbs_source_3"] = df_4010["new-sbs_source_3"]
df_4010["sbs_sutta_3"] = df_4010["new-sbs_sutta_3"]
df_4010["sbs_example_3"] = df_4010["new-sbs_example_3"]
df_4010["sbs_chant_pali_3"] = df_4010["new-sbs_chant_pali_3"]
df_4010["sbs_chant_eng_3"] = df_4010["new-sbs_chant_eng_3"]
df_4010["sbs_chapter_3"] = df_4010["new-sbs_chapter_3"]

df_4010["source_1"] = df_4010["new-source_1"]
df_4010["sutta_1"] = df_4010["new-sutta_1"]
df_4010["example_1"] = df_4010["new-example_1"]
df_4010["sbs_chant_pali_1"] = df_4010["new-sbs_chant_pali_1"]
df_4010["sbs_chant_eng_1"] = df_4010["new-sbs_chant_eng_1"]
df_4010["sbs_chapter_1"] = df_4010["new-sbs_chapter_1"]

df_4010 = df_4010[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_4010)

# df_4010.to_csv("../spreadsheets/df_4010.csv", sep="\t", index=None)


# filtering 4100

test1 = df['move'] == '4100'
filter = test1
df_4100 = df.loc[filter]

df_4100["new-source_1"] = df_4100["sbs_source_3"]
df_4100["new-sutta_1"] = df_4100["sbs_sutta_3"]
df_4100["new-example_1"] = df_4100["sbs_example_3"]
df_4100["new-sbs_chant_pali_1"] = df_4100["sbs_chant_pali_3"]
df_4100["new-sbs_chant_eng_1"] = df_4100["sbs_chant_eng_3"]
df_4100["new-sbs_chapter_1"] = df_4100["sbs_chapter_3"]

df_4100["sbs_source_3"] = ""
df_4100["sbs_sutta_3"] = ""
df_4100["sbs_example_3"] = ""
df_4100["sbs_chant_pali_3"] = ""
df_4100["sbs_chant_eng_3"] = ""
df_4100["sbs_chapter_3"] = ""

df_4100["new-source_2"] = df_4100["source_1"]
df_4100["new-sutta_2"] = df_4100["sutta_1"]
df_4100["new-example_2"] = df_4100["example_1"]
df_4100["new-sbs_chant_pali_2"] = df_4100["sbs_chant_pali_1"]
df_4100["new-sbs_chant_eng_2"] = df_4100["sbs_chant_eng_1"]
df_4100["new-sbs_chapter_2"] = df_4100["sbs_chapter_1"]

df_4100["source_1"] = ""
df_4100["sutta_1"] = ""
df_4100["example_1"] = ""
df_4100["sbs_chant_pali_1"] = ""
df_4100["sbs_chant_eng_1"] = ""
df_4100["sbs_chapter_1"] = ""

df_4100["source_2"] = df_4100["new-source_2"]
df_4100["sutta_2"] = df_4100["new-sutta_2"]
df_4100["example_2"] = df_4100["new-example_2"]
df_4100["sbs_chant_pali_2"] = df_4100["new-sbs_chant_pali_2"]
df_4100["sbs_chant_eng_2"] = df_4100["new-sbs_chant_eng_2"]
df_4100["sbs_chapter_2"] = df_4100["new-sbs_chapter_2"]

df_4100["source_1"] = df_4100["new-source_1"]
df_4100["sutta_1"] = df_4100["new-sutta_1"]
df_4100["example_1"] = df_4100["new-example_1"]
df_4100["sbs_chant_pali_1"] = df_4100["new-sbs_chant_pali_1"]
df_4100["sbs_chant_eng_1"] = df_4100["new-sbs_chant_eng_1"]
df_4100["sbs_chapter_1"] = df_4100["new-sbs_chapter_1"]

df_4100 = df_4100[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# print(df_4100)

# df_4100.to_csv("../spreadsheets/df_4100.csv", sep="\t", index=None)



# combine all

df_combine = pd.concat([df_empty, df_0000, df_0001, df_0002, df_0003, df_0010, df_0012, df_0013, df_0020, df_0021, df_0023, df_0100, df_0102, df_0120, df_0123, df_0300, df_0310, df_0312, df_0320, df_0400, df_0402, df_2000, df_2001, df_2010, df_2013, df_2100, df_2300, df_3000, df_3001, df_3010, df_3012, df_3020, df_3021, df_4000, df_4001, df_4010, df_4100])

df_combine = df_combine[['id', 'pali_1', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]


df_combine.to_csv("../spreadsheets/df_combine.csv", sep="\t", index=None)





