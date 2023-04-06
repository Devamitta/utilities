
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dpd+sbs.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# remove all SBS words
test2 = df['Test-s'].str.contains('e')
filter = test2
df = df.loc[filter]

# save csv
df.to_csv("../spreadsheets/df_e.csv", sep="\t", index=None)


# replace all sutta numbers with '_'
# df['Source1'] = df['Source1'].str.replace(' ', '_')
# df['Source2'] = df['Source2'].str.replace(' ', '_')
# df['Source3'] = df['Source3'].str.replace(' ', '_')

# filter all from sutta1
test1 = df["Fin"] != ""
test2 = df['Sutta1'].str.contains('nīvaraṇappahāna|pabbajitābhiṇhasuttaṃ|sacittasuttaṃ|girimānandasuttaṃ|mettāsuttaṃ|loṇakapallasuttaṃ|devadūtasuttaṃ|kesamuttisuttaṃ|abhayasuttaṃ|rohitassasuttaṃ|vipallāsasuttaṃ|sappurisasuttaṃ|abhiṇhapaccavekkhitabbaṭhānasuttaṃ|soṇasuttaṃ|majjhesuttaṃ|nibbedhikasuttaṃ|pacalāyamānasuttaṃ|mettāsuttaṃ|paññāsuttaṃ|sīhanādasuttaṃ|mahāsatipaṭṭhānasuttaṃ|gaṇakamoggallānasuttaṃ|ānāpānassatisuttaṃ|saḷāyatanavibhaṅgasuttaṃ|araṇavibhaṅgasuttaṃ|indriyabhāvanāsuttaṃ|madhupiṇḍikasuttaṃ|dvedhāvitakkasuttaṃ|sabbāsavasuttaṃ|vitakkasaṇṭhānasuttaṃ|mahāassapurasuttaṃ|mahārāhulovādasuttaṃ|sallekhasuttaṃ|puttamaṃsūpamasuttaṃ|nakulapitusuttaṃ|dutiyagaddulabaddhasuttaṃ|vāsijaṭasuttaṃ|soṇasuttaṃ|khajjanīyasuttaṃ|yamakasuttaṃ|pheṇapiṇḍūpamasuttaṃ|udāyīsuttaṃ|ādittapariyāyasuttaṃ|āsīvisopamasuttaṃ|kummopamasuttaṃ|paṭhamadārukkhandhopamasuttaṃ|vīṇopamasuttaṃ|chappāṇakopamasuttaṃ|yavakalāpisuttaṃ|channasuttaṃ|mālukyaputtasuttaṃ|bhadrakasuttaṃ|saṅgāravasuttaṃ|bhikkhunupassayasuttaṃ|janapadakalyāṇīsuttaṃ|bāhiyasuttaṃ')
# test3 = df['Sutta1'].str.contains('sutta')
filter = test1 & test2
df_sutta1 = df.loc[filter]

# save csv
df_sutta1.to_csv("../spreadsheets/df_sutta1.csv", sep="\t", index=None)



# filter all from sutta1
test1 = df["Fin"] != ""
test3 = df['Sutta2'].str.contains('nīvaraṇappahāna|pabbajitābhiṇhasuttaṃ|sacittasuttaṃ|girimānandasuttaṃ|mettāsuttaṃ|loṇakapallasuttaṃ|devadūtasuttaṃ|kesamuttisuttaṃ|abhayasuttaṃ|rohitassasuttaṃ|vipallāsasuttaṃ|sappurisasuttaṃ|abhiṇhapaccavekkhitabbaṭhānasuttaṃ|soṇasuttaṃ|majjhesuttaṃ|nibbedhikasuttaṃ|pacalāyamānasuttaṃ|mettāsuttaṃ|paññāsuttaṃ|sīhanādasuttaṃ|mahāsatipaṭṭhānasuttaṃ|gaṇakamoggallānasuttaṃ|ānāpānassatisuttaṃ|saḷāyatanavibhaṅgasuttaṃ|araṇavibhaṅgasuttaṃ|indriyabhāvanāsuttaṃ|madhupiṇḍikasuttaṃ|dvedhāvitakkasuttaṃ|sabbāsavasuttaṃ|vitakkasaṇṭhānasuttaṃ|mahāassapurasuttaṃ|mahārāhulovādasuttaṃ|sallekhasuttaṃ|puttamaṃsūpamasuttaṃ|nakulapitusuttaṃ|dutiyagaddulabaddhasuttaṃ|vāsijaṭasuttaṃ|soṇasuttaṃ|khajjanīyasuttaṃ|yamakasuttaṃ|pheṇapiṇḍūpamasuttaṃ|udāyīsuttaṃ|ādittapariyāyasuttaṃ|āsīvisopamasuttaṃ|kummopamasuttaṃ|paṭhamadārukkhandhopamasuttaṃ|vīṇopamasuttaṃ|chappāṇakopamasuttaṃ|yavakalāpisuttaṃ|channasuttaṃ|mālukyaputtasuttaṃ|bhadrakasuttaṃ|saṅgāravasuttaṃ|bhikkhunupassayasuttaṃ|janapadakalyāṇīsuttaṃ|bāhiyasuttaṃ')
# test3 = df['Sutta1'].str.contains('sutta')
filter = test1 & test3
df_sutta2 = df.loc[filter]

# save csv
df_sutta2.to_csv("../spreadsheets/df_sutta2.csv", sep="\t", index=None)



# # move examples from 2 to 1
# df_sutta2["Source1"] = df_sutta2["Source2"]
# df_sutta2["Sutta1"] = df_sutta2["Sutta2"]
# df_sutta2["Example1"] = df_sutta2["Example2"]

# df_sutta2["Source2"] = ""
# df_sutta2["Sutta2"] = ""
# df_sutta2["Example2"] = ""


# # move examples from 3 to 1
# df_sutta3["Source1"] = df_sutta3["Source3"]
# df_sutta3["Sutta1"] = df_sutta3["Sutta3"]
# df_sutta3["Example1"] = df_sutta3["Example3"]

# df_sutta2["Source3"] = ""
# df_sutta2["Sutta3"] = ""
# df_sutta2["Example3"] = ""



# if headword from df_sutta2 is in df_sutta1, then delete whole row from df_sutta2

# logix = df_sutta2['Pāli1'].isin(df_sutta1['Pāli1'])

# df_sutta4 = df_sutta2.drop(df_sutta2[logix].index)

# if headword from df is in df_sutta1, then delete whole row from df

logix = df['Pāli1'].isin(df_sutta1['Pāli1'])

df = df.drop(df[logix].index)

# save csv
df.to_csv("../spreadsheets/df_without_1.csv", sep="\t", index=None)

# if headword from df is in df_sutta2, then delete whole row from df

logix = df['Pāli1'].isin(df_sutta2['Pāli1'])

df = df.drop(df[logix].index)

# save csv
df.to_csv("../spreadsheets/df_without_2.csv", sep="\t", index=None)


# df_combined = pd.concat([df_sutta1, df_sutta2])

# df_combined = df_sutta1.append(df_sutta4)

# df_combined.sort_values(["Source1"], ascending=True, inplace=True)

# choosing order of columns

# df_combined = df_combined[['Pāli1', 'POS', 'Grammar', 'Derived from', 'Neg', 
#        'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'Pāli Root', 'Base',  
#        'Construction', 'Sanskrit', 'Sk Root', 
#        'Variant', 'Commentary', 'Notes', 
#        'Source1', 'Sutta1', 'Example1', 'Source2', 'Sutta2', 'Example2', 'Test']]

# make Feedback
# df_combined.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500="+df['Pāli1']+"\">feedback</a>")

# adding feedback
# df_combined.reset_index(drop=True, inplace=True)
# df_combined['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_combined.Pāli1 + """&entry.1433863141=SuttaPitaka">Fix it here</a>."""

# df_combined = df_combined.drop(['Fin', 'Stem', 'Pattern', 'Meaning in SBS-PER', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Index', 'ex', 'count', 'class'], axis = 1)
# print("columns 'Fin', 'Stem', 'Pattern', 'Meaning in SBS-PER', 'Pali chant 1', 'English chant 1', 'Chapter 1', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Index', 'ex', 'count', 'class' has been dropped")


# save csv
# df_combined.to_csv("../spreadsheets/sutta-from-dpd.csv", sep="\t", index=None)

