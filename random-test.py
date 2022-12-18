import pandas as pd
import random
import markdown

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

df_pat = pd.read_csv("../csv-for-anki/patimokkha-anki.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# df = df.drop(['class', 'count', 'ex'], axis=1)
# print("columns 'class', 'count', 'ex' has been dropped")

# generate random number 1-100
ran = random.sample(range(1, 100), 1)
ran = str(ran[0])

# change Test dps
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Test']] = ran

# change Test pat
test2 = df_pat['pali'] != ""
filter = test2
df_pat.loc[filter, ['test number']] = ran

# save csv dps
df.to_csv("../spreadsheets/dps-test.csv", sep="\t", index=None)

# save csv pat
df_pat.to_csv("../csv-for-anki/patimokkha-anki.csv", sep="\t", index=None)

print(f">>>>>>>>>>>>>>>>>>>>test number : {ran} <<<<<<<<<<<<<<<<<<<<<")

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

