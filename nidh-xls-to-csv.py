import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re


# read ods df_nidh
df_nidh = pd.read_excel("../spreadsheets/nidh_bold.xlsx", dtype=str)
df_nidh.fillna("", inplace=True)
# df_a_masc = pd.read_excel("declensions & conjugations.xlsx", sheet_name="index", dtype=str)

# # adding feedback df_a_masc
# df_a_masc.reset_index(drop=True, inplace=True)
# df_a_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_a_masc.pali + """&entry.1433863141=Pāli Class Grammar">Fix it here</a>."""

# save csv df_a_masc
df_nidh.to_csv("../spreadsheets/nidh_bold.csv", sep="\t", index=None)
