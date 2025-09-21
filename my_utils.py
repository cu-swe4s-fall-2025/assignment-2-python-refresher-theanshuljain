import csv

def get_column(file_name, query_column, query_value, result_column = 1):

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

                if row[query_column] == query_value:
                    try:
                        # Converting to Integers
                        results.append(int(row[result_column]))
                    except ValueError:
                        # SKipping the values that cannot be convered to integers
                        continue

    except Exception as e:
        print(f"Error: {e}")

    return results