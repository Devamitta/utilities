
import pandas as pd
from pandas_ods_reader import read_ods 
import re

df = pd.read_csv("/home/deva/Documents/dpd-db/csvs/dpd-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# print(df['Pāli Root'].dtype)

# concat Pali Root
# root_clean = re.sub(" //d*$", "", root)
df['Root Clean'] = df['Pāli Root'].str.replace(" \d.*$", "", regex=True)
# df['Root Clean'] = df['Pāli Root'].str.replace('[^\w\s]','', regex=True)
# df['Root Clean'] = df['Pāli Root'].str.replace('[^\w\s]','')
test1 = df['Pāli Root'] != ""
test2 = df['Pāli1'] != ""
filter = test1 & test2
df.loc[filter, ['Pāli Root']] = df['Root Clean'] + " " + df['Grp'] + " " + df['Sgn'] + " " + "(" + "to " + df['Root Meaning'] + ")"

# concat English Meaning
# test3 = df['meaning_lit'] != ""
# filter = test3 & test2
# df.loc[filter, ['Meaning IN CONTEXT']] = df['Meaning IN CONTEXT'] + "; lit. " + df['meaning_lit']

# concat Notes and phonetic
# test4 = df['phonetic'] != ""
# test5 = df['notes'] != ""
# test6 = df['notes'] == ""
# filter = test4 & test2 & test5
# df.loc[filter, ['notes']] = df['notes'] + "<br/>" + df['phonetic']
# filter = test4 & test2 & test6
# df.loc[filter, ['notes']] = df['notes'] + df['phonetic']

# df['DPD'] = df['Fin']

# change FIN
test3 = df['Example 2'] != ""
test4 = df['Example1'] != ""
filter = test2 & test3 & test4
df.loc[filter, ['Fin']] = "nn"

test3 = df['Example 2'] == ""
test4 = df['Example1'] != ""
filter = test2 & test3 & test4
df.loc[filter, ['Fin']] = "n"

test3 = df['Example 2'] == ""
test4 = df['Example1'] == ""
filter = test2 & test3 & test4
df.loc[filter, ['Fin']] = ""


# managing Grammar
test4 = df['POS'] == df['Grammar']
# test4 = df['POS'].str.contains(fr"{df['Grammar']}")
filter = test4
df.loc[filter, ['Grammar']] = ""


# if POS in Grammar then remove POS from nothing in Grammar
df['Grammar']=df.apply(lambda x: x['Grammar'].replace(x['Derived from'], ""), axis=1)

df['Grammar']=df.apply(lambda x: x['Grammar'].replace(x['POS'], ""), axis=1)

df['Grammar']=df.apply(lambda x: x['Grammar'].replace("na", ""), axis=1)

# cleaning Grammar
df['Grammar'] = df['Grammar'].replace(' of ', '', regex=True)

df['Grammar'] = df['Grammar'].replace('of', '', regex=True)

df['Grammar'] = df['Grammar'].replace(' from ', '', regex=True)

df['Grammar'] = df['Grammar'].replace({r'^(,)'}, '',  regex=True)

df['Grammar'] = df['Grammar'].replace({r'^( )'}, '',  regex=True)

df['Grammar'] = df['Grammar'].replace({r'( )$'}, '',  regex=True)

df['Grammar'] = df['Grammar'].replace({r'(,)$'}, '',  regex=True)

df['Grammar'] = df['Grammar'].replace({r'^(, )'}, '',  regex=True)

# choosing order of columns

df.insert(17, 'variant', df['Variant – same constr or diff reading'])
df.insert(2, 'sbs_class_anki', None)
df.insert(3, 'sbs_category', None)
df.insert(10, 'ru_meaning', None)
df.insert(11, 'ru_meaning_lit', None)
df.insert(12, 'sbs_notes', None)
df.insert(13, 'ru_notes', None)
df.insert(14, 'SBS Meaning', None)
df.insert(31, 'sbs_chant_Pāli1', None)
df.insert(32, 'sbs_chant_eng_1', None)
df.insert(33, 'sbs_chapter_1', None)
df.insert(35, 'sbs_chant_pali_2', None)
df.insert(36, 'sbs_chant_eng_2', None)
df.insert(37, 'sbs_chapter_2', None)
df.insert(38, 'Source 3', None)
df.insert(39, 'Sutta 3', None)
df.insert(40, 'Example 3', None)
df.insert(41, 'sbs_chant_pali_3', None)
df.insert(42, 'sbs_chant_eng_3', None)
df.insert(43, 'sbs_chapter_3', None)
df.insert(44, 'Source 4', None)
df.insert(45, 'Sutta 4', None)
df.insert(46, 'Example 4', None)
df.insert(47, 'sbs_chant_pali_4', None)
df.insert(48, 'sbs_chant_eng_4', None)
df.insert(49, 'sbs_chapter_4', None)
df.insert(50, 'Source 5', None)
df.insert(51, 'Sutta 5', None)
df.insert(52, 'Example 5', None)
df.insert(53, 'sbs_chant_pali_5', None)
df.insert(54, 'sbs_chant_eng_5', None)
df.insert(55, 'sbs_chapter_5', None)
df.insert(56, 'sbs_index', None)



df = df[['ID', 'Pāli1', 'Fin', 'sbs_class_anki', 'sbs_category', 'POS', 'Grammar', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Literal Meaning', 'ru_meaning', 'ru_meaning_lit', 'SBS Meaning', 'Pāli Root', 'Base', 'Construction', 'Phonetic Changes', 'Derivative', 'Suffix', 'Compound', 'Compound Construction', 'Sanskrit', 'Sk Root', 'variant', 'Commentary', 'Notes', 'sbs_notes', 'ru_notes', 'Source1', 'Sutta1', 'Example1', 'sbs_chant_Pāli1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'Source 2', 'Sutta2', 'Example 2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'Source 3', 'Sutta 3', 'Example 3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'Source 4', 'Sutta 4', 'Example 4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4', 'Source 5', 'Sutta 5', 'Example 5', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_index', 'Stem', 'Pattern']]

# saving csv and xlsx files
df.to_csv("/home/deva/Documents/dps/spreadsheets/nidh_bold.csv", sep="\t", index=None)
df.to_excel("/home/deva/Documents/dps/spreadsheets/nidh_bold.xlsx", index=None)


