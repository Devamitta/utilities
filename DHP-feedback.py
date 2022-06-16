
import pandas as pd
import random

df = pd.read_csv("/home/deva/Documents/dps/spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

# filter all DHP from Source1
test2 = df['Source1'].str.contains('DHP')
test3 = df['Sutta1'].str.contains('vaggo')
filter = test2 & test3
df_DHP1 = df.loc[filter]

# filter all DHP from Source2
test4 = df['Source 2'].str.contains('DHP')
test5 = df['Sutta2'].str.contains('vaggo')
filter = test4 & test5
df_DHP2 = df.loc[filter]

# if headword from df2 is in df1, then delete whole row from df2

logix = df_DHP2['Pāli1'].isin(df_DHP1['Pāli1'])

df_DHP4 = df_DHP2.drop(df_DHP2[logix].index)

df_combined = df_DHP1.append(df_DHP4)

df_combined.sort_values(by="Pāli1")

# choosing order of columns

df_combined = df_combined[['Pāli1', 'POS', 'Grammar', 'Derived from', 'Neg', 
       'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'Pāli Root', 'Base',  
       'Construction', 'Sanskrit', 'Sk Root', 
       'Variant', 'Commentary', 'Notes', 
       'Source1', 'Sutta1', 'Example1', 'Source 2', 'Sutta2', 'Example 2', 'Test']]

# make Feedback
df_combined.insert(25, 'Feedback', "<a href=\"https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500="+df['Pāli1']+"\">feedback</a>")


# save csv
df_combined.to_csv("/home/deva/Documents/dps/spreadsheets/dhp_bold.csv", sep="\t", index=None)

