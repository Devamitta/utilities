import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df_dpd = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df_dpd.fillna("")

df_freq = pd.read_csv("/home/deva/Documents/dps/spreadsheets/frequency-ebt.csv", sep="\t", dtype= str)
df_freq.fillna("")


df_dpd["id-copy"] = df_dpd["user_id"]

df_dpd["pali_1-copy"] = df_dpd["pali_1"]

df_dpd = df_dpd.drop(['id'], axis=1)

# removing numbers dpd
df_dpd['pali_1'] = df_dpd['pali_1'].str.replace('\d+', '')
df_dpd['pali_1'] = df_dpd['pali_1'].str.replace(' ', '')
df_dpd['pali_1'] = df_dpd['pali_1'].str.replace('.', '')


df_merged = pd.merge(df_dpd, df_freq, how='left')


df_merged["pali_1"] = df_merged["pali_1-copy"]

df_merged = df_merged.drop(['pali_1-copy'], axis=1)

df_merged.to_csv("/home/deva/Documents/dps/spreadsheets/dpd-freq.csv", sep="\t", index=None)



# df_dpd = df_dpd[['id', 'DPD_pos', 'DPD_grammar', 'DPD_plus_case', 'DPD_meaning_1', 'DPD_meaning_lit', 'DPD_root_pali', 'DPD_root_base', 'DPD_construction', 'DPD_sanskrit', 'DPD_variant', 'DPD_commentary', 'DPD_notes', 'DPD_source_1', 'DPD_sutta_1', 'DPD_example_1', 'DPD_source_2', 'DPD_sutta_2', 'DPD_example_2', 'DPD_stem', 'DPD_pattern']]


# df_dps = df_dps.drop(['DPD'], axis = 1)

