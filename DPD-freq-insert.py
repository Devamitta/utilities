import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df_dpd = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df_dpd.fillna("")

df_freq = pd.read_csv("/home/deva/Documents/dps/spreadsheets/frequency-ebt.csv", sep="\t", dtype= str)
df_freq.fillna("")

df_dps = pd.read_csv("/home/deva/Documents/dps/spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("")

df_dps = df_dps[['id', 'sbs_class_anki', 'sbs_index']]

df_dpd["id"] = df_dpd["user_id"]

df_dpd["pali_1-copy"] = df_dpd["pali_1"]

df_dpd = df_dpd.drop(['user_id'], axis=1)

# removing numbers dpd
df_dpd['pali_1'] = df_dpd['pali_1'].str.replace('\d+', '')
df_dpd['pali_1'] = df_dpd['pali_1'].str.replace(' ', '')
df_dpd['pali_1'] = df_dpd['pali_1'].str.replace('.', '')


df_merged = pd.merge(df_dpd, df_freq, how='left')

df_merged["pali_1"] = df_merged["pali_1-copy"]

df_merged = df_merged.drop(['pali_1-copy'], axis=1)

df_merged_2 = pd.merge(df_merged, df_dps, how='left')

df_merged_2.to_csv("/home/deva/Documents/dps/spreadsheets/dpd-freq.csv", sep="\t", index=None)

