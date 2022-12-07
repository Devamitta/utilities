
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

# remove all SBS words
test2 = ~df['Fin'].str.contains('s')
filter = test2
df = df.loc[filter]

# replace all sutta numbers with '_'
df['Source1'] = df['Source1'].str.replace(' ', '_')
df['Source2'] = df['Source2'].str.replace(' ', '_')
df['Source3'] = df['Source3'].str.replace(' ', '_')

# filter all DN, AN, MN, SN from Source1
test2 = df['Source1'].str.contains('DN_|MN_|SN_|(^AN_)')
# test3 = df['Sutta1'].str.contains('sutta')
filter = test2
df_sutta1 = df.loc[filter]

# filter all DHP from Source2
test2 = ~df['Source1'].str.contains('DN_|MN_|SN_|(^AN_)')
test4 = df['Source2'].str.contains('DN_|MN_|SN_|(^AN_)')
# test5 = df['Sutta2'].str.contains('vaggo')
filter = test2 & test4
df_sutta2 = df.loc[filter]

# # move examples from 2 to 1
# df_sutta2["Source1"] = df_sutta2["Source2"]
# df_sutta2["Sutta1"] = df_sutta2["Sutta2"]
# df_sutta2["Example1"] = df_sutta2["Example2"]

# df_sutta2["Source2"] = ""
# df_sutta2["Sutta2"] = ""
# df_sutta2["Example2"] = ""

# filter all DHP from Source3
test2 = ~df['Source1'].str.contains('DN_|MN_|SN_|(^AN_)')
test3 = ~df['Source2'].str.contains('DN_|MN_|SN_|(^AN_)')
test4 = df['Source3'].str.contains('DN_|MN_|SN_|(^AN_)')
# test5 = df['Sutta3'].str.contains('vaggo')
filter = test2 & test3 & test4
df_sutta3 = df.loc[filter]

# # move examples from 3 to 1
# df_sutta3["Source1"] = df_sutta3["Source3"]
# df_sutta3["Sutta1"] = df_sutta3["Sutta3"]
# df_sutta3["Example1"] = df_sutta3["Example3"]

# df_sutta2["Source3"] = ""
# df_sutta2["Sutta3"] = ""
# df_sutta2["Example3"] = ""



# if headword from df2 is in df1, then delete whole row from df2

# logix = df_sutta2['Pāli1'].isin(df_sutta1['Pāli1'])

# df_sutta4 = df_sutta2.drop(df_sutta2[logix].index)

df_combined = pd.concat([df_sutta1, df_sutta2, df_sutta3])

# df_combined = df_sutta1.append(df_sutta4)

df_combined.sort_values(["Source1"], ascending=True, inplace=True)

# choosing order of columns

# df_combined = df_combined[['Pāli1', 'POS', 'Grammar', 'Derived from', 'Neg', 
#        'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'Pāli Root', 'Base',  
#        'Construction', 'Sanskrit', 'Sk Root', 
#        'Variant', 'Commentary', 'Notes', 
#        'Source1', 'Sutta1', 'Example1', 'Source2', 'Sutta2', 'Example2', 'Test']]

# make Feedback
# df_combined.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500="+df['Pāli1']+"\">feedback</a>")

# adding feedback
df_combined.reset_index(drop=True, inplace=True)
df_combined['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_combined.Pāli1 + """&entry.1433863141=SuttaPitaka">Fix it here</a>."""

df_combined = df_combined.drop(['Fin', 'Stem', 'Pattern', 'Meaning in SBS-PER', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Index', 'ex', 'count', 'class'], axis = 1)
print("columns 'Fin', 'Stem', 'Pattern', 'Meaning in SBS-PER', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Index', 'ex', 'count', 'class' has been dropped")


# save csv
df_combined.to_csv("../csv-for-anki/sutta-pitaka.csv", sep="\t", index=None)

