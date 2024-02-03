import sys
from support_functions import*

def fill_missingVals(data, method, cols_ls):
    dtypes = get_dtypes(data)
    cols = dict((k, dtypes[k]) for k in cols_ls if k in dtypes)

    for name, dtype in cols.items():
        # If data type is str, use mode
        if dtype == 'str':
            col_mode = mode(collumn(data, name))
        # If data type is int or float, use mean or median based on method
        elif method == 'mean':
            col_mean = mean(collumn(data, name))
        elif method == 'median':
            col_median = median(collumn(data, name))

        for row in data:
            if row[name] == '':
                if dtype == 'str':
                    row[name] = col_mode
                elif dtype == 'int' or dtype == 'float':
                    if method == 'mean':
                        row[name] = col_mean
                    elif method == 'median':
                        row[name] = col_median

    return data

#python 3-Fill_missingVals.py house-prices.csv [LotFrontage,Alley] mean 3-Fill_missingVals.csv
data = readFile(sys.argv[1])
data = change_dtypes(data)
cols_ls = sys.argv[2].strip('][').split(',')
method = sys.argv[3]
data = fill_missingVals(data, method, cols_ls)
writeFile(data, sys.argv[4])