import csv

# Implement the get_column function
def get_column(file_name, query_column, query_value, result_column):
    results = []                                # array to store results

    f = open(file_name, 'r')
    first_line = True
    for l in f:
        if first_line:
            first_line = False                  # skipping the header
            continue
        A = l.rstrip().split(',')               # splitting each row into an array
        if A[query_column] == query_value:      # comparing query_column with query_value
            results.append(A[result_column])    # forming the results array
    f.close()
    return results