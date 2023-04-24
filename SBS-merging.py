import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df_nid = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df_nid.fillna("")

df_nid["DPD_source_1"] = df_nid["source_1"]
df_nid["DPD_sutta_1"] = df_nid["sutta_1"]
df_nid["DPD_example_1"] = df_nid["example_1"]
df_nid["DPD_source_2"] = df_nid["source_2"]
df_nid["DPD_sutta_2"] = df_nid["sutta_2"]
df_nid["DPD_example_2"] = df_nid["example_2"]

df_nid = df_nid[['id', 'DPD_source_1', 'DPD_sutta_1', 'DPD_example_1', 'DPD_source_2', 'DPD_sutta_2', 'DPD_example_2']]

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("")

df_dps = df_dps[['id', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_source_4', 'sbs_sutta_4', 'sbs_example_4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4']]

# choosing order of columns

# df_dps = df_dps[['id', 'ru_meaning', 'Fin-s', 'Test-s', 'sbs_class_anki']]

# df_dps_merged = pd.merge(df_dps, df_nid, how='left')
df_dps_merged = pd.merge(df_dps, df_nid, how='left')

df_dps_merged.to_csv("../spreadsheets/examples.csv", sep="\t", index=None)