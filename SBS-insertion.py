import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df_nid = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df_nid.fillna("")

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("")

df_dps["Fin-s"] = df_dps["Fin"]
df_dps["Test-s"] = df_dps["Test"]

# choosing order of columns

df_dps = df_dps[['ID', 'Meaning in native language', 'Fin-s', 'Test-s', 'ex']]

# df_dps_merged = pd.merge(df_dps, df_nid, how='left')
df_dps_merged = pd.merge(df_nid, df_dps, how='left')

df_dps_merged.to_csv("../spreadsheets/dpd+sbs.csv", sep="\t", index=None)