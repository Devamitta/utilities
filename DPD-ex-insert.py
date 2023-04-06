import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df_dpd = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df_dpd.fillna("")

# df_nid = pd.read_csv("../spreadsheets/nidh_bold.csv", sep="\t", dtype= str)
# df_nid.fillna("")

df_dpd["DPD"] = df_dpd["Fin"]

df_dpd["DPD-Source1"] = df_dpd["Source1"]
df_dpd["DPD-Sutta1"] = df_dpd["Sutta1"]
df_dpd["DPD-Example1"] = df_dpd["Example1"]
df_dpd["DPD-Source2"] = df_dpd["Source 2"]
df_dpd["DPD-Sutta2"] = df_dpd["Sutta2"]
df_dpd["DPD-Example2"] = df_dpd["Example 2"]


df_dpd = df_dpd[['ID', 'DPD', 'DPD-Source1', 'DPD-Sutta1', 'DPD-Example1', 'DPD-Source2', 'DPD-Sutta2', 'DPD-Example2']]

df_dps = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df_dps.fillna("")

df_dps = df_dps.drop(['DPD'], axis = 1)


# df_dps = df_dps[['ID']]



# df_dpd["DPD"] = df_dpd["Fin"]
# df_dpd["new"] = "1"

# choosing order of columns


# df_dpd = df_dpd[['ID', 'Pāli1', 'DPD', 'Phonetic Changes', 'Notes', 'Derivative', 'Suffix', 'Compound', 'Compound Construction', 'new']]

# df_dps_merged = pd.merge(df_dps, df_dpd, how='left')
df_dps_merged = pd.merge(df_dps, df_dpd)

df_dps_merged.to_csv("../spreadsheets/dps-dpd-ex.csv", sep="\t", index=None)
