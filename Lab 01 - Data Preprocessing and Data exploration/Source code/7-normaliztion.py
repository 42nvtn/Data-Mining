import sys
from support_functions import*

#min-max
def minmax_normalization(data, attribute):
    col = collumn(data, attribute)
    col = remove_blank(col)
    # If attribute has no values (all missing), return
    if len(col) == 0:
        print("Attribute has no values")
        return data

    col_min = min(col)
    col_max = max(col)

    # Perform min-max normalization on all attribute items, except '' value items
    for row in data:
        if row[attribute] == '':
            continue
        else:
            row[attribute] = (row[attribute] - col_min)/(col_max - col_min)
    print('Successful normalization')
    return data

#z-score
def zscore_normalization(data, attribute):
    col = collumn(data, attribute)
    col = remove_blank(col)
    # If attribute has no values (all missing), return
    if len(col) == 0:
        print("Attribute has no values")
        return data

    col_mean = mean(col)
    col_sd = standard_deviation(col)

    # Perform z-score normalization on all attribute items, except '' value items
    for row in data:
        if row[attribute] == '':
            continue
        else:
            row[attribute] = (row[attribute] - col_mean)/col_sd
    print('Successful normalization')
    return data


def normalize(data, attribute, method):
    dtypes = get_dtypes(data)

    # Attribute not found
    if attribute not in dtypes.keys():
        print('Attribute does not exist')
        return data
    
    # If attribute data type is str, return
    elif dtypes[attribute] == 'str':
        print('Invalid data type, failed normaliztion')
        return data
    # Else, perform min-max or z-score based on method
    else:
        if method == 'minmax':
            return minmax_normalization(data, attribute)
        elif method == 'zscore':
            return zscore_normalization(data, attribute)
        # Method not found
        else:
            print('Invalid method')
            return data
        
#python 7-normaliztion.py house-prices.csv LotFrontage minmax 7-normaliztion.csv
#python 7-normaliztion.py house-prices.csv LotFrontage zscore 7-normaliztion.csv
data = readFile(sys.argv[1])
data = change_dtypes(data)

data = normalize(data, sys.argv[2], sys.argv[3])
writeFile(data, sys.argv[4])