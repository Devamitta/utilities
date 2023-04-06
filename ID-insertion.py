import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df_nid = pd.read_csv("../spreadsheets/nidh_id.csv", sep="\t", dtype= str)
df_nid.fillna("")

df_dps = pd.read_csv("../spreadsheets/dps.ods-pali.csv", sep="\t", dtype= str)
df_dps.fillna("")

df_dps_merged = pd.merge(df_dps, df_nid, how='left')

df_dps_merged.to_csv("../spreadsheets/dps-ID.csv", sep="\t", index=None)
