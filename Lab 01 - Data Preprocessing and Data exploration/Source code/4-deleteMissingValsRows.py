import sys
from support_functions import*

def deleteRow_withMissingVals(data, percentage):
    del_rows = []
    for row in data:
        count = 0
        # Find all missing values in row
        for k, v in row.items():
            if row[k] == '':
                count += 1
        # If missing percentage is higher than percentage, append it to del_rows
        if (count/len(row))*100 > percentage:
            del_rows.append(row)

    # Delete all data rows from del_rows
    for row in del_rows:
        while row in data:
            data.remove(row)

    return data

#python 4-deleteMissingValsRows.py house-prices.csv 10 4-deleteMissingValsRows.csv
data = readFile(sys.argv[1])
data = change_dtypes(data)

numOfRowsBefore = len(data)
data = deleteRow_withMissingVals(data, float(sys.argv[2]))
numOfRowsAfter = len(data)
writeFile(data, sys.argv[3])

print('Number of rows before: ', numOfRowsBefore)
print('Number of rows after: ', numOfRowsAfter)
print('Number of deleted rows: ', numOfRowsBefore - numOfRowsAfter)