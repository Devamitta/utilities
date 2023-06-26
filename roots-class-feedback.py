
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# adding feedback
# df_roots.reset_index(drop=True, inplace=True)
df['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df.pali_1 + """&entry.1433863141=Roots">Fix it here</a>."""

# change ru_meaning
test1 = df['pali_1'] != ""
filter = test1
df.loc[filter, ['ru_meaning']] = ""

# filter all words from class
test1 = df['sbs_class_anki'] != "" 
filter = test1
df = df.loc[filter]

# filter all words only roots
test2 = df['root_pali'] != "" 
# test3 = df['phonetic'] == "" 
filter = test2
df_roots = df.loc[filter]

# filter all words only change
# test4 = df['phonetic'] != "" 
# filter = test4
# df_change = df.loc[filter]

# df_combined = pd.concat([df_roots, df_change])

df_roots = df_roots.drop(['sbs_category', 'Fin', 'stem', 'pattern', 'sbs_meaning', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4', 'sbs_index', 'count', 'sbs_class', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes'], axis = 1)
# print("columns 'sbs_category',  'Fin', 'stem', 'pattern', 'sbs_meaning', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4', 'sbs_index', 'count', 'sbs_class', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes' has been dropped for class root csv")


# save csv
df_roots.to_csv("../csv-for-anki/classes/roots-class.csv", sep="\t", index=None)

