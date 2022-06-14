def convert_dps_ods_to_csv():
    import pandas as pd
    from pandas_ods_reader import read_ods 
    import re

    df_convert_dps = read_ods("/home/deva/Documents/dps/spreadsheets/dps.ods")
    df_convert_dps.fillna("", inplace=True)
    df_convert_dps = df_convert_dps.astype(str)
    df_convert_dps.rename(columns=df_convert_dps.iloc[0], inplace = True)
    df_convert_dps.drop([0], inplace = True)

    df_convert_dps.to_csv("/home/deva/Documents/dps/spreadsheets/dps.csv", sep="\t", index=None)

convert_dps_ods_to_csv()