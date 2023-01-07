
import pandas as pd
from pandas_ods_reader import read_ods 
import re

df = pd.read_csv("/home/deva/Documents/dpd-br/csvs/dpd-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# concat Pali Root
test1 = df['Pāli Root'] != ""
test2 = df['Pāli1'] != ""
filter = test1 & test2
df.loc[filter, ['Pāli Root']] = df['Pāli Root'] + " " + df['Grp'] + " " + df['Sgn'] + " " + "(" + "to " + df['Root Meaning'] + ")"

# concat English Meaning
test3 = df['Literal Meaning'] != ""
filter = test3 & test2
df.loc[filter, ['Meaning IN CONTEXT']] = df['Meaning IN CONTEXT'] + "; lit. " + df['Literal Meaning']

# concat Notes and Phonetic Changes
test4 = df['Phonetic Changes'] != ""
test5 = df['Notes'] != ""
test6 = df['Notes'] == ""
filter = test4 & test2 & test5
df.loc[filter, ['Notes']] = df['Notes'] + "<br/>" + df['Phonetic Changes']
filter = test4 & test2 & test6
df.loc[filter, ['Notes']] = df['Notes'] + df['Phonetic Changes']

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
df.insert(25, 'Pali chant 1', None)
df.insert(26, 'English chant 1', None)
df.insert(27, 'Chapter 1', None)
df.insert(29, 'Pali chant 2', None)
df.insert(30, 'English chant 2', None)
df.insert(31, 'Chapter 2', None)
df.insert(32, 'Source 3', None)
df.insert(33, 'Sutta 3', None)
df.insert(34, 'Example 3', None)
df.insert(35, 'Pali chant 3', None)
df.insert(36, 'English chant 3', None)
df.insert(37, 'Chapter 3', None)
df.insert(38, 'Index', None)


df = df[['Pāli1', 'Fin', 'Ex', 'POS', 'Grammar', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'SBS Meaning', 'Pāli Root', 'Base', 'Construction', 'Sanskrit', 'Sk Root', 'Variant', 'Commentary', 'Notes', 'Source1', 'Sutta1', 'Example1', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Source 2', 'Sutta2', 'Example 2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source 3', 'Sutta 3', 'Example 3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Index', 'Stem', 'Pattern', 'Category']]

# saving csv file
df.to_csv("../spreadsheets/nidh_bold.csv", sep="\t", index=None)

