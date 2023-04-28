import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df_dpd = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df_dpd.fillna("")

# df_dpd = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
# df_dpd.fillna("")

df_dpd = df_dpd.drop(['id'], axis=1)

df_dpd["id"] = df_dpd["user_id"]

# df_id_a0 = pd.read_csv("../spreadsheets/id_a0.csv", sep="\t", dtype= str)
# df_id_a0.fillna("")

# df_dpd = pd.concat([df_dpd, df_id_a0])

df_dpd["DPD_source_1"] = df_dpd["source_1"]
df_dpd["DPD_sutta_1"] = df_dpd["sutta_1"]
df_dpd["DPD_example_1"] = df_dpd["example_1"]
df_dpd["DPD_source_2"] = df_dpd["source_2"]
df_dpd["DPD_sutta_2"] = df_dpd["sutta_2"]
df_dpd["DPD_example_2"] = df_dpd["example_2"]

df_dpd["DPD_pos"] = df_dpd['pos']
df_dpd["DPD_grammar"] = df_dpd['grammar']
# df_dpd["DPD_derived_from"] = df_dpd['derived_from']
# df_dpd["DPD_neg"] = df_dpd['neg']
# df_dpd["DPD_verb"] = df_dpd['verb']
# df_dpd["DPD_trans"] = df_dpd['trans']
df_dpd["DPD_plus_case"] = df_dpd['plus_case']
df_dpd["DPD_meaning_1"] = df_dpd["meaning_1"]
df_dpd["DPD_meaning_lit"] = df_dpd["meaning_lit"]
df_dpd["DPD_root_pali"] = df_dpd["root_key"]
df_dpd["DPD_root_base"] = df_dpd["root_base"]
df_dpd["DPD_construction"] = df_dpd["construction"]
df_dpd["DPD_sanskrit"] = df_dpd["sanskrit"]
df_dpd["DPD_variant"] = df_dpd["variant"]
df_dpd["DPD_commentary"] = df_dpd["commentary"]
df_dpd["DPD_notes"] = df_dpd["notes"]
df_dpd["DPD_stem"] = df_dpd["stem"]
df_dpd["DPD_pattern"] = df_dpd["pattern"]

df_dpd = df_dpd[['id', 'DPD_pos', 'DPD_grammar', 'DPD_plus_case', 'DPD_meaning_1', 'DPD_meaning_lit', 'DPD_root_pali', 'DPD_root_base', 'DPD_construction', 'DPD_sanskrit', 'DPD_variant', 'DPD_commentary', 'DPD_notes', 'DPD_source_1', 'DPD_sutta_1', 'DPD_example_1', 'DPD_source_2', 'DPD_sutta_2', 'DPD_example_2', 'DPD_stem', 'DPD_pattern']]

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("")

# df_dps = df_dps.drop(['DPD'], axis = 1)

df_dps_merged = pd.merge(df_dps, df_dpd)

df_dps_merged.to_csv("../spreadsheets/dps-dpd-ex.csv", sep="\t", index=None)
