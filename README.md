# Project Description
This project demonstrates how to extract and analyze data from a CSV dataset using Python.  

- **`my_utils.py`** contains utility functions:
  - `get_column`: extracts values from a specified column where another column matches a query value.
  - `calculate_mean`, `calculate_median`, and `calculate_stddev`: perform statistical analysis on lists of integers.  
- **`print_fires.py`** uses these functions to fetch and display data for a chosen country. It accepts command-line arguments for flexible usage, including an optional `--operation` argument (`mean`, `median`, or `stddev`).  
- **`run.sh`** is a Bash script that runs `print_fires.py` with multiple examples, including error scenarios, demonstrating proper exception handling.  
- **Unit tests (`test/unit/test_my_utils.py`)** ensure that statistical functions behave correctly for normal and error cases.  
- **Functional tests (`test/func/test_print_fires.sh`)** validate `print_fires.py` end-to-end using a small test dataset (`test/func/test_data.csv`) and the [ssshtest](https://github.com/ryanlayer/ssshtest) framework.

---

# Usage
The project uses command-line arguments to select the dataset, country, and columns for analysis.

## Running `print_fires.py`:
```bash
python3 print_fires.py --file_name <csv_file> --country "<country_name>" --country_column <column_index> --fires_column <column_index> [--operation mean|median|stddev]
```

If `--operation` is omitted, the raw values are printed.

---

## Example Commands:

### 1. Working example (raw values):

```bash
python3 print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --country_column 0 --fires_column 3
```

#### Example output:

```bash
Number of forest fires in United States of America: [1999, 3286, 1553, ...]
```

### 2. Working example (mean):

```bash
python3 print_fires.py --file_name test/func/test_data.csv --country "United States of America" --country_column 0 --fires_column 3 --operation mean
```

#### Example output:

```bash
Mean number of forest fires in United States of America: 22.5
```

### 3. Error example (missing file):

```bash
python3 print_fires.py --file_name Agrofood_emission.csv --country "United States of America" --country_column 0 --fires_column 3
```

#### Example output:

```bash
[Errno 2] No such file or directory: 'Agrofood_emission.csv'
```

---

# Running the Bash script

```bash
./run.sh
```

This executes `print_fires.py` with examples included in the `run.sh` file.

---

# Running Tests

### Unit tests

Run all unit tests:

```bash
python3 -m unittest discover -s test/unit -p "test_*.py" -v
```

### Functional tests

Make the script executable and run:

```bash
chmod +x test/func/test_print_fires.sh
./test/func/test_print_fires.sh
```

---

# Automated Testing with GitHub Actions

This repository implements continuous integration using GitHub Actions to ensure code quality and functionality. The automated testing system:

## Testing Triggers
- **Push events**: Tests run automatically on pushes to any branch
- **Pull requests**: Tests run when pull requests are made to the main branch

## Test Suite
The CI pipeline includes three types of automated testing:

1. **Unit Tests**: Validates individual functions in `my_utils.py` using Python's unittest framework
2. **Functional Tests**: End-to-end testing of `print_fires.py` using the ssshtest framework
3. **Style Checks**: Code quality enforcement using pycodestyle linter

## Workflow Configuration
- **Environment**: Tests run on Ubuntu latest with micromamba for dependency management
- **Dependencies**: Managed through `environment.yml` with conda-forge and bioconda channels
- **Parallel Execution**: All three test types run concurrently for faster feedback

The automated testing ensures that all code changes maintain functionality and adhere to Python style guidelines before integration.

---

# Function Details

### `get_column(file_name, query_column, query_value, result_column=1)`

- **`file_name:`** Path to the CSV file.
- **`query_column:`** Index of the column to match query_value.
- **`query_value:`** Value to search in query_column.
- **`result_column:`** Index of the column whose values will be returned as integers (default 1).

**Returns:** A list of integers extracted from `result_column`.

**Error handling:**
- Raises `FileNotFoundError` if the CSV file is missing.
- Raises `ValueError` if no matching data is found.
- Skips values that cannot be converted to integers.

---

### `calculate_mean(values)`

Computes the arithmetic mean of a list of integers.  
**Raises:** `ValueError` if the list is empty.

### `calculate_median(values)`

Computes the median of a list of integers.  
If the list length is even, returns the average of the two middle values.  
**Raises:** `ValueError` if the list is empty.

### `calculate_stddev(values)`

Computes the **population** standard deviation of a list of integers.  
**Raises:** `ValueError` if the list is empty.

---
