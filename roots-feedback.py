
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

# filter all words with roots
test2 = df['Pāli Root'] != "" 
filter = test2
df_roots = df.loc[filter]

df_roots.sort_values(["Source1"], ascending=True, inplace=True)

# adding feedback
df_roots.reset_index(drop=True, inplace=True)
df_roots['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_roots.Pāli1 + """&entry.1433863141=SuttaPitaka">Fix it here</a>."""

df_roots = df_roots.drop(['Fin', 'Stem', 'Pattern', 'Meaning in SBS-PER', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Index', 'ex', 'count', 'class'], axis = 1)
print("columns 'Fin', 'Stem', 'Pattern', 'Meaning in SBS-PER', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Index', 'ex', 'count', 'class' has been dropped")


# save csv
df_roots.to_csv("../csv-for-anki/roots.csv", sep="\t", index=None)

