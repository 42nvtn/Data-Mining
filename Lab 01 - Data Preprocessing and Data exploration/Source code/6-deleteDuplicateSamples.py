import sys
from support_functions import*

def del_duplicate(data):
    seen = set()
    new_data = []
    for row in data:
        # Convert dictionary to tuple. Since tuple can be hashed, we can use set
        t = tuple(row.items())
        if t not in seen:
            seen.add(t)
            new_data.append(row)
    return new_data

#python 6-deleteDuplicateSamples.py house-prices.csv 6-deleteDuplicateSamples.csv
data = readFile(sys.argv[1])
data = change_dtypes(data)

numOfRowsBefore = len(data)
data = del_duplicate(data)
numOfRowsAfter = len(data)

writeFile(data, sys.argv[2])

print('Number of rows before: ', numOfRowsBefore)
print('Number of rows after: ', numOfRowsAfter)
print('Number of deleted rows: ', numOfRowsBefore - numOfRowsAfter)