# Project Description
This project demonstrates how to extract and analyze data from a CSV dataset using Python.  

- **`my_utils.py`** contains the `get_column` function, which extracts values from a specified column where another column matches a query value. The function returns a list of integers for easy analysis.  
- **`print_fires.py`** uses `get_column` to fetch and display the desired data for a chosen country. It accepts command-line arguments for flexible usage.  
- **`run.sh`** is a Bash script that runs `print_fires.py` with multiple examples, including error scenarios, demonstrating proper exception handling.

---

# Usage
The project uses command-line arguments to select the dataset, country, and columns for analysis.

## Running `print_fires.py`:
```bash
python3 print_fires.py --file_name <csv_file> --country "<country_name>" --country_column <column_index> --fires_column <column_index>
```
This is the `run.sh` file that runs the `print_fires.py` file. The `print_fires.py` file calls the `my_utils.py` file and runs the `get_column` function.

## Example Commands:
### 1. Working example:
```bash
python3 print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --country_column 0 --fires_column 3
```
#### Example output:
```bash
Working example: 
Number of forest fires in United States of America are: [1999, 1999, 1999, 1999, 1999, 1999, 3286, 1553, 3099, 3578, 3687, 534, 1475, 1224, 1201, 915, 1086, 1558, 2068, 1093, 912, 1330, 1173, 1284, 1336, 2235, 1438, 2664, 2457, 1190, 5405].
```
### 2. Error example:
```bash
python3 print_fires.py --file_name Agrofood_emission.csv --country "United States of America" --country_column 0 --fires_column 3
```
#### Example output:
```bash
First example with error: 
[Errno 2] No such file or directory: 'Agrofood_emission.csv'
```

## Running the Bash script
```bash
./run.sh
```
This code executes the `print_fires.py` file with some more examples included in the `run.sh` file.

---

# Function Details
`get_column(file_name, query_column, query_value, result_column=1):`
- **`file_name:`** Path to the CSV file.
- **`query_column:`** Index of the column to match query_value.
- **`query_value:`** Value to search in query_column.
- **`result_column:`** Index of the column whose values will be returned as integers (default 1).

**`Returns:`** A list of integers extracted from `result_column` where `query_column` matches `query_value`.

**`Error handling:`**
- Raises `FileNotFoundError` if the CSV file is missing.
- Raises `ValueError` if no matching data is found.
- Skips values that cannot be converted to integers.

---

