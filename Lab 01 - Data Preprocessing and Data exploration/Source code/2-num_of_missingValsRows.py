import sys
from support_functions import*

def num_of_missingValsRows(data):
    count = 0
    for row in data:
        for k, v in row.items():
            # If encounter a missing value in row, raise count by 1 and break a for loop (next row)
            if row[k] == '':
                count += 1
                break
    return count

#python 2-num_of_missingValsRows.py house-prices.csv
data = readFile(sys.argv[1])
data = change_dtypes(data)

num = num_of_missingValsRows(data)
print('Number of lines with missing data: ', num)