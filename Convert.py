import pandas as pd 

xl = pd.ExcelFile("input.xlsx")
print(xl.sheet_names)