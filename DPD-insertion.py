import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df_dpd = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df_dpd.fillna("")

df_nid = pd.read_csv("../spreadsheets/nidh_bold.csv", sep="\t", dtype= str)
df_nid.fillna("")

df_nid = df_nid[['ID', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Pāli Root', 'Base', 'Construction', 'Variant', 'Commentary']]

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("")

df_dps = df_dps[['ID']]

# df_dps = df_dps.drop(['Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Pāli Root', 'Base', 'Construction', 'Variant', 'Commentary'], axis = 1)

df_dpd["DPD"] = df_dpd["Fin"]
df_dpd["new"] = "1"

# choosing order of columns


df_dpd = df_dpd[['ID', 'Pāli1', 'DPD', 'Phonetic Changes', 'Notes', 'Derivative', 'Suffix', 'Compound', 'Compound Construction', 'new']]

# df_dps_merged = pd.merge(df_dps, df_dpd, how='left')
df_dps_merged = pd.merge(df_dps, df_nid)

df_dps_merged.to_csv("../spreadsheets/dps+nidh.csv", sep="\t", index=None)
