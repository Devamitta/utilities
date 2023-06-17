
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change ru_meaning
test1 = df['pali_1'] != ""
filter = test1
df.loc[filter, ['ru_meaning']] = ""

# remove all SBS words
test2 = ~df['Fin'].str.contains('s')
filter = test2
df = df.loc[filter]

# replace all sutta numbers with '_'
df['source_1'] = df['source_1'].str.replace(' ', '_')
df['source_2'] = df['source_2'].str.replace(' ', '_')
df['sbs_source_3'] = df['sbs_source_3'].str.replace(' ', '_')
df['sbs_source_4'] = df['sbs_source_4'].str.replace(' ', '_')

# filter all DN, AN, MN, SN from source_1
test2 = df['source_1'].str.contains('DN_|MN_|SN_|(^AN_)')
# test3 = df['sutta_1'].str.contains('sutta')
filter = test2
df_sutta1 = df.loc[filter]

# filter all DHP from source_2
test2 = ~df['source_1'].str.contains('DN_|MN_|SN_|(^AN_)')
test4 = df['source_2'].str.contains('DN_|MN_|SN_|(^AN_)')
# test5 = df['sutta_2'].str.contains('vaggo')
filter = test2 & test4
df_sutta2 = df.loc[filter]

# # move examples from 2 to 1
# df_sutta2["source_1"] = df_sutta2["source_2"]
# df_sutta2["sutta_1"] = df_sutta2["sutta_2"]
# df_sutta2["example_1"] = df_sutta2["example_2"]

# df_sutta2["source_2"] = ""
# df_sutta2["sutta_2"] = ""
# df_sutta2["example_2"] = ""

# filter all DHP from sbs_source_3
test2 = ~df['source_1'].str.contains('DN_|MN_|SN_|(^AN_)')
test3 = ~df['source_2'].str.contains('DN_|MN_|SN_|(^AN_)')
test4 = df['sbs_source_3'].str.contains('DN_|MN_|SN_|(^AN_)')
# test5 = df['sbs_sutta_3'].str.contains('vaggo')
filter = test2 & test3 & test4
df_sutta3 = df.loc[filter]

# # move examples from 3 to 1
# df_sutta3["source_1"] = df_sutta3["sbs_source_3"]
# df_sutta3["sutta_1"] = df_sutta3["sbs_sutta_3"]
# df_sutta3["example_1"] = df_sutta3["sbs_example_3"]

# df_sutta2["sbs_source_3"] = ""
# df_sutta2["sbs_sutta_3"] = ""
# df_sutta2["sbs_example_3"] = ""


# filter all DHP from sbs_source_4
test2 = ~df['source_1'].str.contains('DN_|MN_|SN_|(^AN_)')
test3 = ~df['source_2'].str.contains('DN_|MN_|SN_|(^AN_)')
test4 = ~df['sbs_source_3'].str.contains('DN_|MN_|SN_|(^AN_)')
test5 = df['sbs_source_4'].str.contains('DN_|MN_|SN_|(^AN_)')
# test6 = df['sbs_sutta_3'].str.contains('vaggo')
filter = test2 & test3 & test4 & test5
df_sutta4 = df.loc[filter]


# if headword from df2 is in df1, then delete whole row from df2

# logix = df_sutta2['pali_1'].isin(df_sutta1['pali_1'])

# df_sutta4 = df_sutta2.drop(df_sutta2[logix].index)

df_combined = pd.concat([df_sutta1, df_sutta2, df_sutta3, df_sutta4])

# df_combined = df_sutta1.append(df_sutta4)

df_combined.sort_values(["source_1"], ascending=True, inplace=True)

# choosing order of columns

# df_combined = df_combined[['pali_1', 'pos', 'grammar', 'derived_from', 'neg', 
#        'verb', 'trans', 'plus_case', 'meaning_1', 'ru_meaning', 'root_pali', 'root_base',  
#        'construction', 'sanskrit', 'root_sk', 
#        'variant', 'commentary', 'notes', 
#        'source_1', 'sutta_1', 'example_1', 'source_2', 'sutta_2', 'example_2', 'Test']]

# make Feedback
# df_combined.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500="+df['pali_1']+"\">feedback</a>")

# adding feedback
df_combined.reset_index(drop=True, inplace=True)
df_combined['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_combined.pali_1 + """&entry.1433863141=SuttaPitaka">Fix it here</a>."""

df_combined = df_combined.drop(['sbs_category', 'Fin', 'stem', 'pattern', 'sbs_meaning', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4', 'sbs_index', 'sbs_class_anki', 'count', 'sbs_class', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes'], axis = 1)
print("columns 'sbs_category', 'Fin', 'stem', 'pattern', 'sbs_meaning', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4', 'sbs_index', 'sbs_class_anki', 'count', 'sbs_class', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes' has been dropped")


# save csv
df_combined.to_csv("../csv-for-anki/sutta-pitaka.csv", sep="\t", index=None)

