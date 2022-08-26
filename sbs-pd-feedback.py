
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

# filter all SBS words
test2 = df['Fin'].str.contains('s')
filter = test2
df = df.loc[filter]

# make Feedback
# df.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500="+df['Pāli1']+"\">feedback</a>")

# adding feedback
df.reset_index(drop=True, inplace=True)
df['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df.Pāli1 + """&entry.1433863141=Anki">Fix it here</a>."""

# make double tags
df.insert(40, 'Tags', None)

# replace all chant names with '_'
df['Pali chant 2'] = df['Pali chant 2'].str.replace(' ', '_')
df['Pali chant 3'] = df['Pali chant 3'].str.replace(' ', '_')

df["Tags"] = df["Pali chant 2"]

test3 = df['Pali chant 3'] != ""
filter = test3
df.loc[filter, ['Tags']] = df['Pali chant 2'] + " " + df['Pali chant 3']

# sort by Index
df = df.sort_values(by=['Index', 'Example2'])

# save csv
df.to_csv("../spreadsheets/sbs-pd.csv", sep="\t", index=None)

