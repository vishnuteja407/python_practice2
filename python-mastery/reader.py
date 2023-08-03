import csv

data = []
def read_csv_as_dicts(filename, coltypes):
    with open(filename, 'r') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)   #headers
        for row in f_csv:
            result = { name:func(val) for name, func, val in zip(headers, coltypes, row) }
            data.append(result)
    return data
