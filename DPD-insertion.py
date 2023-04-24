import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df_dpd = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df_dpd.fillna("")

df_nid = pd.read_csv("../spreadsheets/nidh_bold.csv", sep="\t", dtype= str)
df_nid.fillna("")

df_nid = df_nid[['id', 'derived_from', 'neg', 'verb', 'trans', 'plus_case', 'meaning_1', 'root_pali', 'root_base', 'construction', 'variant', 'commentary']]

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("")

df_dps = df_dps[['id']]

# df_dps = df_dps.drop(['derived_from', 'neg', 'verb', 'trans', 'plus_case', 'meaning_1', 'root_pali', 'root_base', 'construction', 'variant', 'commentary'], axis = 1)

df_dpd["DPD"] = df_dpd["Fin"]
df_dpd["new"] = "1"

# choosing order of columns


df_dpd = df_dpd[['id', 'pali_1', 'DPD', 'phonetic', 'notes', 'derivative', 'suffix', 'compound_type', 'compound_construction', 'new']]

# df_dps_merged = pd.merge(df_dps, df_dpd, how='left')
df_dps_merged = pd.merge(df_dps, df_nid)

df_dps_merged.to_csv("../spreadsheets/dps+nidh.csv", sep="\t", index=None)
