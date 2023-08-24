# Generate csvs for grammar anki deck for all classes from the database. 
# https://sasanarakkha.github.io/study-tools/pali-class/pali-class.html

import pandas as pd

# Load the Excel file into a pandas ExcelFile object
excel_file = pd.ExcelFile('../pali_resources/pāli-course/grammar.xlsx')

# Create a dictionary to store the DataFrames
dfs = {}

# Loop through each sheet in the Excel file
for sheet_name in excel_file.sheet_names:
    # Read the current sheet into a DataFrame
    df = excel_file.parse(sheet_name)

    # Check if df is a DataFrame
    if isinstance(df, pd.DataFrame):
        # Convert the values in the '2nd column' to strings
        df.iloc[:, 1] = df.iloc[:, 1].astype(str)

        second_column_name = df.columns[1]
        df['feedback'] = df.apply(lambda row: (
            f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/1Z8Jjt0-E0HNX7ygABIzAcrChG23M3IOyoZGQ-EDRzXY/viewform?usp=pp_url&entry.644913945"""
            f"""={row[second_column_name]}"""
            f"""&entry.957833742=Anki Deck Grammar">Fix it here</a>"""
        ), axis=1)

        # Reset the index and drop the old index
        df.reset_index(drop=True, inplace=True)

        # Store the DataFrame in the dictionary with the sheet name as the key
        dfs[sheet_name] = df
    else:
        print(f"Sheet {sheet_name} did not load as a DataFrame. It is a {type(df)}.")

# Now you can access each DataFrame using its sheet name as a key
# For example, dfs['Sheet1'] will give you the DataFrame for 'Sheet1', and so on.

# Save the DataFrame to a CSV file after dropping unnecessary columns
dfs['abbr'].drop(columns=['id', 'type', 'pattern', 'feedback']).to_csv(
    "../exporter/assets/abbreviations.csv",
    sep="\t",
    index=False,
    header=True
)

# Print completion message in green color
print("\033[32mExtraction abbreviations.csv for exporter complete.\033[0m")

# Filter the DataFrame to include only rows where 'type' column is not null
filtered_df = dfs['abbr'][dfs['abbr']['type'].notna()]

# Drop unnecessary columns from the filtered DataFrame
df_abbr_class = filtered_df.drop(columns=['ru-meaning', 'ru-abbrev', 'type'])

# Concatenate df_abbr_class, df_alph, df_samasa, df_upasagga into df_sum_abbr
df_sum_abbr = pd.concat([df_abbr_class, dfs['alph'], dfs['samasa'], dfs['upasagga']])

# Save df_sum_abbr to a CSV file
df_sum_abbr.to_csv("../csv-for-anki/grammar/cl_sum_abbr.csv", sep="\t", index=False)

# Print completion message in green color
print("\033[32mExtraction df_sum_abbr for class complete.\033[0m")

# Concatenate the DataFrames and store the result in df_sum_sandhi
df_sum_sandhi = pd.concat([
    dfs['v_sandhi'],
    dfs['c_sandhi'],
    dfs['m_sandhi'],
    dfs['assim'],
    dfs['mx_sandhi'],
    dfs['change_s'],
    dfs['irr_base'],
    dfs['taddhita'],
    dfs['kitaka']
])

# Save df_sum_sandhi to a CSV file
df_sum_sandhi.to_csv("../csv-for-anki/grammar/cl_sum_sandhi.csv", sep="\t", index=False)

# Print completion message in green color
print("\033[32mExtraction df_sum_sandhi for class complete.\033[0m")

# Concatenate all DataFrames except those in df_sum_abbr and df_sum_sandhi
dfs_to_concat = [
    dfs[sheet_name] for sheet_name in excel_file.sheet_names 
    if sheet_name not in ['abbr', 'alph', 'samasa', 'upasagga', 'v_sandhi', 'c_sandhi', 
        'm_sandhi', 'assim', 'mx_sandhi', 'change_s', 'irr_base', 'taddhita', 'kitaka']
]
df_sum_gramm = pd.concat(dfs_to_concat)

# Save df_sum_gramm to a CSV file
df_sum_gramm.to_csv("../csv-for-anki/grammar/cl_sum_gramm.csv", sep="\t", index=False)

# Save the column list of df_sum_abbr to a text file
file_path = "../../sasanarakkha/study-tools/anki-style/field-list-grammar-abbr.txt"
with open(file_path, "w") as file:
    file.write('\n'.join(df_sum_abbr.columns))

# Save the column list of df_sum_sandhi to a text file
file_path = "../../sasanarakkha/study-tools/anki-style/field-list-grammar-sandhi.txt"
with open(file_path, "w") as file:
    file.write('\n'.join(df_sum_sandhi.columns))

# Save the column list of df_sum_gramm to a text file
file_path = "../../sasanarakkha/study-tools/anki-style/field-list-grammar-gramm.txt"
with open(file_path, "w") as file:
    file.write('\n'.join(df_sum_gramm.columns))

# Print completion message in green color
print("\033[32mExtraction df_sum_gramm for class complete.\033[0m")