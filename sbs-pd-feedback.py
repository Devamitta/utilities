
import pandas as pd

df = pd.read_csv("../spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change ru_meaning
test1 = df['pali_1'] != ""
filter = test1
df.loc[filter, ['ru_meaning']] = ""

# filter all SBS words
test2 = df['Fin'].str.contains('s')
filter = test2
df = df.loc[filter]


# adding feedback
df.reset_index(drop=True, inplace=True)
df['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df.pali_1 + """&entry.1433863141=Anki">Fix it here</a>."""

# make double tags
# df.insert(40, 'Tags', None)

# replace all chant names with '_'
df['sbs_chant_pali_1'] = df['sbs_chant_pali_1'].str.replace(' ', '_')
df['sbs_chant_pali_2'] = df['sbs_chant_pali_2'].str.replace(' ', '_')
df['sbs_chant_pali_3'] = df['sbs_chant_pali_3'].str.replace(' ', '_')
df['sbs_chant_pali_4'] = df['sbs_chant_pali_4'].str.replace(' ', '_')

df["Tags"] = df["sbs_chant_pali_1"]

test3 = df['Feedback'] != ""
filter = test3
df.loc[filter, ['Tags']] = df['sbs_chant_pali_1'] + " " + df['sbs_chant_pali_2'] + " " + df['sbs_chant_pali_3'] + " " + df['sbs_chant_pali_4']

# sort by sbs_index
df = df.sort_values(by=['sbs_index', 'example_2'])

df = df.drop(['Fin', 'stem', 'pattern', 'sbs_class_anki', 'count', 'sbs_class', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes'], axis = 1)
print("columns 'Fin', 'stem', 'pattern', 'sbs_class_anki', 'count', 'sbs_class', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes' - has been dropped")

# save csv
df.to_csv("../csv-for-anki/sbs-pd-feedback.csv", sep="\t", index=None)

