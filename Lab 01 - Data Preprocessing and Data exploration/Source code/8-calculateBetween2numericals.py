import sys
from support_functions import*

def calc_2cols(data, attr1, attr2, method):
    dtypes = get_dtypes(data)

    # Check data type of attr1 and attr2. If str, return
    if dtypes[attr1] == 'str':
        print('Invalid data type, 2 collumns must be numeric')
        return data
    elif dtypes[attr2] == 'str':
        print('Invalid data type, 2 collumns must be numeric')
        return data
    # Addition
    if method == '+':
        for row in data:
            # If one of the attributes or both have '' value, output will be '' value too
            if (row[attr1] == '' and row[attr2] == '') or row[attr1] == '' or row[attr2] == '':
                row[attr1 + ' + ' + attr2] = ''
            else:
                row[attr1 + ' + ' + attr2] = float(row[attr1] + row[attr2])
        return data
    # Subtraction
    elif method == '-':
        for row in data:
            # If one of the attributes or both have '' value, output will be '' value too
            if (row[attr1] == '' and row[attr2] == '') or row[attr1] == '' or row[attr2] == '':
                row[attr1 + ' - ' + attr2] = ''
            else:
                row[attr1 + ' - ' + attr2] = float(row[attr1] - row[attr2])
        return data
    # Multiplication
    elif method == '*':
        for row in data:
            # If one of the attributes or both have '' value, output will be '' value too
            if (row[attr1] == '' and row[attr2] == '') or row[attr1] == '' or row[attr2] == '':
                row[attr1 + ' * ' + attr2] = ''
            else:
                row[attr1 + ' * ' + attr2] = float(row[attr1] * row[attr2])
        return data
    # Division
    elif method == '/':
        for row in data:
            # If one of the attributes or both have '' value, output will be '' value too
            if (row[attr1] == '' and row[attr2] == '') or row[attr1] == '' or row[attr2] == '':
                row[attr1 + ' / ' + attr2] = ''
            # If attr2 equals 0, output will be inf
            elif row[attr2] == 0:
                row[attr1 + ' / ' + attr2] = float('inf')
            else:
                row[attr1 + ' / ' + attr2] = float(row[attr1] / row[attr2])
        return data
    
#python 8-calculateBetween2numericals.py house-prices.csv MSSubClass LotFrontage + 8-calculateBetween2numericals.csv
data = readFile(sys.argv[1])
data = change_dtypes(data)
data = calc_2cols(data, sys.argv[2], sys.argv[3], sys.argv[4])

writeFile(data, sys.argv[5])