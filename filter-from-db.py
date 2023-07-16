
import pandas as pd

df = pd.read_csv("../../dpd-db/csvs/dpd-dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# filter all DPS words
test1 = df['ru_meaning'] != ""
# test2 = df['Fin'].str.contains('s')
filter = test1
df_dps = df.loc[filter]

# make all e,pty meaning1 = meaning2
test1 = df_dps['meaning_1'] == ""
filter = test1
df_dps.loc[filter, "meaning_1"] = df_dps.loc[filter, "Buddhadatta"]

df_dps_meaning = df_dps.drop(['Buddhadatta'], axis=1)

# save csv
df_dps_meaning.to_csv("../spreadsheets/dps-full.csv", sep="\t", index=None)




