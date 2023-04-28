
import pandas as pd
from pandas_ods_reader import read_ods 
import re

df = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# print(df['root_pali'].dtype)

# concat Pali Root
# root_clean = re.sub(" //d*$", "", root)
df['Root Clean'] = df['root_pali'].str.replace(" \d.*$", "", regex=True)
# df['Root Clean'] = df['root_pali'].str.replace('[^\w\s]','', regex=True)
# df['Root Clean'] = df['root_pali'].str.replace('[^\w\s]','')
test1 = df['root_pali'] != ""
test2 = df['pali_1'] != ""
filter = test1 & test2
df.loc[filter, ['root_pali']] = df['Root Clean'] + " " + df['Grp'] + " " + df['Sgn'] + " " + "(" + "to " + df['Root Meaning'] + ")"

# concat English Meaning
test3 = df['meaning_lit'] != ""
filter = test3 & test2
df.loc[filter, ['meaning_1']] = df['meaning_1'] + "; lit. " + df['meaning_lit']

# concat Notes and phonetic
# test4 = df['phonetic'] != ""
# test5 = df['notes'] != ""
# test6 = df['notes'] == ""
# filter = test4 & test2 & test5
# df.loc[filter, ['notes']] = df['notes'] + "<br/>" + df['phonetic']
# filter = test4 & test2 & test6
# df.loc[filter, ['notes']] = df['notes'] + df['phonetic']

df['DPD'] = df['Fin']

# change FIN
test3 = df['example_2'] != ""
test4 = df['example_1'] != ""
filter = test2 & test3 & test4
df.loc[filter, ['Fin']] = "nn"

test3 = df['example_2'] == ""
test4 = df['example_1'] != ""
filter = test2 & test3 & test4
df.loc[filter, ['Fin']] = "n"

test3 = df['example_2'] == ""
test4 = df['example_1'] == ""
filter = test2 & test3 & test4
df.loc[filter, ['Fin']] = ""


# managing grammar
test4 = df['pos'] == df['grammar']
# test4 = df['pos'].str.contains(fr"{df['grammar']}")
filter = test4
df.loc[filter, ['grammar']] = ""


# if pos in grammar then remove pos from nothing in grammar
df['grammar']=df.apply(lambda x: x['grammar'].replace(x['derived_from'], ""), axis=1)

df['grammar']=df.apply(lambda x: x['grammar'].replace(x['pos'], ""), axis=1)

df['grammar']=df.apply(lambda x: x['grammar'].replace("na", ""), axis=1)

# cleaning grammar
df['grammar'] = df['grammar'].replace(' of ', '', regex=True)

df['grammar'] = df['grammar'].replace('of', '', regex=True)

df['grammar'] = df['grammar'].replace(' from ', '', regex=True)

df['grammar'] = df['grammar'].replace({r'^(,)'}, '',  regex=True)

df['grammar'] = df['grammar'].replace({r'^( )'}, '',  regex=True)

df['grammar'] = df['grammar'].replace({r'( )$'}, '',  regex=True)

df['grammar'] = df['grammar'].replace({r'(,)$'}, '',  regex=True)

df['grammar'] = df['grammar'].replace({r'^(, )'}, '',  regex=True)

# choosing order of columns

df.insert(17, 'variant', df['variant – same constr or diff reading'])
df.insert(2, 'sbs_class_anki', None)
df.insert(10, 'ru_meaning', None)
df.insert(11, 'SBS Meaning', None)
df.insert(31, 'sbs_chant_pali_1', None)
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
df.insert(50, 'sbs_index', None)
df.insert(51, 'Test', None)
df.insert(52, 'sbs_class', None)
df.insert(53, 'count', None)
df.insert(54, 'sbs_audio', None)


df = df[['id', 'pali_1', 'Fin', 'sbs_class_anki', 'pos', 'grammar', 'derived_from', 'neg', 'verb', 'trans', 'plus_case', 'meaning_1', 'ru_meaning', 'SBS Meaning', 'root_pali', 'root_base', 'construction', 'phonetic', 'derivative', 'suffix', 'compound_type', 'compound_construction', 'sanskrit', 'root_sk', 'variant', 'commentary', 'notes', 'source_1', 'sutta_1', 'example_1', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'Source 3', 'Sutta 3', 'Example 3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'Source 4', 'Sutta 4', 'Example 4', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4', 'sbs_index', 'stem', 'pattern', 'Test', 'sbs_class', 'count', 'sbs_audio', 'DPD', 'Category']]

# saving csv file
df.to_csv("../spreadsheets/nidh_bold.csv", sep="\t", index=None)

