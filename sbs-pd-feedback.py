
import pandas as pd

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


# adding feedback
df.reset_index(drop=True, inplace=True)
df['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df.Pāli1 + """&entry.1433863141=Anki">Fix it here</a>."""

# make double tags
# df.insert(40, 'Tags', None)

# replace all chant names with '_'
df['Pali chant 1'] = df['Pali chant 1'].str.replace(' ', '_')
df['Pali chant 2'] = df['Pali chant 2'].str.replace(' ', '_')
df['Pali chant 3'] = df['Pali chant 3'].str.replace(' ', '_')

df["Tags"] = df["Pali chant 1"]

test3 = df['Feedback'] != ""
filter = test3
df.loc[filter, ['Tags']] = df['Pali chant 1'] + " " + df['Pali chant 2'] + " " + df['Pali chant 3']

# sort by Index
df = df.sort_values(by=['Index', 'Example2'])

df = df.drop(['Fin', 'Stem', 'Pattern', 'ex', 'count', 'class'], axis = 1)
print("columns 'Fin', 'Stem', 'Pattern', 'ex', 'count', 'class' - has been dropped")

# save csv
df.to_csv("../csv-for-anki/sbs-pd-feedback.csv", sep="\t", index=None)

