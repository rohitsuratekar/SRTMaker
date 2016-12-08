# SRTMaker
Small python script which makes .SRT files from Excel or csv files

Requirement : Python3 , Pandas Library

This script uses python3 to convert excel file into .srt file (used for subtitle in videos)

excel file should be in following format

Column 1: Text <br>
Column 2: start timing in (hh:mm:ss) format <br>
Column 3: milliseconds <br>
Column 4: end timing in (hh:mm:ss) format <br>
Column 5: milliseconds <br>

Start from first row - first column (A1) WITHOUT headers

Just change file name to "input.xlsx" or change inside code :)