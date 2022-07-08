import pandas as pd
import random
import markdown

df = pd.read_csv("/home/deva/Documents/dps/spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# generate random number 1-100
ran = random.sample(range(1, 100), 1)
ran = str(ran[0])

# change Test
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Test']] = ran

# save csv
df.to_csv("/home/deva/Documents/dps/spreadsheets/dps-test.csv", sep="\t", index=None)

# make test.md
result_markdown_1 = markdown.markdown(f"""

# Removing duplicated words

This work is based on the [DPD](https://digitalpalidictionary.github.io/) which is the work in progress and updating regularly. Because of this, time after time may be added or edited some words (for example: the word 'pada' become 'pada 1', because has been found another meaning of this word in another context). We need time after time to remove those duplicated words, which are not existing any more. For this reason, we have a field **"Test"**
After you updated your Anki Deck (same way, just by double-clicking on the latest downloaded file). Choose your Deck and in the **Browse** add:

`-test:`{ran}

It will show all cards which do not have number '{ran}' in field "Test". And you can easily delate all of this old words, by selecting all (**Ctrl + A**) and deleting (**Ctrl + Delete**). 

Now you are up-to-date.

With every next update, this 'test number' will be different.

""")

with open('/home/deva/Documents/sasanarakkha/study-tools/Anki_Decks/SBS_Pāli-English_Vocab/test.md', 'w') as f:
    f.write(result_markdown_1)
f.close()

# make тест.md
result_markdown_2 = markdown.markdown(f"""

# Удаление повторяющихся слов

Эта работа основана на [DPD](https://digitalpalidictionary.github.io/), который находится в стадии разработки и регулярно обновляется. Из-за этого раз за разом могут быть добавлены или отредактированы некоторые слова (например: слово 'pada' стало 'pada 1', т.к. было найдено другое значение этого слова в другом контексте). Нужно раз за разом удалять повторяющиеся слова, которые больше не существуют. Для этого существует поле **"Test"**.
После того, как вы обновили свою колоду Anki (дважды щелкнув по загруженной свежей версии колоды Pāli.apkg). Во вкладке **Обзор** введите:

`"deck:.Pāli" -test:`{ran}

Будут показаны все слова, у которых нет цифры '{ran}' в поле «Test». И вы можете легко удалить их, выбрав все (**Ctrl + A**) и удалив (**Ctrl + Delete**).

С каждым следующим обновлением этот номер в поле «Test» будет разным.

""")

with open('/home/deva/Documents/sasanarakkha/study-tools/Anki_Decks/Пали_Словарь_Анки/тест.md', 'w') as f:
    f.write(result_markdown_2)
f.close()