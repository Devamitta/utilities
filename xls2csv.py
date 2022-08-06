import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
import sys

file_path = sys.argv[1]

print(f"converting {file_path} to csv")

# read ods df
df = pd.read_excel(f"{file_path}",dtype=str)
df.fillna("", inplace=True)

print(f"opening xlsx")

# save csv df_a_masc
df.to_csv(f"{file_path}.csv", sep="\t", index=None)

print(f"saving csv")

rows = df.shape[0]
columns = df.shape[1]

print(f" {file_path}.csv {rows} rows {columns} columns")
