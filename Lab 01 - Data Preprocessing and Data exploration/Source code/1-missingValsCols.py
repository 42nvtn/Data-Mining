import sys
from support_functions import*

def extract_Col_of_MissingVals(data):
    MissingValCols_ls = []
    for row in data:
        for k, v in row.items():
            # If collumn name already exists in MissingValCols_ls, continue
            if k in MissingValCols_ls:
                continue
            # If encounter a missing value, append that missing value's collumn name to MissingValCols_ls
            elif row[k] == '':
                MissingValCols_ls.append(k)
    return MissingValCols_ls

#python 1-missingValsCols.py house-prices.csv
data = readFile(sys.argv[1])
data = change_dtypes(data)

missingVals_cols = extract_Col_of_MissingVals(data)
print('Number of missing values collumns: ', len(missingVals_cols))
print('Columns with missing values: ', missingVals_cols)