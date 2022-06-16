import pandas as pd

df = pd.read_csv("/home/deva/Documents/dps/spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# make Feedback
df.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/1iMD9sCSWFfJAFCFYuG9HRIyrr9KFRy0nAOVApM998wM/viewform?usp=pp_url&entry.438735500="+df['Pāli1']+"\">feedback</a>")

# save csv
df.to_csv("/home/deva/Documents/dps/spreadsheets/dps-feedback.csv", sep="\t", index=None)
