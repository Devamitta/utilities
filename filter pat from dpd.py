
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dpd+sbs.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# remove all SBS words
test2 = df['Test-s'].str.contains('p')
filter = test2
df = df.loc[filter]

# save csv
# df.to_csv("../spreadsheets/df.csv", sep="\t", index=None)


# replace all sutta numbers with '_'
# df['source_1'] = df['source_1'].str.replace(' ', '_')
# df['source_2'] = df['source_2'].str.replace(' ', '_')
# df['sbs_source_3'] = df['sbs_source_3'].str.replace(' ', '_')

# filter all from sutta1
test1 = df["Fin"] != ""
test2 = df['source_1'].str.contains('PAT')
# test3 = df['sutta_1'].str.contains('sutta')
filter = test1 & test2
df_sutta1 = df.loc[filter]

# save csv
# df_sutta1.to_csv("../spreadsheets/df_sutta1.csv", sep="\t", index=None)



# filter all from sutta1
test1 = df["Fin"] != ""
test3 = df['source_2'].str.contains('PAT')
# test3 = df['sutta_1'].str.contains('sutta')
filter = test1 & test3
df_sutta2 = df.loc[filter]

# save csv
# df_sutta2.to_csv("../spreadsheets/df_sutta2.csv", sep="\t", index=None)



# # move examples from 2 to 1
# df_sutta2["source_1"] = df_sutta2["source_2"]
# df_sutta2["sutta_1"] = df_sutta2["sutta_2"]
# df_sutta2["example_1"] = df_sutta2["example_2"]

# df_sutta2["source_2"] = ""
# df_sutta2["sutta_2"] = ""
# df_sutta2["example_2"] = ""


# # move examples from 3 to 1
# df_sutta3["source_1"] = df_sutta3["sbs_source_3"]
# df_sutta3["sutta_1"] = df_sutta3["sbs_sutta_3"]
# df_sutta3["example_1"] = df_sutta3["sbs_example_3"]

# df_sutta2["sbs_source_3"] = ""
# df_sutta2["sbs_sutta_3"] = ""
# df_sutta2["sbs_example_3"] = ""



# if headword from df_sutta2 is in df_sutta1, then delete whole row from df_sutta2

# logix = df_sutta2['pali_1'].isin(df_sutta1['pali_1'])

# df_sutta4 = df_sutta2.drop(df_sutta2[logix].index)

# if headword from df is in df_sutta1, then delete whole row from df

logix = df['pali_1'].isin(df_sutta1['pali_1'])

df = df.drop(df[logix].index)

# save csv
# df.to_csv("../spreadsheets/df_without_1.csv", sep="\t", index=None)

# if headword from df is in df_sutta2, then delete whole row from df

logix = df['pali_1'].isin(df_sutta2['pali_1'])

df = df.drop(df[logix].index)

# save csv
df.to_csv("../spreadsheets/df_without_2.csv", sep="\t", index=None)


# df_combined = pd.concat([df_sutta1, df_sutta2])

# df_combined = df_sutta1.append(df_sutta4)

# df_combined.sort_values(["source_1"], ascending=True, inplace=True)

# choosing order of columns

# df_combined = df_combined[['pali_1', 'pos', 'grammar', 'derived_from', 'neg', 
#        'verb', 'trans', 'plus_case', 'meaning_1', 'ru_meaning', 'root_pali', 'root_base',  
#        'construction', 'sanskrit', 'root_sk', 
#        'variant', 'commentary', 'notes', 
#        'source_1', 'sutta_1', 'example_1', 'source_2', 'sutta_2', 'example_2', 'Test']]

# make Feedback
# df_combined.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500="+df['pali_1']+"\">feedback</a>")

# adding feedback
# df_combined.reset_index(drop=True, inplace=True)
# df_combined['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_combined.pali_1 + """&entry.1433863141=SuttaPitaka">Fix it here</a>."""

# df_combined = df_combined.drop(['Fin', 'stem', 'pattern', 'sbs_meaning', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_index', 'sbs_class_anki', 'count', 'sbs_class'], axis = 1)
# print("columns 'Fin', 'stem', 'pattern', 'sbs_meaning', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_index', 'sbs_class_anki', 'count', 'sbs_class' has been dropped")


# save csv
# df_combined.to_csv("../spreadsheets/sutta-from-dpd.csv", sep="\t", index=None)

