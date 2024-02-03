import sys
from support_functions import*

def deleteCol_withMissingVals(data, percentage):
    col_names = data[0].keys()
    del_cols = []
    
    for name in col_names:
        count = 0
        # Find all missing values in collumn
        for row in data:
            if row[name] == '':
                count += 1
        # If missing percentage is higher than percentage, append it to del_cols
        if (count/len(data))*100 > percentage:
            del_cols.append(name)
    
    # Delete all collumns from del_rows
    for col in del_cols:
        del_col(data, col)
    return data

#python 5-deleteMissingValsCols.py house-prices.csv 50 5-deleteMissingValsCols.csv
data = readFile(sys.argv[1])
data = change_dtypes(data)

numOfColsBefore = len(data[0])
data = deleteCol_withMissingVals(data, float(sys.argv[2]))
numOfColsAfter = len(data[0])
writeFile(data, sys.argv[3])

print('Number of cols before: ', numOfColsBefore)
print('Number of cols after: ', numOfColsAfter)
print('Number of deleted cols: ', numOfColsBefore - numOfColsAfter)