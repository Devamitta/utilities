import pandas as pd

df = pd.read_csv("../spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# make Feedback
# df.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/1iMD9sCSWFfJAFCFYuG9HRIyrr9KFRy0nAOVApM998wM/viewform?usp=pp_url&entry.438735500="+df['pali_1']+"\">feedback</a>")

# adding feedback
df.reset_index(drop=True, inplace=True)
df['Feedback'] = f"""Нашли ошибку? <a class="link" href="https://docs.google.com/forms/d/1iMD9sCSWFfJAFCFYuG9HRIyrr9KFRy0nAOVApM998wM/viewform?usp=pp_url&entry.438735500=""" + df.pali_1 + """&entry.1433863141=Anki">Пожалуйста сообщите</a>."""

df = df.drop(['sbs_category', 'Fin', 'stem', 'pattern', 'sbs_meaning', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4', 'sbs_index', 'sbs_class_anki', 'count', 'sbs_class', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes'], axis = 1)
# print("columns 'sbs_category', 'Fin', 'stem', 'pattern', 'sbs_meaning', 'sbs_chant_pali_1', 'sbs_chant_eng_1', 'sbs_chapter_1', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'sbs_chant_pali_4', 'sbs_chant_eng_4', 'sbs_chapter_4', 'sbs_index', 'sbs_class_anki', 'count', 'sbs_class', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes' has been dropped")

# save csv
df.to_csv("../csv-for-anki/dps-feedback.csv", sep="\t", index=None)
