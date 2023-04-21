import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("")

# df = df.drop(['sync'], axis=1)

# df = df[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4', 'move', 'sync']]


# filtering df_0000 and empty and df_extra

test1 = df['move'] == '0000'
filter = test1
df_0000 = df.loc[filter]

df_0000 = df_0000[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# df_0000.to_csv("../spreadsheets/df_0000.csv", sep="\t", index=None)

test1 = df['move'] == "empty"
filter = test1
df_empty = df.loc[filter]

df_empty = df_empty[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# df_empty.to_csv("../spreadsheets/df_empty.csv", sep="\t", index=None)

test1 = df['sync'] == 'e'
filter = test1
df_extra = df.loc[filter]

df_extra.to_csv("../spreadsheets/df_extra.csv", sep="\t", index=None)

# filtering 0001

test1 = df['move'] == '0001'
filter = test1
df_0001 = df.loc[filter]

df_0001["new-Source4"] = df_0001["Source1"]
df_0001["new-Sutta4"] = df_0001["Sutta1"]
df_0001["new-Example4"] = df_0001["Example1"]
df_0001["new-Pali chant 4"] = df_0001["Pali chant 1"]
df_0001["new-English chant 4"] = df_0001["English chant 1"]
df_0001["new-Chapter 4"] = df_0001["Chapter 1"]

df_0001["Source1"] = ""
df_0001["Sutta1"] = ""
df_0001["Example1"] = ""
df_0001["Pali chant 1"] = ""
df_0001["English chant 1"] = ""
df_0001["Chapter 1"] = ""

df_0001["Source4"] = df_0001["new-Source4"]
df_0001["Sutta4"] = df_0001["new-Sutta4"]
df_0001["Example4"] = df_0001["new-Example4"]
df_0001["Pali chant 4"] = df_0001["new-Pali chant 4"]
df_0001["English chant 4"] = df_0001["new-English chant 4"]
df_0001["Chapter 4"] = df_0001["new-Chapter 4"]


df_0001 = df_0001[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0001)

# df_0001.to_csv("../spreadsheets/df_0001.csv", sep="\t", index=None)

# filtering 0002

test1 = df['move'] == '0002'
filter = test1
df_0002 = df.loc[filter]

df_0002["new-Source4"] = df_0002["Source2"]
df_0002["new-Sutta4"] = df_0002["Sutta2"]
df_0002["new-Example4"] = df_0002["Example2"]
df_0002["new-Pali chant 4"] = df_0002["Pali chant 2"]
df_0002["new-English chant 4"] = df_0002["English chant 2"]
df_0002["new-Chapter 4"] = df_0002["Chapter 2"]

df_0002["Source2"] = ""
df_0002["Sutta2"] = ""
df_0002["Example2"] = ""
df_0002["Pali chant 2"] = ""
df_0002["English chant 2"] = ""
df_0002["Chapter 2"] = ""

df_0002["Source4"] = df_0002["new-Source4"]
df_0002["Sutta4"] = df_0002["new-Sutta4"]
df_0002["Example4"] = df_0002["new-Example4"]
df_0002["Pali chant 4"] = df_0002["new-Pali chant 4"]
df_0002["English chant 4"] = df_0002["new-English chant 4"]
df_0002["Chapter 4"] = df_0002["new-Chapter 4"]


df_0002 = df_0002[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0002)

# df_0002.to_csv("../spreadsheets/df_0002.csv", sep="\t", index=None)


# filtering 0003

test1 = df['move'] == '0003'
filter = test1
df_0003 = df.loc[filter]

df_0003["new-Source4"] = df_0003["Source3"]
df_0003["new-Sutta4"] = df_0003["Sutta3"]
df_0003["new-Example4"] = df_0003["Example3"]
df_0003["new-Pali chant 4"] = df_0003["Pali chant 3"]
df_0003["new-English chant 4"] = df_0003["English chant 3"]
df_0003["new-Chapter 4"] = df_0003["Chapter 3"]

df_0003["Source3"] = ""
df_0003["Sutta3"] = ""
df_0003["Example3"] = ""
df_0003["Pali chant 3"] = ""
df_0003["English chant 3"] = ""
df_0003["Chapter 3"] = ""

df_0003["Source4"] = df_0003["new-Source4"]
df_0003["Sutta4"] = df_0003["new-Sutta4"]
df_0003["Example4"] = df_0003["new-Example4"]
df_0003["Pali chant 4"] = df_0003["new-Pali chant 4"]
df_0003["English chant 4"] = df_0003["new-English chant 4"]
df_0003["Chapter 4"] = df_0003["new-Chapter 4"]


df_0003 = df_0003[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0003)

# df_0003.to_csv("../spreadsheets/df_0003.csv", sep="\t", index=None)


# filtering 0010

test1 = df['move'] == '0010'
filter = test1
df_0010 = df.loc[filter]

df_0010["new-Source3"] = df_0010["Source1"]
df_0010["new-Sutta3"] = df_0010["Sutta1"]
df_0010["new-Example3"] = df_0010["Example1"]
df_0010["new-Pali chant 3"] = df_0010["Pali chant 1"]
df_0010["new-English chant 3"] = df_0010["English chant 1"]
df_0010["new-Chapter 3"] = df_0010["Chapter 1"]

df_0010["Source1"] = ""
df_0010["Sutta1"] = ""
df_0010["Example1"] = ""
df_0010["Pali chant 1"] = ""
df_0010["English chant 1"] = ""
df_0010["Chapter 1"] = ""

df_0010["Source3"] = df_0010["new-Source3"]
df_0010["Sutta3"] = df_0010["new-Sutta3"]
df_0010["Example3"] = df_0010["new-Example3"]
df_0010["Pali chant 3"] = df_0010["new-Pali chant 3"]
df_0010["English chant 3"] = df_0010["new-English chant 3"]
df_0010["Chapter 3"] = df_0010["new-Chapter 3"]


df_0010 = df_0010[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0010)

# df_0010.to_csv("../spreadsheets/df_0010.csv", sep="\t", index=None)

# filtering 0012

test1 = df['move'] == '0012'
filter = test1
df_0012 = df.loc[filter]

df_0012["new-Source3"] = df_0012["Source1"]
df_0012["new-Sutta3"] = df_0012["Sutta1"]
df_0012["new-Example3"] = df_0012["Example1"]
df_0012["new-Pali chant 3"] = df_0012["Pali chant 1"]
df_0012["new-English chant 3"] = df_0012["English chant 1"]
df_0012["new-Chapter 3"] = df_0012["Chapter 1"]

df_0012["Source1"] = ""
df_0012["Sutta1"] = ""
df_0012["Example1"] = ""
df_0012["Pali chant 1"] = ""
df_0012["English chant 1"] = ""
df_0012["Chapter 1"] = ""

df_0012["new-Source4"] = df_0012["Source2"]
df_0012["new-Sutta4"] = df_0012["Sutta2"]
df_0012["new-Example4"] = df_0012["Example2"]
df_0012["new-Pali chant 4"] = df_0012["Pali chant 2"]
df_0012["new-English chant 4"] = df_0012["English chant 2"]
df_0012["new-Chapter 4"] = df_0012["Chapter 2"]

df_0012["Source2"] = ""
df_0012["Sutta2"] = ""
df_0012["Example2"] = ""
df_0012["Pali chant 2"] = ""
df_0012["English chant 2"] = ""
df_0012["Chapter 2"] = ""

df_0012["Source4"] = df_0012["new-Source4"]
df_0012["Sutta4"] = df_0012["new-Sutta4"]
df_0012["Example4"] = df_0012["new-Example4"]
df_0012["Pali chant 4"] = df_0012["new-Pali chant 4"]
df_0012["English chant 4"] = df_0012["new-English chant 4"]
df_0012["Chapter 4"] = df_0012["new-Chapter 4"]

df_0012["Source3"] = df_0012["new-Source3"]
df_0012["Sutta3"] = df_0012["new-Sutta3"]
df_0012["Example3"] = df_0012["new-Example3"]
df_0012["Pali chant 3"] = df_0012["new-Pali chant 3"]
df_0012["English chant 3"] = df_0012["new-English chant 3"]
df_0012["Chapter 3"] = df_0012["new-Chapter 3"]


df_0012 = df_0012[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0012)

# df_0012.to_csv("../spreadsheets/df_0012.csv", sep="\t", index=None)


# filtering 0013

test1 = df['move'] == '0013'
filter = test1
df_0013 = df.loc[filter]

df_0013["new-Source3"] = df_0013["Source1"]
df_0013["new-Sutta3"] = df_0013["Sutta1"]
df_0013["new-Example3"] = df_0013["Example1"]
df_0013["new-Pali chant 3"] = df_0013["Pali chant 1"]
df_0013["new-English chant 3"] = df_0013["English chant 1"]
df_0013["new-Chapter 3"] = df_0013["Chapter 1"]

df_0013["Source1"] = ""
df_0013["Sutta1"] = ""
df_0013["Example1"] = ""
df_0013["Pali chant 1"] = ""
df_0013["English chant 1"] = ""
df_0013["Chapter 1"] = ""

df_0013["new-Source4"] = df_0013["Source3"]
df_0013["new-Sutta4"] = df_0013["Sutta3"]
df_0013["new-Example4"] = df_0013["Example3"]
df_0013["new-Pali chant 4"] = df_0013["Pali chant 3"]
df_0013["new-English chant 4"] = df_0013["English chant 3"]
df_0013["new-Chapter 4"] = df_0013["Chapter 3"]

df_0013["Source3"] = ""
df_0013["Sutta3"] = ""
df_0013["Example3"] = ""
df_0013["Pali chant 3"] = ""
df_0013["English chant 3"] = ""
df_0013["Chapter 3"] = ""

df_0013["Source4"] = df_0013["new-Source4"]
df_0013["Sutta4"] = df_0013["new-Sutta4"]
df_0013["Example4"] = df_0013["new-Example4"]
df_0013["Pali chant 4"] = df_0013["new-Pali chant 4"]
df_0013["English chant 4"] = df_0013["new-English chant 4"]
df_0013["Chapter 4"] = df_0013["new-Chapter 4"]

df_0013["Source3"] = df_0013["new-Source3"]
df_0013["Sutta3"] = df_0013["new-Sutta3"]
df_0013["Example3"] = df_0013["new-Example3"]
df_0013["Pali chant 3"] = df_0013["new-Pali chant 3"]
df_0013["English chant 3"] = df_0013["new-English chant 3"]
df_0013["Chapter 3"] = df_0013["new-Chapter 3"]


df_0013 = df_0013[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0013)

# df_0013.to_csv("../spreadsheets/df_0013.csv", sep="\t", index=None)

# filtering 0020

test1 = df['move'] == '0020'
filter = test1
df_0020 = df.loc[filter]

df_0020["new-Source3"] = df_0020["Source2"]
df_0020["new-Sutta3"] = df_0020["Sutta2"]
df_0020["new-Example3"] = df_0020["Example2"]
df_0020["new-Pali chant 3"] = df_0020["Pali chant 2"]
df_0020["new-English chant 3"] = df_0020["English chant 2"]
df_0020["new-Chapter 3"] = df_0020["Chapter 2"]

df_0020["Source2"] = ""
df_0020["Sutta2"] = ""
df_0020["Example2"] = ""
df_0020["Pali chant 2"] = ""
df_0020["English chant 2"] = ""
df_0020["Chapter 2"] = ""

df_0020["Source3"] = df_0020["new-Source3"]
df_0020["Sutta3"] = df_0020["new-Sutta3"]
df_0020["Example3"] = df_0020["new-Example3"]
df_0020["Pali chant 3"] = df_0020["new-Pali chant 3"]
df_0020["English chant 3"] = df_0020["new-English chant 3"]
df_0020["Chapter 3"] = df_0020["new-Chapter 3"]


df_0020 = df_0020[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0020)

# df_0020.to_csv("../spreadsheets/df_0020.csv", sep="\t", index=None)


# filtering 0021

test1 = df['move'] == '0021'
filter = test1
df_0021 = df.loc[filter]

df_0021["new-Source3"] = df_0021["Source2"]
df_0021["new-Sutta3"] = df_0021["Sutta2"]
df_0021["new-Example3"] = df_0021["Example2"]
df_0021["new-Pali chant 3"] = df_0021["Pali chant 2"]
df_0021["new-English chant 3"] = df_0021["English chant 2"]
df_0021["new-Chapter 3"] = df_0021["Chapter 2"]

df_0021["Source2"] = ""
df_0021["Sutta2"] = ""
df_0021["Example2"] = ""
df_0021["Pali chant 2"] = ""
df_0021["English chant 2"] = ""
df_0021["Chapter 2"] = ""

df_0021["new-Source4"] = df_0021["Source1"]
df_0021["new-Sutta4"] = df_0021["Sutta1"]
df_0021["new-Example4"] = df_0021["Example1"]
df_0021["new-Pali chant 4"] = df_0021["Pali chant 1"]
df_0021["new-English chant 4"] = df_0021["English chant 1"]
df_0021["new-Chapter 4"] = df_0021["Chapter 1"]

df_0021["Source1"] = ""
df_0021["Sutta1"] = ""
df_0021["Example1"] = ""
df_0021["Pali chant 1"] = ""
df_0021["English chant 1"] = ""
df_0021["Chapter 1"] = ""

df_0021["Source4"] = df_0021["new-Source4"]
df_0021["Sutta4"] = df_0021["new-Sutta4"]
df_0021["Example4"] = df_0021["new-Example4"]
df_0021["Pali chant 4"] = df_0021["new-Pali chant 4"]
df_0021["English chant 4"] = df_0021["new-English chant 4"]
df_0021["Chapter 4"] = df_0021["new-Chapter 4"]

df_0021["Source3"] = df_0021["new-Source3"]
df_0021["Sutta3"] = df_0021["new-Sutta3"]
df_0021["Example3"] = df_0021["new-Example3"]
df_0021["Pali chant 3"] = df_0021["new-Pali chant 3"]
df_0021["English chant 3"] = df_0021["new-English chant 3"]
df_0021["Chapter 3"] = df_0021["new-Chapter 3"]


df_0021 = df_0021[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]
# print(df_0021)

# df_0021.to_csv("../spreadsheets/df_0021.csv", sep="\t", index=None)

# filtering 0023

test1 = df['move'] == '0023'
filter = test1
df_0023 = df.loc[filter]

df_0023["new-Source3"] = df_0023["Source2"]
df_0023["new-Sutta3"] = df_0023["Sutta2"]
df_0023["new-Example3"] = df_0023["Example2"]
df_0023["new-Pali chant 3"] = df_0023["Pali chant 2"]
df_0023["new-English chant 3"] = df_0023["English chant 2"]
df_0023["new-Chapter 3"] = df_0023["Chapter 2"]

df_0023["Source2"] = ""
df_0023["Sutta2"] = ""
df_0023["Example2"] = ""
df_0023["Pali chant 2"] = ""
df_0023["English chant 2"] = ""
df_0023["Chapter 2"] = ""

df_0023["new-Source4"] = df_0023["Source3"]
df_0023["new-Sutta4"] = df_0023["Sutta3"]
df_0023["new-Example4"] = df_0023["Example3"]
df_0023["new-Pali chant 4"] = df_0023["Pali chant 3"]
df_0023["new-English chant 4"] = df_0023["English chant 3"]
df_0023["new-Chapter 4"] = df_0023["Chapter 3"]

df_0023["Source3"] = ""
df_0023["Sutta3"] = ""
df_0023["Example3"] = ""
df_0023["Pali chant 3"] = ""
df_0023["English chant 3"] = ""
df_0023["Chapter 3"] = ""

df_0023["Source4"] = df_0023["new-Source4"]
df_0023["Sutta4"] = df_0023["new-Sutta4"]
df_0023["Example4"] = df_0023["new-Example4"]
df_0023["Pali chant 4"] = df_0023["new-Pali chant 4"]
df_0023["English chant 4"] = df_0023["new-English chant 4"]
df_0023["Chapter 4"] = df_0023["new-Chapter 4"]

df_0023["Source3"] = df_0023["new-Source3"]
df_0023["Sutta3"] = df_0023["new-Sutta3"]
df_0023["Example3"] = df_0023["new-Example3"]
df_0023["Pali chant 3"] = df_0023["new-Pali chant 3"]
df_0023["English chant 3"] = df_0023["new-English chant 3"]
df_0023["Chapter 3"] = df_0023["new-Chapter 3"]


df_0023 = df_0023[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]
# print(df_0023)

# df_0023.to_csv("../spreadsheets/df_0023.csv", sep="\t", index=None)


# filtering 0100

test1 = df['move'] == '0100'
filter = test1
df_0100 = df.loc[filter]

df_0100["new-Source2"] = df_0100["Source1"]
df_0100["new-Sutta2"] = df_0100["Sutta1"]
df_0100["new-Example2"] = df_0100["Example1"]
df_0100["new-Pali chant 2"] = df_0100["Pali chant 1"]
df_0100["new-English chant 2"] = df_0100["English chant 1"]
df_0100["new-Chapter 2"] = df_0100["Chapter 1"]

df_0100["Source1"] = ""
df_0100["Sutta1"] = ""
df_0100["Example1"] = ""
df_0100["Pali chant 1"] = ""
df_0100["English chant 1"] = ""
df_0100["Chapter 1"] = ""

df_0100["Source2"] = df_0100["new-Source2"]
df_0100["Sutta2"] = df_0100["new-Sutta2"]
df_0100["Example2"] = df_0100["new-Example2"]
df_0100["Pali chant 2"] = df_0100["new-Pali chant 2"]
df_0100["English chant 2"] = df_0100["new-English chant 2"]
df_0100["Chapter 2"] = df_0100["new-Chapter 2"]


df_0100 = df_0100[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0100)

# df_0100.to_csv("../spreadsheets/df_0100.csv", sep="\t", index=None)

# filtering 0102

test1 = df['move'] == '0102'
filter = test1
df_0102 = df.loc[filter]

df_0102["new-Source2"] = df_0102["Source1"]
df_0102["new-Sutta2"] = df_0102["Sutta1"]
df_0102["new-Example2"] = df_0102["Example1"]
df_0102["new-Pali chant 2"] = df_0102["Pali chant 1"]
df_0102["new-English chant 2"] = df_0102["English chant 1"]
df_0102["new-Chapter 2"] = df_0102["Chapter 1"]

df_0102["Source1"] = ""
df_0102["Sutta1"] = ""
df_0102["Example1"] = ""
df_0102["Pali chant 1"] = ""
df_0102["English chant 1"] = ""
df_0102["Chapter 1"] = ""

df_0102["new-Source4"] = df_0102["Source2"]
df_0102["new-Sutta4"] = df_0102["Sutta2"]
df_0102["new-Example4"] = df_0102["Example2"]
df_0102["new-Pali chant 4"] = df_0102["Pali chant 2"]
df_0102["new-English chant 4"] = df_0102["English chant 2"]
df_0102["new-Chapter 4"] = df_0102["Chapter 2"]

df_0102["Source2"] = ""
df_0102["Sutta2"] = ""
df_0102["Example2"] = ""
df_0102["Pali chant 2"] = ""
df_0102["English chant 2"] = ""
df_0102["Chapter 2"] = ""

df_0102["Source4"] = df_0102["new-Source4"]
df_0102["Sutta4"] = df_0102["new-Sutta4"]
df_0102["Example4"] = df_0102["new-Example4"]
df_0102["Pali chant 4"] = df_0102["new-Pali chant 4"]
df_0102["English chant 4"] = df_0102["new-English chant 4"]
df_0102["Chapter 4"] = df_0102["new-Chapter 4"]

df_0102["Source2"] = df_0102["new-Source2"]
df_0102["Sutta2"] = df_0102["new-Sutta2"]
df_0102["Example2"] = df_0102["new-Example2"]
df_0102["Pali chant 2"] = df_0102["new-Pali chant 2"]
df_0102["English chant 2"] = df_0102["new-English chant 2"]
df_0102["Chapter 2"] = df_0102["new-Chapter 2"]


df_0102 = df_0102[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0102)

# df_0102.to_csv("../spreadsheets/df_0102.csv", sep="\t", index=None)

# filtering 0120

test1 = df['move'] == '0120'
filter = test1
df_0120 = df.loc[filter]

df_0120["new-Source2"] = df_0120["Source1"]
df_0120["new-Sutta2"] = df_0120["Sutta1"]
df_0120["new-Example2"] = df_0120["Example1"]
df_0120["new-Pali chant 2"] = df_0120["Pali chant 1"]
df_0120["new-English chant 2"] = df_0120["English chant 1"]
df_0120["new-Chapter 2"] = df_0120["Chapter 1"]

df_0120["Source1"] = ""
df_0120["Sutta1"] = ""
df_0120["Example1"] = ""
df_0120["Pali chant 1"] = ""
df_0120["English chant 1"] = ""
df_0120["Chapter 1"] = ""

df_0120["new-Source3"] = df_0120["Source2"]
df_0120["new-Sutta3"] = df_0120["Sutta2"]
df_0120["new-Example3"] = df_0120["Example2"]
df_0120["new-Pali chant 3"] = df_0120["Pali chant 2"]
df_0120["new-English chant 3"] = df_0120["English chant 2"]
df_0120["new-Chapter 3"] = df_0120["Chapter 2"]

df_0120["Source2"] = ""
df_0120["Sutta2"] = ""
df_0120["Example2"] = ""
df_0120["Pali chant 2"] = ""
df_0120["English chant 2"] = ""
df_0120["Chapter 2"] = ""

df_0120["Source3"] = df_0120["new-Source3"]
df_0120["Sutta3"] = df_0120["new-Sutta3"]
df_0120["Example3"] = df_0120["new-Example3"]
df_0120["Pali chant 3"] = df_0120["new-Pali chant 3"]
df_0120["English chant 3"] = df_0120["new-English chant 3"]
df_0120["Chapter 3"] = df_0120["new-Chapter 3"]

df_0120["Source2"] = df_0120["new-Source2"]
df_0120["Sutta2"] = df_0120["new-Sutta2"]
df_0120["Example2"] = df_0120["new-Example2"]
df_0120["Pali chant 2"] = df_0120["new-Pali chant 2"]
df_0120["English chant 2"] = df_0120["new-English chant 2"]
df_0120["Chapter 2"] = df_0120["new-Chapter 2"]


df_0120 = df_0120[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0120)

# df_0120.to_csv("../spreadsheets/df_0120.csv", sep="\t", index=None)

# filtering 0123

test1 = df['move'] == '0123'
filter = test1
df_0123 = df.loc[filter]

df_0123["new-Source2"] = df_0123["Source1"]
df_0123["new-Sutta2"] = df_0123["Sutta1"]
df_0123["new-Example2"] = df_0123["Example1"]
df_0123["new-Pali chant 2"] = df_0123["Pali chant 1"]
df_0123["new-English chant 2"] = df_0123["English chant 1"]
df_0123["new-Chapter 2"] = df_0123["Chapter 1"]

df_0123["Source1"] = ""
df_0123["Sutta1"] = ""
df_0123["Example1"] = ""
df_0123["Pali chant 1"] = ""
df_0123["English chant 1"] = ""
df_0123["Chapter 1"] = ""

df_0123["new-Source3"] = df_0123["Source2"]
df_0123["new-Sutta3"] = df_0123["Sutta2"]
df_0123["new-Example3"] = df_0123["Example2"]
df_0123["new-Pali chant 3"] = df_0123["Pali chant 2"]
df_0123["new-English chant 3"] = df_0123["English chant 2"]
df_0123["new-Chapter 3"] = df_0123["Chapter 2"]

df_0123["Source2"] = ""
df_0123["Sutta2"] = ""
df_0123["Example2"] = ""
df_0123["Pali chant 2"] = ""
df_0123["English chant 2"] = ""
df_0123["Chapter 2"] = ""

df_0123["new-Source4"] = df_0123["Source3"]
df_0123["new-Sutta4"] = df_0123["Sutta3"]
df_0123["new-Example4"] = df_0123["Example3"]
df_0123["new-Pali chant 4"] = df_0123["Pali chant 3"]
df_0123["new-English chant 4"] = df_0123["English chant 3"]
df_0123["new-Chapter 4"] = df_0123["Chapter 3"]

df_0123["Source3"] = ""
df_0123["Sutta3"] = ""
df_0123["Example3"] = ""
df_0123["Pali chant 3"] = ""
df_0123["English chant 3"] = ""
df_0123["Chapter 3"] = ""

df_0123["Source4"] = df_0123["new-Source4"]
df_0123["Sutta4"] = df_0123["new-Sutta4"]
df_0123["Example4"] = df_0123["new-Example4"]
df_0123["Pali chant 4"] = df_0123["new-Pali chant 4"]
df_0123["English chant 4"] = df_0123["new-English chant 4"]
df_0123["Chapter 4"] = df_0123["new-Chapter 4"]

df_0123["Source3"] = df_0123["new-Source3"]
df_0123["Sutta3"] = df_0123["new-Sutta3"]
df_0123["Example3"] = df_0123["new-Example3"]
df_0123["Pali chant 3"] = df_0123["new-Pali chant 3"]
df_0123["English chant 3"] = df_0123["new-English chant 3"]
df_0123["Chapter 3"] = df_0123["new-Chapter 3"]

df_0123["Source2"] = df_0123["new-Source2"]
df_0123["Sutta2"] = df_0123["new-Sutta2"]
df_0123["Example2"] = df_0123["new-Example2"]
df_0123["Pali chant 2"] = df_0123["new-Pali chant 2"]
df_0123["English chant 2"] = df_0123["new-English chant 2"]
df_0123["Chapter 2"] = df_0123["new-Chapter 2"]

df_0123 = df_0123[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0123)

# df_0123.to_csv("../spreadsheets/df_0123.csv", sep="\t", index=None)

# filtering 0300

test1 = df['move'] == '0300'
filter = test1
df_0300 = df.loc[filter]

df_0300["new-Source2"] = df_0300["Source3"]
df_0300["new-Sutta2"] = df_0300["Sutta3"]
df_0300["new-Example2"] = df_0300["Example3"]
df_0300["new-Pali chant 2"] = df_0300["Pali chant 3"]
df_0300["new-English chant 2"] = df_0300["English chant 3"]
df_0300["new-Chapter 2"] = df_0300["Chapter 3"]

df_0300["Source3"] = ""
df_0300["Sutta3"] = ""
df_0300["Example3"] = ""
df_0300["Pali chant 3"] = ""
df_0300["English chant 3"] = ""
df_0300["Chapter 3"] = ""

df_0300["Source2"] = df_0300["new-Source2"]
df_0300["Sutta2"] = df_0300["new-Sutta2"]
df_0300["Example2"] = df_0300["new-Example2"]
df_0300["Pali chant 2"] = df_0300["new-Pali chant 2"]
df_0300["English chant 2"] = df_0300["new-English chant 2"]
df_0300["Chapter 2"] = df_0300["new-Chapter 2"]


df_0300 = df_0300[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0300)

# df_0300.to_csv("../spreadsheets/df_0300.csv", sep="\t", index=None)

# filtering 0310

test1 = df['move'] == '0310'
filter = test1
df_0310 = df.loc[filter]

df_0310["new-Source2"] = df_0310["Source3"]
df_0310["new-Sutta2"] = df_0310["Sutta3"]
df_0310["new-Example2"] = df_0310["Example3"]
df_0310["new-Pali chant 2"] = df_0310["Pali chant 3"]
df_0310["new-English chant 2"] = df_0310["English chant 3"]
df_0310["new-Chapter 2"] = df_0310["Chapter 3"]

df_0310["Source3"] = ""
df_0310["Sutta3"] = ""
df_0310["Example3"] = ""
df_0310["Pali chant 3"] = ""
df_0310["English chant 3"] = ""
df_0310["Chapter 3"] = ""

df_0310["new-Source3"] = df_0310["Source1"]
df_0310["new-Sutta3"] = df_0310["Sutta1"]
df_0310["new-Example3"] = df_0310["Example1"]
df_0310["new-Pali chant 3"] = df_0310["Pali chant 1"]
df_0310["new-English chant 3"] = df_0310["English chant 1"]
df_0310["new-Chapter 3"] = df_0310["Chapter 1"]

df_0310["Source1"] = ""
df_0310["Sutta1"] = ""
df_0310["Example1"] = ""
df_0310["Pali chant 1"] = ""
df_0310["English chant 1"] = ""
df_0310["Chapter 1"] = ""

df_0310["Source3"] = df_0310["new-Source3"]
df_0310["Sutta3"] = df_0310["new-Sutta3"]
df_0310["Example3"] = df_0310["new-Example3"]
df_0310["Pali chant 3"] = df_0310["new-Pali chant 3"]
df_0310["English chant 3"] = df_0310["new-English chant 3"]
df_0310["Chapter 3"] = df_0310["new-Chapter 3"]

df_0310["Source2"] = df_0310["new-Source2"]
df_0310["Sutta2"] = df_0310["new-Sutta2"]
df_0310["Example2"] = df_0310["new-Example2"]
df_0310["Pali chant 2"] = df_0310["new-Pali chant 2"]
df_0310["English chant 2"] = df_0310["new-English chant 2"]
df_0310["Chapter 2"] = df_0310["new-Chapter 2"]


df_0310 = df_0310[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0310)

# df_0310.to_csv("../spreadsheets/df_0310.csv", sep="\t", index=None)

# filtering 0312

test1 = df['move'] == '0312'
filter = test1
df_0312 = df.loc[filter]

df_0312["new-Source2"] = df_0312["Source3"]
df_0312["new-Sutta2"] = df_0312["Sutta3"]
df_0312["new-Example2"] = df_0312["Example3"]
df_0312["new-Pali chant 2"] = df_0312["Pali chant 3"]
df_0312["new-English chant 2"] = df_0312["English chant 3"]
df_0312["new-Chapter 2"] = df_0312["Chapter 3"]

df_0312["Source3"] = ""
df_0312["Sutta3"] = ""
df_0312["Example3"] = ""
df_0312["Pali chant 3"] = ""
df_0312["English chant 3"] = ""
df_0312["Chapter 3"] = ""

df_0312["new-Source3"] = df_0312["Source1"]
df_0312["new-Sutta3"] = df_0312["Sutta1"]
df_0312["new-Example3"] = df_0312["Example1"]
df_0312["new-Pali chant 3"] = df_0312["Pali chant 1"]
df_0312["new-English chant 3"] = df_0312["English chant 1"]
df_0312["new-Chapter 3"] = df_0312["Chapter 1"]

df_0312["Source1"] = ""
df_0312["Sutta1"] = ""
df_0312["Example1"] = ""
df_0312["Pali chant 1"] = ""
df_0312["English chant 1"] = ""
df_0312["Chapter 1"] = ""

df_0312["new-Source4"] = df_0312["Source2"]
df_0312["new-Sutta4"] = df_0312["Sutta2"]
df_0312["new-Example4"] = df_0312["Example2"]
df_0312["new-Pali chant 4"] = df_0312["Pali chant 2"]
df_0312["new-English chant 4"] = df_0312["English chant 2"]
df_0312["new-Chapter 4"] = df_0312["Chapter 2"]

df_0312["Source2"] = ""
df_0312["Sutta2"] = ""
df_0312["Example2"] = ""
df_0312["Pali chant 2"] = ""
df_0312["English chant 2"] = ""
df_0312["Chapter 2"] = ""

df_0312["Source4"] = df_0312["new-Source4"]
df_0312["Sutta4"] = df_0312["new-Sutta4"]
df_0312["Example4"] = df_0312["new-Example4"]
df_0312["Pali chant 4"] = df_0312["new-Pali chant 4"]
df_0312["English chant 4"] = df_0312["new-English chant 4"]
df_0312["Chapter 4"] = df_0312["new-Chapter 4"]

df_0312["Source3"] = df_0312["new-Source3"]
df_0312["Sutta3"] = df_0312["new-Sutta3"]
df_0312["Example3"] = df_0312["new-Example3"]
df_0312["Pali chant 3"] = df_0312["new-Pali chant 3"]
df_0312["English chant 3"] = df_0312["new-English chant 3"]
df_0312["Chapter 3"] = df_0312["new-Chapter 3"]

df_0312["Source2"] = df_0312["new-Source2"]
df_0312["Sutta2"] = df_0312["new-Sutta2"]
df_0312["Example2"] = df_0312["new-Example2"]
df_0312["Pali chant 2"] = df_0312["new-Pali chant 2"]
df_0312["English chant 2"] = df_0312["new-English chant 2"]
df_0312["Chapter 2"] = df_0312["new-Chapter 2"]

df_0312 = df_0312[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0312)

# df_0312.to_csv("../spreadsheets/df_0312.csv", sep="\t", index=None)


# filtering 0320

test1 = df['move'] == '0320'
filter = test1
df_0320 = df.loc[filter]

df_0320["new-Source2"] = df_0320["Source3"]
df_0320["new-Sutta2"] = df_0320["Sutta3"]
df_0320["new-Example2"] = df_0320["Example3"]
df_0320["new-Pali chant 2"] = df_0320["Pali chant 3"]
df_0320["new-English chant 2"] = df_0320["English chant 3"]
df_0320["new-Chapter 2"] = df_0320["Chapter 3"]

df_0320["Source3"] = ""
df_0320["Sutta3"] = ""
df_0320["Example3"] = ""
df_0320["Pali chant 3"] = ""
df_0320["English chant 3"] = ""
df_0320["Chapter 3"] = ""

df_0320["new-Source3"] = df_0320["Source2"]
df_0320["new-Sutta3"] = df_0320["Sutta2"]
df_0320["new-Example3"] = df_0320["Example2"]
df_0320["new-Pali chant 3"] = df_0320["Pali chant 2"]
df_0320["new-English chant 3"] = df_0320["English chant 2"]
df_0320["new-Chapter 3"] = df_0320["Chapter 2"]

df_0320["Source2"] = ""
df_0320["Sutta2"] = ""
df_0320["Example2"] = ""
df_0320["Pali chant 2"] = ""
df_0320["English chant 2"] = ""
df_0320["Chapter 2"] = ""

df_0320["Source3"] = df_0320["new-Source3"]
df_0320["Sutta3"] = df_0320["new-Sutta3"]
df_0320["Example3"] = df_0320["new-Example3"]
df_0320["Pali chant 3"] = df_0320["new-Pali chant 3"]
df_0320["English chant 3"] = df_0320["new-English chant 3"]
df_0320["Chapter 3"] = df_0320["new-Chapter 3"]

df_0320["Source2"] = df_0320["new-Source2"]
df_0320["Sutta2"] = df_0320["new-Sutta2"]
df_0320["Example2"] = df_0320["new-Example2"]
df_0320["Pali chant 2"] = df_0320["new-Pali chant 2"]
df_0320["English chant 2"] = df_0320["new-English chant 2"]
df_0320["Chapter 2"] = df_0320["new-Chapter 2"]


df_0320 = df_0320[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0320)

# df_0320.to_csv("../spreadsheets/df_0320.csv", sep="\t", index=None)


# filtering 0400

test1 = df['move'] == '0400'
filter = test1
df_0400 = df.loc[filter]

df_0400["new-Source2"] = df_0400["Source4"]
df_0400["new-Sutta2"] = df_0400["Sutta4"]
df_0400["new-Example2"] = df_0400["Example4"]
df_0400["new-Pali chant 2"] = df_0400["Pali chant 4"]
df_0400["new-English chant 2"] = df_0400["English chant 4"]
df_0400["new-Chapter 2"] = df_0400["Chapter 4"]

df_0400["Source4"] = ""
df_0400["Sutta4"] = ""
df_0400["Example4"] = ""
df_0400["Pali chant 4"] = ""
df_0400["English chant 4"] = ""
df_0400["Chapter 4"] = ""

df_0400["Source2"] = df_0400["new-Source2"]
df_0400["Sutta2"] = df_0400["new-Sutta2"]
df_0400["Example2"] = df_0400["new-Example2"]
df_0400["Pali chant 2"] = df_0400["new-Pali chant 2"]
df_0400["English chant 2"] = df_0400["new-English chant 2"]
df_0400["Chapter 2"] = df_0400["new-Chapter 2"]


df_0400 = df_0400[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0400)

# df_0400.to_csv("../spreadsheets/df_0400.csv", sep="\t", index=None)


# filtering 0402

test1 = df['move'] == '0402'
filter = test1
df_0402 = df.loc[filter]

df_0402["new-Source2"] = df_0402["Source4"]
df_0402["new-Sutta2"] = df_0402["Sutta4"]
df_0402["new-Example2"] = df_0402["Example4"]
df_0402["new-Pali chant 2"] = df_0402["Pali chant 4"]
df_0402["new-English chant 2"] = df_0402["English chant 4"]
df_0402["new-Chapter 2"] = df_0402["Chapter 4"]

df_0402["Source4"] = ""
df_0402["Sutta4"] = ""
df_0402["Example4"] = ""
df_0402["Pali chant 4"] = ""
df_0402["English chant 4"] = ""
df_0402["Chapter 4"] = ""

df_0402["new-Source4"] = df_0402["Source2"]
df_0402["new-Sutta4"] = df_0402["Sutta2"]
df_0402["new-Example4"] = df_0402["Example2"]
df_0402["new-Pali chant 4"] = df_0402["Pali chant 2"]
df_0402["new-English chant 4"] = df_0402["English chant 2"]
df_0402["new-Chapter 4"] = df_0402["Chapter 2"]

df_0402["Source2"] = ""
df_0402["Sutta2"] = ""
df_0402["Example2"] = ""
df_0402["Pali chant 2"] = ""
df_0402["English chant 2"] = ""
df_0402["Chapter 2"] = ""

df_0402["Source4"] = df_0402["new-Source4"]
df_0402["Sutta4"] = df_0402["new-Sutta4"]
df_0402["Example4"] = df_0402["new-Example4"]
df_0402["Pali chant 4"] = df_0402["new-Pali chant 4"]
df_0402["English chant 4"] = df_0402["new-English chant 4"]
df_0402["Chapter 4"] = df_0402["new-Chapter 4"]

df_0402["Source2"] = df_0402["new-Source2"]
df_0402["Sutta2"] = df_0402["new-Sutta2"]
df_0402["Example2"] = df_0402["new-Example2"]
df_0402["Pali chant 2"] = df_0402["new-Pali chant 2"]
df_0402["English chant 2"] = df_0402["new-English chant 2"]
df_0402["Chapter 2"] = df_0402["new-Chapter 2"]


df_0402 = df_0402[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_0402)

# df_0402.to_csv("../spreadsheets/df_0402.csv", sep="\t", index=None)


# filtering 2000

test1 = df['move'] == '2000'
filter = test1
df_2000 = df.loc[filter]

df_2000["new-Source1"] = df_2000["Source2"]
df_2000["new-Sutta1"] = df_2000["Sutta2"]
df_2000["new-Example1"] = df_2000["Example2"]
df_2000["new-Pali chant 1"] = df_2000["Pali chant 2"]
df_2000["new-English chant 1"] = df_2000["English chant 2"]
df_2000["new-Chapter 1"] = df_2000["Chapter 2"]

df_2000["Source2"] = ""
df_2000["Sutta2"] = ""
df_2000["Example2"] = ""
df_2000["Pali chant 2"] = ""
df_2000["English chant 2"] = ""
df_2000["Chapter 2"] = ""

df_2000["Source1"] = df_2000["new-Source1"]
df_2000["Sutta1"] = df_2000["new-Sutta1"]
df_2000["Example1"] = df_2000["new-Example1"]
df_2000["Pali chant 1"] = df_2000["new-Pali chant 1"]
df_2000["English chant 1"] = df_2000["new-English chant 1"]
df_2000["Chapter 1"] = df_2000["new-Chapter 1"]


df_2000 = df_2000[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_2000)

# df_2000.to_csv("../spreadsheets/df_2000.csv", sep="\t", index=None)


# filtering 2001

test1 = df['move'] == '2001'
filter = test1
df_2001 = df.loc[filter]

df_2001["new-Source1"] = df_2001["Source2"]
df_2001["new-Sutta1"] = df_2001["Sutta2"]
df_2001["new-Example1"] = df_2001["Example2"]
df_2001["new-Pali chant 1"] = df_2001["Pali chant 2"]
df_2001["new-English chant 1"] = df_2001["English chant 2"]
df_2001["new-Chapter 1"] = df_2001["Chapter 2"]

df_2001["Source2"] = ""
df_2001["Sutta2"] = ""
df_2001["Example2"] = ""
df_2001["Pali chant 2"] = ""
df_2001["English chant 2"] = ""
df_2001["Chapter 2"] = ""

df_2001["new-Source4"] = df_2001["Source1"]
df_2001["new-Sutta4"] = df_2001["Sutta1"]
df_2001["new-Example4"] = df_2001["Example1"]
df_2001["new-Pali chant 4"] = df_2001["Pali chant 1"]
df_2001["new-English chant 4"] = df_2001["English chant 1"]
df_2001["new-Chapter 4"] = df_2001["Chapter 1"]

df_2001["Source1"] = ""
df_2001["Sutta1"] = ""
df_2001["Example1"] = ""
df_2001["Pali chant 1"] = ""
df_2001["English chant 1"] = ""
df_2001["Chapter 1"] = ""

df_2001["Source4"] = df_2001["new-Source4"]
df_2001["Sutta4"] = df_2001["new-Sutta4"]
df_2001["Example4"] = df_2001["new-Example4"]
df_2001["Pali chant 4"] = df_2001["new-Pali chant 4"]
df_2001["English chant 4"] = df_2001["new-English chant 4"]
df_2001["Chapter 4"] = df_2001["new-Chapter 4"]

df_2001["Source1"] = df_2001["new-Source1"]
df_2001["Sutta1"] = df_2001["new-Sutta1"]
df_2001["Example1"] = df_2001["new-Example1"]
df_2001["Pali chant 1"] = df_2001["new-Pali chant 1"]
df_2001["English chant 1"] = df_2001["new-English chant 1"]
df_2001["Chapter 1"] = df_2001["new-Chapter 1"]

df_2001 = df_2001[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_2001)

# df_2001.to_csv("../spreadsheets/df_2001.csv", sep="\t", index=None)

# filtering 2010

test1 = df['move'] == '2010'
filter = test1
df_2010 = df.loc[filter]

df_2010["new-Source1"] = df_2010["Source2"]
df_2010["new-Sutta1"] = df_2010["Sutta2"]
df_2010["new-Example1"] = df_2010["Example2"]
df_2010["new-Pali chant 1"] = df_2010["Pali chant 2"]
df_2010["new-English chant 1"] = df_2010["English chant 2"]
df_2010["new-Chapter 1"] = df_2010["Chapter 2"]

df_2010["Source2"] = ""
df_2010["Sutta2"] = ""
df_2010["Example2"] = ""
df_2010["Pali chant 2"] = ""
df_2010["English chant 2"] = ""
df_2010["Chapter 2"] = ""

df_2010["new-Source3"] = df_2010["Source1"]
df_2010["new-Sutta3"] = df_2010["Sutta1"]
df_2010["new-Example3"] = df_2010["Example1"]
df_2010["new-Pali chant 3"] = df_2010["Pali chant 1"]
df_2010["new-English chant 3"] = df_2010["English chant 1"]
df_2010["new-Chapter 3"] = df_2010["Chapter 1"]

df_2010["Source1"] = ""
df_2010["Sutta1"] = ""
df_2010["Example1"] = ""
df_2010["Pali chant 1"] = ""
df_2010["English chant 1"] = ""
df_2010["Chapter 1"] = ""

df_2010["Source3"] = df_2010["new-Source3"]
df_2010["Sutta3"] = df_2010["new-Sutta3"]
df_2010["Example3"] = df_2010["new-Example3"]
df_2010["Pali chant 3"] = df_2010["new-Pali chant 3"]
df_2010["English chant 3"] = df_2010["new-English chant 3"]
df_2010["Chapter 3"] = df_2010["new-Chapter 3"]

df_2010["Source1"] = df_2010["new-Source1"]
df_2010["Sutta1"] = df_2010["new-Sutta1"]
df_2010["Example1"] = df_2010["new-Example1"]
df_2010["Pali chant 1"] = df_2010["new-Pali chant 1"]
df_2010["English chant 1"] = df_2010["new-English chant 1"]
df_2010["Chapter 1"] = df_2010["new-Chapter 1"]

df_2010 = df_2010[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_2010)

# df_2010.to_csv("../spreadsheets/df_2010.csv", sep="\t", index=None)

# filtering 2013

test1 = df['move'] == '2013'
filter = test1
df_2013 = df.loc[filter]

df_2013["new-Source1"] = df_2013["Source2"]
df_2013["new-Sutta1"] = df_2013["Sutta2"]
df_2013["new-Example1"] = df_2013["Example2"]
df_2013["new-Pali chant 1"] = df_2013["Pali chant 2"]
df_2013["new-English chant 1"] = df_2013["English chant 2"]
df_2013["new-Chapter 1"] = df_2013["Chapter 2"]

df_2013["Source2"] = ""
df_2013["Sutta2"] = ""
df_2013["Example2"] = ""
df_2013["Pali chant 2"] = ""
df_2013["English chant 2"] = ""
df_2013["Chapter 2"] = ""

df_2013["new-Source3"] = df_2013["Source1"]
df_2013["new-Sutta3"] = df_2013["Sutta1"]
df_2013["new-Example3"] = df_2013["Example1"]
df_2013["new-Pali chant 3"] = df_2013["Pali chant 1"]
df_2013["new-English chant 3"] = df_2013["English chant 1"]
df_2013["new-Chapter 3"] = df_2013["Chapter 1"]

df_2013["Source1"] = ""
df_2013["Sutta1"] = ""
df_2013["Example1"] = ""
df_2013["Pali chant 1"] = ""
df_2013["English chant 1"] = ""
df_2013["Chapter 1"] = ""

df_2013["new-Source4"] = df_2013["Source3"]
df_2013["new-Sutta4"] = df_2013["Sutta3"]
df_2013["new-Example4"] = df_2013["Example3"]
df_2013["new-Pali chant 4"] = df_2013["Pali chant 3"]
df_2013["new-English chant 4"] = df_2013["English chant 3"]
df_2013["new-Chapter 4"] = df_2013["Chapter 3"]

df_2013["Source3"] = ""
df_2013["Sutta3"] = ""
df_2013["Example3"] = ""
df_2013["Pali chant 3"] = ""
df_2013["English chant 3"] = ""
df_2013["Chapter 3"] = ""

df_2013["Source4"] = df_2013["new-Source4"]
df_2013["Sutta4"] = df_2013["new-Sutta4"]
df_2013["Example4"] = df_2013["new-Example4"]
df_2013["Pali chant 4"] = df_2013["new-Pali chant 4"]
df_2013["English chant 4"] = df_2013["new-English chant 4"]
df_2013["Chapter 4"] = df_2013["new-Chapter 4"]

df_2013["Source3"] = df_2013["new-Source3"]
df_2013["Sutta3"] = df_2013["new-Sutta3"]
df_2013["Example3"] = df_2013["new-Example3"]
df_2013["Pali chant 3"] = df_2013["new-Pali chant 3"]
df_2013["English chant 3"] = df_2013["new-English chant 3"]
df_2013["Chapter 3"] = df_2013["new-Chapter 3"]

df_2013["Source1"] = df_2013["new-Source1"]
df_2013["Sutta1"] = df_2013["new-Sutta1"]
df_2013["Example1"] = df_2013["new-Example1"]
df_2013["Pali chant 1"] = df_2013["new-Pali chant 1"]
df_2013["English chant 1"] = df_2013["new-English chant 1"]
df_2013["Chapter 1"] = df_2013["new-Chapter 1"]

df_2013 = df_2013[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_2013)

# df_2013.to_csv("../spreadsheets/df_2013.csv", sep="\t", index=None)

# filtering 2100

test1 = df['move'] == '2100'
filter = test1
df_2100 = df.loc[filter]

df_2100["new-Source1"] = df_2100["Source2"]
df_2100["new-Sutta1"] = df_2100["Sutta2"]
df_2100["new-Example1"] = df_2100["Example2"]
df_2100["new-Pali chant 1"] = df_2100["Pali chant 2"]
df_2100["new-English chant 1"] = df_2100["English chant 2"]
df_2100["new-Chapter 1"] = df_2100["Chapter 2"]

df_2100["Source2"] = ""
df_2100["Sutta2"] = ""
df_2100["Example2"] = ""
df_2100["Pali chant 2"] = ""
df_2100["English chant 2"] = ""
df_2100["Chapter 2"] = ""

df_2100["new-Source2"] = df_2100["Source1"]
df_2100["new-Sutta2"] = df_2100["Sutta1"]
df_2100["new-Example2"] = df_2100["Example1"]
df_2100["new-Pali chant 2"] = df_2100["Pali chant 1"]
df_2100["new-English chant 2"] = df_2100["English chant 1"]
df_2100["new-Chapter 2"] = df_2100["Chapter 1"]

df_2100["Source1"] = ""
df_2100["Sutta1"] = ""
df_2100["Example1"] = ""
df_2100["Pali chant 1"] = ""
df_2100["English chant 1"] = ""
df_2100["Chapter 1"] = ""

df_2100["Source2"] = df_2100["new-Source2"]
df_2100["Sutta2"] = df_2100["new-Sutta2"]
df_2100["Example2"] = df_2100["new-Example2"]
df_2100["Pali chant 2"] = df_2100["new-Pali chant 2"]
df_2100["English chant 2"] = df_2100["new-English chant 2"]
df_2100["Chapter 2"] = df_2100["new-Chapter 2"]

df_2100["Source1"] = df_2100["new-Source1"]
df_2100["Sutta1"] = df_2100["new-Sutta1"]
df_2100["Example1"] = df_2100["new-Example1"]
df_2100["Pali chant 1"] = df_2100["new-Pali chant 1"]
df_2100["English chant 1"] = df_2100["new-English chant 1"]
df_2100["Chapter 1"] = df_2100["new-Chapter 1"]

df_2100 = df_2100[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_2100)

# df_2100.to_csv("../spreadsheets/df_2100.csv", sep="\t", index=None)

# filtering 2300

test1 = df['move'] == '2300'
filter = test1
df_2300 = df.loc[filter]

df_2300["new-Source1"] = df_2300["Source2"]
df_2300["new-Sutta1"] = df_2300["Sutta2"]
df_2300["new-Example1"] = df_2300["Example2"]
df_2300["new-Pali chant 1"] = df_2300["Pali chant 2"]
df_2300["new-English chant 1"] = df_2300["English chant 2"]
df_2300["new-Chapter 1"] = df_2300["Chapter 2"]

df_2300["Source2"] = ""
df_2300["Sutta2"] = ""
df_2300["Example2"] = ""
df_2300["Pali chant 2"] = ""
df_2300["English chant 2"] = ""
df_2300["Chapter 2"] = ""

df_2300["new-Source2"] = df_2300["Source3"]
df_2300["new-Sutta2"] = df_2300["Sutta3"]
df_2300["new-Example2"] = df_2300["Example3"]
df_2300["new-Pali chant 2"] = df_2300["Pali chant 3"]
df_2300["new-English chant 2"] = df_2300["English chant 3"]
df_2300["new-Chapter 2"] = df_2300["Chapter 3"]

df_2300["Source3"] = ""
df_2300["Sutta3"] = ""
df_2300["Example3"] = ""
df_2300["Pali chant 3"] = ""
df_2300["English chant 3"] = ""
df_2300["Chapter 3"] = ""

df_2300["Source2"] = df_2300["new-Source2"]
df_2300["Sutta2"] = df_2300["new-Sutta2"]
df_2300["Example2"] = df_2300["new-Example2"]
df_2300["Pali chant 2"] = df_2300["new-Pali chant 2"]
df_2300["English chant 2"] = df_2300["new-English chant 2"]
df_2300["Chapter 2"] = df_2300["new-Chapter 2"]

df_2300["Source1"] = df_2300["new-Source1"]
df_2300["Sutta1"] = df_2300["new-Sutta1"]
df_2300["Example1"] = df_2300["new-Example1"]
df_2300["Pali chant 1"] = df_2300["new-Pali chant 1"]
df_2300["English chant 1"] = df_2300["new-English chant 1"]
df_2300["Chapter 1"] = df_2300["new-Chapter 1"]


df_2300 = df_2300[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_2300)

# df_2300.to_csv("../spreadsheets/df_2300.csv", sep="\t", index=None)


# filtering 3000

test1 = df['move'] == '3000'
filter = test1
df_3000 = df.loc[filter]

df_3000["new-Source1"] = df_3000["Source3"]
df_3000["new-Sutta1"] = df_3000["Sutta3"]
df_3000["new-Example1"] = df_3000["Example3"]
df_3000["new-Pali chant 1"] = df_3000["Pali chant 3"]
df_3000["new-English chant 1"] = df_3000["English chant 3"]
df_3000["new-Chapter 1"] = df_3000["Chapter 3"]

df_3000["Source3"] = ""
df_3000["Sutta3"] = ""
df_3000["Example3"] = ""
df_3000["Pali chant 3"] = ""
df_3000["English chant 3"] = ""
df_3000["Chapter 3"] = ""

df_3000["Source1"] = df_3000["new-Source1"]
df_3000["Sutta1"] = df_3000["new-Sutta1"]
df_3000["Example1"] = df_3000["new-Example1"]
df_3000["Pali chant 1"] = df_3000["new-Pali chant 1"]
df_3000["English chant 1"] = df_3000["new-English chant 1"]
df_3000["Chapter 1"] = df_3000["new-Chapter 1"]

df_3000 = df_3000[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_3000)

# df_3000.to_csv("../spreadsheets/df_3000.csv", sep="\t", index=None)

# filtering 3001

test1 = df['move'] == '3001'
filter = test1
df_3001 = df.loc[filter]

df_3001["new-Source1"] = df_3001["Source3"]
df_3001["new-Sutta1"] = df_3001["Sutta3"]
df_3001["new-Example1"] = df_3001["Example3"]
df_3001["new-Pali chant 1"] = df_3001["Pali chant 3"]
df_3001["new-English chant 1"] = df_3001["English chant 3"]
df_3001["new-Chapter 1"] = df_3001["Chapter 3"]

df_3001["Source3"] = ""
df_3001["Sutta3"] = ""
df_3001["Example3"] = ""
df_3001["Pali chant 3"] = ""
df_3001["English chant 3"] = ""
df_3001["Chapter 3"] = ""

df_3001["new-Source4"] = df_3001["Source1"]
df_3001["new-Sutta4"] = df_3001["Sutta1"]
df_3001["new-Example4"] = df_3001["Example1"]
df_3001["new-Pali chant 4"] = df_3001["Pali chant 1"]
df_3001["new-English chant 4"] = df_3001["English chant 1"]
df_3001["new-Chapter 4"] = df_3001["Chapter 1"]

df_3001["Source1"] = ""
df_3001["Sutta1"] = ""
df_3001["Example1"] = ""
df_3001["Pali chant 1"] = ""
df_3001["English chant 1"] = ""
df_3001["Chapter 1"] = ""

df_3001["Source4"] = df_3001["new-Source4"]
df_3001["Sutta4"] = df_3001["new-Sutta4"]
df_3001["Example4"] = df_3001["new-Example4"]
df_3001["Pali chant 4"] = df_3001["new-Pali chant 4"]
df_3001["English chant 4"] = df_3001["new-English chant 4"]
df_3001["Chapter 4"] = df_3001["new-Chapter 4"]

df_3001["Source1"] = df_3001["new-Source1"]
df_3001["Sutta1"] = df_3001["new-Sutta1"]
df_3001["Example1"] = df_3001["new-Example1"]
df_3001["Pali chant 1"] = df_3001["new-Pali chant 1"]
df_3001["English chant 1"] = df_3001["new-English chant 1"]
df_3001["Chapter 1"] = df_3001["new-Chapter 1"]

df_3001 = df_3001[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_3001)

# df_3001.to_csv("../spreadsheets/df_3001.csv", sep="\t", index=None)

# filtering 3010

test1 = df['move'] == '3010'
filter = test1
df_3010 = df.loc[filter]

df_3010["new-Source1"] = df_3010["Source3"]
df_3010["new-Sutta1"] = df_3010["Sutta3"]
df_3010["new-Example1"] = df_3010["Example3"]
df_3010["new-Pali chant 1"] = df_3010["Pali chant 3"]
df_3010["new-English chant 1"] = df_3010["English chant 3"]
df_3010["new-Chapter 1"] = df_3010["Chapter 3"]

df_3010["Source3"] = ""
df_3010["Sutta3"] = ""
df_3010["Example3"] = ""
df_3010["Pali chant 3"] = ""
df_3010["English chant 3"] = ""
df_3010["Chapter 3"] = ""

df_3010["new-Source3"] = df_3010["Source1"]
df_3010["new-Sutta3"] = df_3010["Sutta1"]
df_3010["new-Example3"] = df_3010["Example1"]
df_3010["new-Pali chant 3"] = df_3010["Pali chant 1"]
df_3010["new-English chant 3"] = df_3010["English chant 1"]
df_3010["new-Chapter 3"] = df_3010["Chapter 1"]

df_3010["Source1"] = ""
df_3010["Sutta1"] = ""
df_3010["Example1"] = ""
df_3010["Pali chant 1"] = ""
df_3010["English chant 1"] = ""
df_3010["Chapter 1"] = ""

df_3010["Source3"] = df_3010["new-Source3"]
df_3010["Sutta3"] = df_3010["new-Sutta3"]
df_3010["Example3"] = df_3010["new-Example3"]
df_3010["Pali chant 3"] = df_3010["new-Pali chant 3"]
df_3010["English chant 3"] = df_3010["new-English chant 3"]
df_3010["Chapter 3"] = df_3010["new-Chapter 3"]

df_3010["Source1"] = df_3010["new-Source1"]
df_3010["Sutta1"] = df_3010["new-Sutta1"]
df_3010["Example1"] = df_3010["new-Example1"]
df_3010["Pali chant 1"] = df_3010["new-Pali chant 1"]
df_3010["English chant 1"] = df_3010["new-English chant 1"]
df_3010["Chapter 1"] = df_3010["new-Chapter 1"]


df_3010 = df_3010[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_3010)

# df_3010.to_csv("../spreadsheets/df_3010.csv", sep="\t", index=None)

# filtering 3012

test1 = df['move'] == '3012'
filter = test1
df_3012 = df.loc[filter]

df_3012["new-Source1"] = df_3012["Source3"]
df_3012["new-Sutta1"] = df_3012["Sutta3"]
df_3012["new-Example1"] = df_3012["Example3"]
df_3012["new-Pali chant 1"] = df_3012["Pali chant 3"]
df_3012["new-English chant 1"] = df_3012["English chant 3"]
df_3012["new-Chapter 1"] = df_3012["Chapter 3"]

df_3012["Source3"] = ""
df_3012["Sutta3"] = ""
df_3012["Example3"] = ""
df_3012["Pali chant 3"] = ""
df_3012["English chant 3"] = ""
df_3012["Chapter 3"] = ""

df_3012["new-Source3"] = df_3012["Source1"]
df_3012["new-Sutta3"] = df_3012["Sutta1"]
df_3012["new-Example3"] = df_3012["Example1"]
df_3012["new-Pali chant 3"] = df_3012["Pali chant 1"]
df_3012["new-English chant 3"] = df_3012["English chant 1"]
df_3012["new-Chapter 3"] = df_3012["Chapter 1"]

df_3012["Source1"] = ""
df_3012["Sutta1"] = ""
df_3012["Example1"] = ""
df_3012["Pali chant 1"] = ""
df_3012["English chant 1"] = ""
df_3012["Chapter 1"] = ""

df_3012["new-Source4"] = df_3012["Source2"]
df_3012["new-Sutta4"] = df_3012["Sutta2"]
df_3012["new-Example4"] = df_3012["Example2"]
df_3012["new-Pali chant 4"] = df_3012["Pali chant 2"]
df_3012["new-English chant 4"] = df_3012["English chant 2"]
df_3012["new-Chapter 4"] = df_3012["Chapter 2"]

df_3012["Source2"] = ""
df_3012["Sutta2"] = ""
df_3012["Example2"] = ""
df_3012["Pali chant 2"] = ""
df_3012["English chant 2"] = ""
df_3012["Chapter 2"] = ""

df_3012["Source4"] = df_3012["new-Source4"]
df_3012["Sutta4"] = df_3012["new-Sutta4"]
df_3012["Example4"] = df_3012["new-Example4"]
df_3012["Pali chant 4"] = df_3012["new-Pali chant 4"]
df_3012["English chant 4"] = df_3012["new-English chant 4"]
df_3012["Chapter 4"] = df_3012["new-Chapter 4"]

df_3012["Source3"] = df_3012["new-Source3"]
df_3012["Sutta3"] = df_3012["new-Sutta3"]
df_3012["Example3"] = df_3012["new-Example3"]
df_3012["Pali chant 3"] = df_3012["new-Pali chant 3"]
df_3012["English chant 3"] = df_3012["new-English chant 3"]
df_3012["Chapter 3"] = df_3012["new-Chapter 3"]

df_3012["Source1"] = df_3012["new-Source1"]
df_3012["Sutta1"] = df_3012["new-Sutta1"]
df_3012["Example1"] = df_3012["new-Example1"]
df_3012["Pali chant 1"] = df_3012["new-Pali chant 1"]
df_3012["English chant 1"] = df_3012["new-English chant 1"]
df_3012["Chapter 1"] = df_3012["new-Chapter 1"]


df_3012 = df_3012[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_3012)

# df_3012.to_csv("../spreadsheets/df_3012.csv", sep="\t", index=None)


# filtering 3020

test1 = df['move'] == '3020'
filter = test1
df_3020 = df.loc[filter]

df_3020["new-Source1"] = df_3020["Source3"]
df_3020["new-Sutta1"] = df_3020["Sutta3"]
df_3020["new-Example1"] = df_3020["Example3"]
df_3020["new-Pali chant 1"] = df_3020["Pali chant 3"]
df_3020["new-English chant 1"] = df_3020["English chant 3"]
df_3020["new-Chapter 1"] = df_3020["Chapter 3"]

df_3020["Source3"] = ""
df_3020["Sutta3"] = ""
df_3020["Example3"] = ""
df_3020["Pali chant 3"] = ""
df_3020["English chant 3"] = ""
df_3020["Chapter 3"] = ""

df_3020["new-Source3"] = df_3020["Source2"]
df_3020["new-Sutta3"] = df_3020["Sutta2"]
df_3020["new-Example3"] = df_3020["Example2"]
df_3020["new-Pali chant 3"] = df_3020["Pali chant 2"]
df_3020["new-English chant 3"] = df_3020["English chant 2"]
df_3020["new-Chapter 3"] = df_3020["Chapter 2"]

df_3020["Source2"] = ""
df_3020["Sutta2"] = ""
df_3020["Example2"] = ""
df_3020["Pali chant 2"] = ""
df_3020["English chant 2"] = ""
df_3020["Chapter 2"] = ""

df_3020["Source3"] = df_3020["new-Source3"]
df_3020["Sutta3"] = df_3020["new-Sutta3"]
df_3020["Example3"] = df_3020["new-Example3"]
df_3020["Pali chant 3"] = df_3020["new-Pali chant 3"]
df_3020["English chant 3"] = df_3020["new-English chant 3"]
df_3020["Chapter 3"] = df_3020["new-Chapter 3"]

df_3020["Source1"] = df_3020["new-Source1"]
df_3020["Sutta1"] = df_3020["new-Sutta1"]
df_3020["Example1"] = df_3020["new-Example1"]
df_3020["Pali chant 1"] = df_3020["new-Pali chant 1"]
df_3020["English chant 1"] = df_3020["new-English chant 1"]
df_3020["Chapter 1"] = df_3020["new-Chapter 1"]

df_3020 = df_3020[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_3020)

# df_3020.to_csv("../spreadsheets/df_3020.csv", sep="\t", index=None)

# filtering 3021

test1 = df['move'] == '3021'
filter = test1
df_3021 = df.loc[filter]

df_3021["new-Source1"] = df_3021["Source3"]
df_3021["new-Sutta1"] = df_3021["Sutta3"]
df_3021["new-Example1"] = df_3021["Example3"]
df_3021["new-Pali chant 1"] = df_3021["Pali chant 3"]
df_3021["new-English chant 1"] = df_3021["English chant 3"]
df_3021["new-Chapter 1"] = df_3021["Chapter 3"]

df_3021["Source3"] = ""
df_3021["Sutta3"] = ""
df_3021["Example3"] = ""
df_3021["Pali chant 3"] = ""
df_3021["English chant 3"] = ""
df_3021["Chapter 3"] = ""

df_3021["new-Source3"] = df_3021["Source2"]
df_3021["new-Sutta3"] = df_3021["Sutta2"]
df_3021["new-Example3"] = df_3021["Example2"]
df_3021["new-Pali chant 3"] = df_3021["Pali chant 2"]
df_3021["new-English chant 3"] = df_3021["English chant 2"]
df_3021["new-Chapter 3"] = df_3021["Chapter 2"]

df_3021["Source2"] = ""
df_3021["Sutta2"] = ""
df_3021["Example2"] = ""
df_3021["Pali chant 2"] = ""
df_3021["English chant 2"] = ""
df_3021["Chapter 2"] = ""

df_3021["new-Source4"] = df_3021["Source1"]
df_3021["new-Sutta4"] = df_3021["Sutta1"]
df_3021["new-Example4"] = df_3021["Example1"]
df_3021["new-Pali chant 4"] = df_3021["Pali chant 1"]
df_3021["new-English chant 4"] = df_3021["English chant 1"]
df_3021["new-Chapter 4"] = df_3021["Chapter 1"]

df_3021["Source1"] = ""
df_3021["Sutta1"] = ""
df_3021["Example1"] = ""
df_3021["Pali chant 1"] = ""
df_3021["English chant 1"] = ""
df_3021["Chapter 1"] = ""

df_3021["Source4"] = df_3021["new-Source4"]
df_3021["Sutta4"] = df_3021["new-Sutta4"]
df_3021["Example4"] = df_3021["new-Example4"]
df_3021["Pali chant 4"] = df_3021["new-Pali chant 4"]
df_3021["English chant 4"] = df_3021["new-English chant 4"]
df_3021["Chapter 4"] = df_3021["new-Chapter 4"]

df_3021["Source3"] = df_3021["new-Source3"]
df_3021["Sutta3"] = df_3021["new-Sutta3"]
df_3021["Example3"] = df_3021["new-Example3"]
df_3021["Pali chant 3"] = df_3021["new-Pali chant 3"]
df_3021["English chant 3"] = df_3021["new-English chant 3"]
df_3021["Chapter 3"] = df_3021["new-Chapter 3"]

df_3021["Source1"] = df_3021["new-Source1"]
df_3021["Sutta1"] = df_3021["new-Sutta1"]
df_3021["Example1"] = df_3021["new-Example1"]
df_3021["Pali chant 1"] = df_3021["new-Pali chant 1"]
df_3021["English chant 1"] = df_3021["new-English chant 1"]
df_3021["Chapter 1"] = df_3021["new-Chapter 1"]

df_3021 = df_3021[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_3021)

# df_3021.to_csv("../spreadsheets/df_3021.csv", sep="\t", index=None)


# filtering 4000

test1 = df['move'] == '4000'
filter = test1
df_4000 = df.loc[filter]

df_4000["new-Source1"] = df_4000["Source3"]
df_4000["new-Sutta1"] = df_4000["Sutta3"]
df_4000["new-Example1"] = df_4000["Example3"]
df_4000["new-Pali chant 1"] = df_4000["Pali chant 3"]
df_4000["new-English chant 1"] = df_4000["English chant 3"]
df_4000["new-Chapter 1"] = df_4000["Chapter 3"]

df_4000["Source3"] = ""
df_4000["Sutta3"] = ""
df_4000["Example3"] = ""
df_4000["Pali chant 3"] = ""
df_4000["English chant 3"] = ""
df_4000["Chapter 3"] = ""

df_4000["Source1"] = df_4000["new-Source1"]
df_4000["Sutta1"] = df_4000["new-Sutta1"]
df_4000["Example1"] = df_4000["new-Example1"]
df_4000["Pali chant 1"] = df_4000["new-Pali chant 1"]
df_4000["English chant 1"] = df_4000["new-English chant 1"]
df_4000["Chapter 1"] = df_4000["new-Chapter 1"]


df_4000 = df_4000[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_4000)

# df_4000.to_csv("../spreadsheets/df_4000.csv", sep="\t", index=None)


# filtering 4001

test1 = df['move'] == '4001'
filter = test1
df_4001 = df.loc[filter]

df_4001["new-Source1"] = df_4001["Source3"]
df_4001["new-Sutta1"] = df_4001["Sutta3"]
df_4001["new-Example1"] = df_4001["Example3"]
df_4001["new-Pali chant 1"] = df_4001["Pali chant 3"]
df_4001["new-English chant 1"] = df_4001["English chant 3"]
df_4001["new-Chapter 1"] = df_4001["Chapter 3"]

df_4001["Source3"] = ""
df_4001["Sutta3"] = ""
df_4001["Example3"] = ""
df_4001["Pali chant 3"] = ""
df_4001["English chant 3"] = ""
df_4001["Chapter 3"] = ""

df_4001["new-Source4"] = df_4001["Source1"]
df_4001["new-Sutta4"] = df_4001["Sutta1"]
df_4001["new-Example4"] = df_4001["Example1"]
df_4001["new-Pali chant 4"] = df_4001["Pali chant 1"]
df_4001["new-English chant 4"] = df_4001["English chant 1"]
df_4001["new-Chapter 4"] = df_4001["Chapter 1"]

df_4001["Source1"] = ""
df_4001["Sutta1"] = ""
df_4001["Example1"] = ""
df_4001["Pali chant 1"] = ""
df_4001["English chant 1"] = ""
df_4001["Chapter 1"] = ""

df_4001["Source4"] = df_4001["new-Source4"]
df_4001["Sutta4"] = df_4001["new-Sutta4"]
df_4001["Example4"] = df_4001["new-Example4"]
df_4001["Pali chant 4"] = df_4001["new-Pali chant 4"]
df_4001["English chant 4"] = df_4001["new-English chant 4"]
df_4001["Chapter 4"] = df_4001["new-Chapter 4"]

df_4001["Source1"] = df_4001["new-Source1"]
df_4001["Sutta1"] = df_4001["new-Sutta1"]
df_4001["Example1"] = df_4001["new-Example1"]
df_4001["Pali chant 1"] = df_4001["new-Pali chant 1"]
df_4001["English chant 1"] = df_4001["new-English chant 1"]
df_4001["Chapter 1"] = df_4001["new-Chapter 1"]


df_4001 = df_4001[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_4001)

# df_4001.to_csv("../spreadsheets/df_4001.csv", sep="\t", index=None)

# filtering 4010

test1 = df['move'] == '4010'
filter = test1
df_4010 = df.loc[filter]

df_4010["new-Source1"] = df_4010["Source3"]
df_4010["new-Sutta1"] = df_4010["Sutta3"]
df_4010["new-Example1"] = df_4010["Example3"]
df_4010["new-Pali chant 1"] = df_4010["Pali chant 3"]
df_4010["new-English chant 1"] = df_4010["English chant 3"]
df_4010["new-Chapter 1"] = df_4010["Chapter 3"]

df_4010["Source3"] = ""
df_4010["Sutta3"] = ""
df_4010["Example3"] = ""
df_4010["Pali chant 3"] = ""
df_4010["English chant 3"] = ""
df_4010["Chapter 3"] = ""

df_4010["new-Source3"] = df_4010["Source1"]
df_4010["new-Sutta3"] = df_4010["Sutta1"]
df_4010["new-Example3"] = df_4010["Example1"]
df_4010["new-Pali chant 3"] = df_4010["Pali chant 1"]
df_4010["new-English chant 3"] = df_4010["English chant 1"]
df_4010["new-Chapter 3"] = df_4010["Chapter 1"]

df_4010["Source1"] = ""
df_4010["Sutta1"] = ""
df_4010["Example1"] = ""
df_4010["Pali chant 1"] = ""
df_4010["English chant 1"] = ""
df_4010["Chapter 1"] = ""

df_4010["Source3"] = df_4010["new-Source3"]
df_4010["Sutta3"] = df_4010["new-Sutta3"]
df_4010["Example3"] = df_4010["new-Example3"]
df_4010["Pali chant 3"] = df_4010["new-Pali chant 3"]
df_4010["English chant 3"] = df_4010["new-English chant 3"]
df_4010["Chapter 3"] = df_4010["new-Chapter 3"]

df_4010["Source1"] = df_4010["new-Source1"]
df_4010["Sutta1"] = df_4010["new-Sutta1"]
df_4010["Example1"] = df_4010["new-Example1"]
df_4010["Pali chant 1"] = df_4010["new-Pali chant 1"]
df_4010["English chant 1"] = df_4010["new-English chant 1"]
df_4010["Chapter 1"] = df_4010["new-Chapter 1"]

df_4010 = df_4010[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_4010)

# df_4010.to_csv("../spreadsheets/df_4010.csv", sep="\t", index=None)


# filtering 4100

test1 = df['move'] == '4100'
filter = test1
df_4100 = df.loc[filter]

df_4100["new-Source1"] = df_4100["Source3"]
df_4100["new-Sutta1"] = df_4100["Sutta3"]
df_4100["new-Example1"] = df_4100["Example3"]
df_4100["new-Pali chant 1"] = df_4100["Pali chant 3"]
df_4100["new-English chant 1"] = df_4100["English chant 3"]
df_4100["new-Chapter 1"] = df_4100["Chapter 3"]

df_4100["Source3"] = ""
df_4100["Sutta3"] = ""
df_4100["Example3"] = ""
df_4100["Pali chant 3"] = ""
df_4100["English chant 3"] = ""
df_4100["Chapter 3"] = ""

df_4100["new-Source2"] = df_4100["Source1"]
df_4100["new-Sutta2"] = df_4100["Sutta1"]
df_4100["new-Example2"] = df_4100["Example1"]
df_4100["new-Pali chant 2"] = df_4100["Pali chant 1"]
df_4100["new-English chant 2"] = df_4100["English chant 1"]
df_4100["new-Chapter 2"] = df_4100["Chapter 1"]

df_4100["Source1"] = ""
df_4100["Sutta1"] = ""
df_4100["Example1"] = ""
df_4100["Pali chant 1"] = ""
df_4100["English chant 1"] = ""
df_4100["Chapter 1"] = ""

df_4100["Source2"] = df_4100["new-Source2"]
df_4100["Sutta2"] = df_4100["new-Sutta2"]
df_4100["Example2"] = df_4100["new-Example2"]
df_4100["Pali chant 2"] = df_4100["new-Pali chant 2"]
df_4100["English chant 2"] = df_4100["new-English chant 2"]
df_4100["Chapter 2"] = df_4100["new-Chapter 2"]

df_4100["Source1"] = df_4100["new-Source1"]
df_4100["Sutta1"] = df_4100["new-Sutta1"]
df_4100["Example1"] = df_4100["new-Example1"]
df_4100["Pali chant 1"] = df_4100["new-Pali chant 1"]
df_4100["English chant 1"] = df_4100["new-English chant 1"]
df_4100["Chapter 1"] = df_4100["new-Chapter 1"]

df_4100 = df_4100[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# print(df_4100)

# df_4100.to_csv("../spreadsheets/df_4100.csv", sep="\t", index=None)



# combine all

df_combine = pd.concat([df_empty, df_0000, df_0001, df_0002, df_0003, df_0010, df_0012, df_0013, df_0020, df_0021, df_0023, df_0100, df_0102, df_0120, df_0123, df_0300, df_0310, df_0312, df_0320, df_0400, df_0402, df_2000, df_2001, df_2010, df_2013, df_2100, df_2300, df_3000, df_3001, df_3010, df_3012, df_3020, df_3021, df_4000, df_4001, df_4010, df_4100])

df_combine = df_combine[['ID', 'Pāli1', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]


df_combine.to_csv("../spreadsheets/df_combine.csv", sep="\t", index=None)





