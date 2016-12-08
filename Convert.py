"""
SRTMaker
Requirement : Python3 , Pandas Library

This script uses python3 to convert excel file into .srt file (used for subtitle in videos)
excel file should be in following format
Column 1: Text
Column 2: start timing in (hh:mm:ss) format
Column 3: milliseconds
Column 4: end timing in (hh:mm:ss) format
Column 5: milliseconds

Start from first row - first column (A1) WITHOUT headers
"""
import pandas as pd

column_names = ["text", "start", "start_milli", "end", "end_milli"]
input_file = pd.ExcelFile("input.xlsx", converters={'start_milli': str, 'end_milli': str})
sheet1 = input_file.parse(0, header=None, names=column_names)
counter = 1
with open("output.srt", 'w') as file:
    for index, row in sheet1.iterrows():
        milli1 = str(row["start_milli"]).split(".")[0].replace("nan", "000")
        milli2 = str(row["end_milli"]).split(".")[0].replace("nan", "000")
        print("%d\n%s,%s --> %s,%s\n%s\n" % (
            counter, row["start"], milli1, row["end"], milli2, row["text"]), file=file)
        counter += 1
