import csv

def get_column(file_name, query_column, query_value, result_column):
    results = []

    f = open(file_name, 'r')
    first_line = True
    for l in f:
        if first_line:
            first_line = False
            continue
        A = l.rstrip().split(',')
        if A[query_column] == query_value:
            results.append(A[result_column])
    f.close()
    return results