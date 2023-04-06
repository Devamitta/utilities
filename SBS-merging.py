import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df_nid = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df_nid.fillna("")

df_nid["DPD-Source1"] = df_nid["Source1"]
df_nid["DPD-Sutta1"] = df_nid["Sutta1"]
df_nid["DPD-Example1"] = df_nid["Example1"]
df_nid["DPD-Source2"] = df_nid["Source 2"]
df_nid["DPD-Sutta2"] = df_nid["Sutta2"]
df_nid["DPD-Example2"] = df_nid["Example 2"]

df_nid = df_nid[['ID', 'DPD-Source1', 'DPD-Sutta1', 'DPD-Example1', 'DPD-Source2', 'DPD-Sutta2', 'DPD-Example2']]

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("")

df_dps = df_dps[['ID', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source4', 'Sutta4', 'Example4', 'Pali chant 4', 'English chant 4', 'Chapter 4']]

# choosing order of columns

# df_dps = df_dps[['ID', 'Meaning in native language', 'Fin-s', 'Test-s', 'ex']]

# df_dps_merged = pd.merge(df_dps, df_nid, how='left')
df_dps_merged = pd.merge(df_dps, df_nid, how='left')

df_dps_merged.to_csv("../spreadsheets/examples.csv", sep="\t", index=None)