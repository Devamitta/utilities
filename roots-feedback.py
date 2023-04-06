
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

df_roots.sort_values(["Source1"], ascending=True, inplace=True)

# adding feedback
df_roots.reset_index(drop=True, inplace=True)
df_roots['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_roots.Pāli1 + """&entry.1433863141=SuttaPitaka">Fix it here</a>."""

# filter all words only roots
test2 = df['Pāli Root'] != "" 
test3 = ~df['Phonetic Changes'] != "" 
filter = test2 & test3
df_roots = df.loc[filter]

# filter all words only change
test4 = df['Phonetic Changes'] != "" 
filter = test4
df_change = df.loc[filter]

df_combined = pd.concat([df_roots, df_change])

df_combined = df_combined.drop(['Fin', 'Stem', 'Pattern', 'Meaning in SBS-PER', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Pali chant 4', 'English chant 4', 'Chapter 4', 'Index', 'count', 'class', 'Pāli-old', 'eng-old', 'DPD', 'move', 'sync'], axis = 1)
print("columns 'Fin', 'Stem', 'Pattern', 'Meaning in SBS-PER', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Pali chant 4', 'English chant 4', 'Chapter 4', 'Index', 'count', 'class', 'Pāli-old', 'eng-old', 'DPD', 'move', 'sync' has been dropped for root csv")

# save csv
df_combined.to_csv("../csv-for-anki/roots.csv", sep="\t", index=None)

