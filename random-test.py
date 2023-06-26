import pandas as pd
import random
import markdown

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

df_pat = pd.read_csv("../csv-for-anki/patimokkha-anki.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

df.insert(65, 'test', None)


# concat English Meaning
test1 = df['pali_1'] != ""
test2 = df['meaning_lit'] != ""
filter = test1 & test2
df.loc[filter, ['meaning_1']] = df['meaning_1'] + "; lit. " + df['meaning_lit']

df = df.drop(['meaning_lit'], axis=1)

# print("column 'meaning_lit' has been dropped")

# concat Ru Meaning
test1 = df['pali_1'] != ""
test2 = df['ru_meaning_lit'] != ""
filter = test1 & test2
df.loc[filter, ['ru_meaning']] = df['ru_meaning'] + "; досл. " + df['ru_meaning_lit']

df = df.drop(['ru_meaning_lit'], axis=1)

# print("column 'ru_meaning_lit' has been dropped")

# make original dps for anki

df_anki = df.drop(['sbs_class', 'count', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes'], axis=1)
# print("columns 'sbs_class', 'count', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes' has been dropped for anki")

df_anki.to_csv("../csv-for-anki//dps-orig.csv", sep="\t", index=None)

# make sutta deck
test2 = df['sbs_category'] != ""
filter = test2
df_sutta = df.loc[filter]

df_sutta = df_sutta.drop(['sbs_class', 'count', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes'], axis=1)
# print("columns 'sbs_class', 'count', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes' has been dropped for anki")

# change ru_meaning
test2 = df_sutta['pali_1'] != ""
filter = test2
df_sutta.loc[filter, ['ru_meaning']] = ""

# generate random number 1-100
ran = random.sample(range(1, 100), 1)
ran = str(ran[0])

# change Test dps
test1 = df['pali_1'] != ""
filter = test1
df.loc[filter, ['test']] = ran

# change Test pat
test2 = df_pat['pali'] != ""
filter = test2
df_pat.loc[filter, ['test number']] = ran

# change Test sutta
test1 = df_sutta['pali_1'] != ""
filter = test1
df_sutta.loc[filter, ['test']] = ran

# save csv dps
df.to_csv("../spreadsheets/dps-test.csv", sep="\t", index=None)

# save csv pat
df_pat.to_csv("../csv-for-anki/patimokkha-anki.csv", sep="\t", index=None)

# adding feedback
df_sutta['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_sutta['pali_1'] + """&entry.644913945=Anki Deck Suttas">Fix it here</a>."""


# save csv sutta
df_sutta.to_csv("../csv-for-anki/suttas-feedback.csv", sep="\t", index=None)

print("\033[32m" + f">>>>>>>>>>>>>>>>>>>>test number : {ran} <<<<<<<<<<<<<<<<<<<<<" + "\033[0m")


# make test.md
result_markdown_1 = markdown.markdown(f"""

# Removing duplicated words

Please see small [video](https://user-images.githubusercontent.com/39419221/187020101-701ee57e-b708-4be1-91d7-0c9b411a11cd.mp4) how to do it.

This work is based on the [DPD](https://digitalpalidictionary.github.io/) dictionary which is a work in progress and being updated regularly. Because of this, from time to time may an updated may be done of selected words (this will show itself like this; for example: the word 'pada' will become 'pada 1', and variations of meanings of 'pada' will be added as 'pada 2', 'pada 3' etc.). 

From this follows that from time to time duplicated words (the original 'pada' is now duplicated as 'pada 1', need to be removed. For this, the field called **"Test"** is used.

After you updated the downloaded Anki Deck (same way, just by double-clicking on the latest downloaded file). Choose your Deck and in the **Browse** add:

`-test:`{ran}

It will show all cards which do not have a number in field "Test". And you can easily delate all of this old words, by selecting all (**Ctrl + A**) and deleting (**Ctrl + Delete**). 

Now you are up-to-date.

With every update, this number will be different.


""")

with open('/home/deva/Documents/dps/test.md', 'w') as f:
    f.write(result_markdown_1)
f.close()

# with open('/home/deva/Documents/sasanarakkha/study-tools/temp-push/test.md', 'w') as f:
#     f.write(result_markdown_1)
# f.close()

# make ru-test.md
result_markdown_2 = markdown.markdown(f"""

# Удаление повторяющихся слов

Описание на английском на [видео](https://user-images.githubusercontent.com/39419221/187020101-701ee57e-b708-4be1-91d7-0c9b411a11cd.mp4).

Эта работа основана на [DPD](https://digitalpalidictionary.github.io/) который находится в стадии разработки и регулярно обновляется. Из-за этого раз за разом могут быть добавлены или отредактированы некоторые слова (например: слово 'pada' стало 'pada 1', т.к. было найдено другое значение этого слова в другом контексте). Нужно раз за разом удалять повторяющиеся слова, которые больше не существуют. Для этого существует поле **"Test"**.

После того, как вы обновили свою колоду Anki (дважды щелкнув по загруженной свежей версии колоды Pāli.apkg). Во вкладке **Browse** введите:

`-test:`{ran}

Будут показаны все слова, у которых нет {ran} в поле «Test». И вы можете легко удалить их, выбрав все (**Ctrl + A**) и удалив (**Ctrl + Delete**). 

С каждым следующим обновлением это число в поле «Test» будет разным.


""")

with open('/home/deva/Documents/dps/ru-test.md', 'w') as f:
    f.write(result_markdown_2)
f.close()

# with open('/home/deva/Documents/sasanarakkha/study-tools/temp-push/ru-test.md', 'w') as f:
#     f.write(result_markdown_2)
# f.close()

