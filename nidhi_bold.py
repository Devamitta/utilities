
import pandas as pd
from pandas_ods_reader import read_ods 
import re

df = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
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
test3 = df['Literal Meaning'] != ""
filter = test3 & test2
df.loc[filter, ['Meaning IN CONTEXT']] = df['Meaning IN CONTEXT'] + "; lit. " + df['Literal Meaning']

# concat Notes and Phonetic Changes
# test4 = df['Phonetic Changes'] != ""
# test5 = df['Notes'] != ""
# test6 = df['Notes'] == ""
# filter = test4 & test2 & test5
# df.loc[filter, ['Notes']] = df['Notes'] + "<br/>" + df['Phonetic Changes']
# filter = test4 & test2 & test6
# df.loc[filter, ['Notes']] = df['Notes'] + df['Phonetic Changes']

df['DPD'] = df['Fin']

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


# if pos in grammar then remove pos from nothing in grammar
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

df.insert(17, 'Variant', df['Variant – same constr or diff reading'])
df.insert(2, 'Ex', None)
df.insert(10, 'Meaning in native language', None)
df.insert(11, 'SBS Meaning', None)
df.insert(31, 'Pali chant 1', None)
df.insert(32, 'English chant 1', None)
df.insert(33, 'Chapter 1', None)
df.insert(35, 'Pali chant 2', None)
df.insert(36, 'English chant 2', None)
df.insert(37, 'Chapter 2', None)
df.insert(38, 'Source 3', None)
df.insert(39, 'Sutta 3', None)
df.insert(40, 'Example 3', None)
df.insert(41, 'Pali chant 3', None)
df.insert(42, 'English chant 3', None)
df.insert(43, 'Chapter 3', None)
df.insert(44, 'Source 4', None)
df.insert(45, 'Sutta 4', None)
df.insert(46, 'Example 4', None)
df.insert(47, 'Pali chant 4', None)
df.insert(48, 'English chant 4', None)
df.insert(49, 'Chapter 4', None)
df.insert(50, 'Index', None)
df.insert(51, 'Test', None)
df.insert(52, 'class', None)
df.insert(53, 'count', None)
df.insert(54, 'audio', None)


df = df[['ID', 'Pāli1', 'Fin', 'Ex', 'POS', 'Grammar', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'SBS Meaning', 'Pāli Root', 'Base', 'Construction', 'Phonetic Changes', 'Derivative', 'Suffix', 'Compound', 'Compound Construction', 'Sanskrit', 'Sk Root', 'Variant', 'Commentary', 'Notes', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source 2', 'Sutta2', 'Example 2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source 3', 'Sutta 3', 'Example 3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Source 4', 'Sutta 4', 'Example 4', 'Pali chant 4', 'English chant 4', 'Chapter 4', 'Index', 'Stem', 'Pattern', 'Test', 'class', 'count', 'audio', 'DPD', 'Category']]

# saving csv file
df.to_csv("../spreadsheets/nidh_bold.csv", sep="\t", index=None)

