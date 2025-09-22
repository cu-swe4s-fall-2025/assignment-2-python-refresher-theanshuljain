import csv

def get_column(file_name, query_column, query_value, result_column = 1):
    """
    Extract values from a CSV file where a given column matches a query value.

    Args:
        file_name (str): Path to the CSV file.
        query_column (int): Index of the column to search for the query_value.
        query_value (str): Value to look for in the query_column.
        result_column (int, optional): Index of the result column. Defaults to 1.
    
    Returns:
        list[int]: A list of integers extracted from the result_column.
    """

    # Array to store results
    results = []

    try:
        with open(file_name, "r", newline = "", encoding = "utf-8") as f:
            reader = csv.reader(f)

            # Skip the header row
            next(reader)

            for row in reader:
                # Skipping the row does not have the desired values
                if len(row) <= max(query_column, result_column):
                    continue

                if row[query_column].strip() == query_value.strip():
                    try:
                        # Converting to Integers
                        results.append(int(float(row[result_column].strip())))
                    except ValueError:
                        # Skipping values that cannot be converted to integers
                        continue

    except FileNotFoundError as fnf_error:
        raise FileNotFoundError(fnf_error)
    except Exception as e:
        raise Exception(f"Unexpected Error: {e}")
    
    # Raise an error if there are no results
    if not results:
        raise ValueError(f"No data could be found for '{query_value}' in column {query_column}.")

    return results