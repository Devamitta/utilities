import pandas as pd
import random
import markdown

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

df = df.drop(['class', 'count'], axis=1)
print("columns 'class', 'count' has been dropped")

# generate random number 1-100
ran = random.sample(range(1, 100), 1)
ran = str(ran[0])

# change Test
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Test']] = ran

# save csv
df.to_csv("../spreadsheets/dps-test.csv", sep="\t", index=None)

# make test.md
result_markdown_1 = markdown.markdown(f"""

<h1>Tools for study Pāli</h1>


Dictionaries:

- [SBS Pāli-English Dictionary](https://sasanarakkha.github.io/study-tools/sbs-pali-dictionary.html)
- [Pāli-Russian Dictionary](https://sasanarakkha.github.io/study-tools/ru-pali-dictionary.html)
- [Digital Pāḷi Dictionary](https://digitalpalidictionary.github.io/)

PDF:

- [SBS Pāli-English Recitations](https://github.com/sasanarakkha/pali-english-recitations/releases/latest/)
- [Analysis of SBS Pāli-English Recitations](https://github.com/sasanarakkha/study-tools/releases/latest/download/analysis-of-sbs-pali-english-recitations.pdf)

Anki decks:

- [SBS Pāli-English Vocab](https://sasanarakkha.github.io/study-tools/sbs-pali-english-vocab.html)
- [DHP Vocab](https://sasanarakkha.github.io/study-tools/dhp-vocab.html)
- [DHP Learning](https://sasanarakkha.github.io/study-tools/dhp-learning.html)
- [Pātimokkha Word by Word](https://sasanarakkha.github.io/study-tools/patimokkha-word-by-word.html)
- [Pātimokkha Learning](https://sasanarakkha.github.io/study-tools/patimokkha-learning.html)
- [SBS Anumodāna](https://sasanarakkha.github.io/study-tools/sbs-anumodana.html)
- [Sutta Q&A](https://sasanarakkha.github.io/study-tools/sutta-q-a.html)
- [Russian Anki Deck](https://sasanarakkha.github.io/study-tools/ru-pali-vocab.html)
- [Ñāṇatiloka Buddhist Dictionary](https://sasanarakkha.github.io/study-tools/nanatiloka.html)

Made available for public testing and [feedback](https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.1433863141=SBS-study-tools).

If you have any questions related to Pāli-study, please [ask](mailto:devamitta@sasanarakkha.org) freely.

-----------------

<h1>Random number for Test in Anki</h1>

<p><strong>The test number for this update is '{ran}'</strong>

Choose your Deck and in the **Browse** add:

`-test:`{ran}


""")

with open('/home/deva/Documents/sasanarakkha/study-tools/temp-push/test.md', 'w') as f:
    f.write(result_markdown_1)
f.close()

