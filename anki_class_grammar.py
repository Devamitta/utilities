# Generate csvs for grammar anki deck for all classes from the database. 
# https://sasanarakkha.github.io/study-tools/pali-class/pali-class.html

import pandas as pd
import sys
import os
import shutil

from rich.console import Console

sys.path.append("/home/deva/Documents/dpd-db") # https://github.com/digitalpalidictionary/dpd-db

from tools.tic_toc import tic, toc


console = Console()

def main():
    tic()
    moving_grammar()
    make_grammar_csvs()
    toc()


def moving_grammar():
    # Print completion message in green color
    print("\033[1;33m moving grammar.xlsx from Downloads/ \033[0m")

    # Assuming the script is in the 'Documents//dps/utilites' directory
    script_dir = os.path.dirname(os.path.realpath(__file__))
    deva_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..'))

    downloads_dir = os.path.join(deva_dir, 'Downloads')

    pali_course_dir = os.path.join(
    deva_dir,
    'Documents', 
    'pali_resources', 
    'pāli-course', 
    )

    grammar_src = os.path.join(downloads_dir, 'grammar.xlsx')
    grammar_dest = os.path.join(pali_course_dir, 'grammar.xlsx')

    # Move dpd-kindle.mobi to the specified directory
    if os.path.exists(grammar_src):
        shutil.move(grammar_src, grammar_dest)
        print("\033[1;32m grammar.xlsx moved to pāli-course folder \033[0m")
    else:
        print("\033[1;31m grammar.xlsx is missing.\033[0m")


def make_grammar_csvs():
    # Load the Excel file into a pandas ExcelFile object
    excel_file = pd.ExcelFile('../../pali_resources/pāli-course/grammar.xlsx')

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

    console.print("[bold green]extracting abbreviations.csv for exporter.")

    # Save the DataFrame to a CSV file after dropping unnecessary columns
    trimmed_df = dfs['abbr'].drop(columns=['id', 'type', 'pattern', 'feedback'])
    trimmed_df.to_csv("../exporter/assets/abbreviations.csv", sep="\t", index=False, header=True)

    # Printing the number of rows in the trimmed DataFrame
    row_count = len(trimmed_df)
    print("Number of rows:", row_count)

    console.print("[bold green]extracting df_sum_abbr for class.")

    # Filter the DataFrame to include only rows where 'type' column is not null
    filtered_df = dfs['abbr'][dfs['abbr']['type'].notna()]

    # Drop unnecessary columns from the filtered DataFrame
    df_abbr_class = filtered_df.drop(columns=['ru-meaning', 'ru-abbrev', 'type'])

    # Concatenate df_abbr_class, df_alph, df_samasa, df_upasagga into df_sum_abbr
    df_sum_abbr = pd.concat([df_abbr_class, dfs['alph'], dfs['samasa'], dfs['upasagga'], dfs['roots']])

    # Save df_sum_abbr to a CSV file
    df_sum_abbr.to_csv("../../dpd-db/dps/csvs/anki_csvs/pali_class/grammar/cl_sum_abbr.csv", sep="\t", index=False)

    row_count = len(df_sum_abbr)
    print("Number of rows:", row_count)

    console.print("[bold green]extracting df_sum_sandhi for class.")

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
        dfs['kitaka'],
        dfs['vuddhi']
    ])

    # Save df_sum_sandhi to a CSV file
    df_sum_sandhi.to_csv("../../dpd-db/dps/csvs/anki_csvs/pali_class/grammar/cl_sum_sandhi.csv", sep="\t", index=False)

    row_count = len(df_sum_sandhi)
    print("Number of rows:", row_count)

    console.print("[bold green]extracting cl_sum_gramm for class.")

    # Concatenate all DataFrames except those in df_sum_abbr and df_sum_sandhi
    dfs_to_concat = [
        dfs[sheet_name] for sheet_name in excel_file.sheet_names 
        if sheet_name not in ['abbr', 'alph', 'samasa', 'upasagga', 'roots', 'v_sandhi', 'c_sandhi', 
            'm_sandhi', 'assim', 'mx_sandhi', 'change_s', 'irr_base', 'taddhita', 'kitaka', 'vuddhi']
    ]
    df_sum_gramm = pd.concat(dfs_to_concat)

    # Save df_sum_gramm to a CSV file
    df_sum_gramm.to_csv("../../dpd-db/dps/csvs/anki_csvs/pali_class/grammar/cl_sum_gramm.csv", sep="\t", index=False)

    row_count = len(df_sum_gramm)
    print("Number of rows:", row_count)

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


if __name__ == "__main__":
    main()