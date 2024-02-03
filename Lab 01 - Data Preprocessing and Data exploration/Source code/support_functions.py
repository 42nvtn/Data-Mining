import csv

# Read a csv file to a list of dicts
def readFile(filename):
    data = []
    with open(filename, 'r') as file:
        my_reader = csv.DictReader(file, delimiter=',')
        for row in my_reader:
            data.append(dict(row))
    return data

# Write a list of dicts to a csv file
def writeFile(data, filename):
    with open(filename, 'w', newline='') as output_file:
        dict_writer  = csv.DictWriter(output_file, fieldnames=data[0].keys())
        dict_writer .writeheader()
        dict_writer .writerows(data)

# Check if a string can be converted to a number (float, int)
def is_float_int(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Change list of dicts (from readFile function, data types are all str) data types to str, int or float 
def change_dtypes(data):
    for row in data:
        for k, v in row.items():
            if is_float_int(v):
                row[k] = eval(v)
            else:
                row[k] = v
    return data

# Get data collumn
def collumn(data, name):
    return [row[name] for row in data]

# Remove '' items from a list
def remove_blank(ls):
    res = []
    for val in ls:
        if val != '':
            res.append(val)
    return res

# Calculate mean of a list
def mean(ls):
    ls = remove_blank(ls)
    if len(ls) == 0:
        return ''
    
    return sum(ls)/len(ls)    

# Calculate median of a list
def median(ls):
    ls = remove_blank(ls)
    if len(ls) == 0:
        return ''
    
    ls.sort()
    mid = len(ls) // 2
    res = (ls[mid] + ls[~mid]) / 2
    return res

# Calculate mode of a list
def mode(ls):
    ls = remove_blank(ls)
    if len(ls) == 0:
        return ''
    
    return (max(set(ls), key = ls.count))

# Calculate standard deviation of a list
def standard_deviation(ls):
    ls = remove_blank(ls)
    if len(ls) == 0:
        return None
    mean = sum(ls)/len(ls)
    deviations = [(x - mean) ** 2 for x in ls]
    variance = sum(deviations) / len(ls)
    sd = variance ** (1/2)
    return sd

# Return a string contains a's data type (int, float, str)
def is_str_int_float(a):
    if isinstance(a, int):
        return 'int'
    elif isinstance(a, float):
        return 'float'
    elif isinstance(a, str):
        return 'str'
    return 0

# Return a dictionary (key: collumn name, val: data type)
def get_dtypes(data):
    res = {}
    for k, v in data[0].items():
        for row in data:
            # If encounter a missing value, ignore it and cotinue
            if row[k] == '':
                continue
            # If encounter a value, check it's data type, break a for loop and write it's data type to data types dictionary
            else:
                dtype = is_str_int_float(row[k])
                break
        res[k] = dtype
    return res

# Delete a collumn from data
def del_col(data, col):
    for row in data:
        del row[col]
    return data