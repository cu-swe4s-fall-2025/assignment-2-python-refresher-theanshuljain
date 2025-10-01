"""
my_utils.py

Utility functions for working with CSV data and performing simple statistics.

Functions:
- get_column: Extract values from a CSV file where a given column matches a
query value.
- calculate_mean: Compute the arithmetic mean of a list of integers.
- calculate_median: Compute the median of a list of integers.
- calculate_stddev: Compute the population standard deviation of a list of
integers.
"""

import csv
import math
from typing import List


def get_column(file_name: str,
               query_column: int,
               query_value: str,
               result_column: int = 1) -> List[int]:
    """
    Extract values from a CSV file where a given column matches a query value.

    Args:
        file_name (str): Path to the CSV file.
        query_column (int): Index of the column to search for the query_value.
        query_value (str): Value to look for in the query_column.
        result_column (int, optional): Index of the result column.
            Defaults to 1.

    Returns:
        List[int]: A list of integers extracted from the result_column.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If no results are found for the given query.
        RuntimeError: For unexpected errors.
    """
    results: List[int] = []

    try:
        with open(file_name, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)

            # Skip the header row
            next(reader)

            for row in reader:
                # Skip rows with insufficient columns
                if len(row) <= max(query_column, result_column):
                    continue

                if row[query_column].strip() == query_value.strip():
                    try:
                        results.append(int(float(row[result_column].strip())))
                    except ValueError:
                        # Skip rows with non-numeric values
                        continue

    except FileNotFoundError as fnf_error:
        raise FileNotFoundError(fnf_error) from None
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {e}") from e

    if not results:
        raise ValueError(
            f"No data found for '{query_value}' in column {query_column}."
        )

    return results


def calculate_mean(values: List[int]) -> float:
    """Calculate the arithmetic mean of a list of integers."""
    if not values:
        raise ValueError("calculate_mean() received an empty list.")
    return sum(values) / len(values)


def calculate_median(values: List[int]) -> float:
    """Calculate the median of a list of integers."""
    if not values:
        raise ValueError("calculate_median() received an empty list.")

    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2

    if n % 2 == 1:
        return float(sorted_values[mid])

    return (sorted_values[mid - 1] + sorted_values[mid]) / 2.0


def calculate_stddev(values: List[int]) -> float:
    """Calculate the population standard deviation of a list of integers."""
    if not values:
        raise ValueError("calculate_stddev() received an empty list.")

    mean = calculate_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)

    return math.sqrt(variance)
