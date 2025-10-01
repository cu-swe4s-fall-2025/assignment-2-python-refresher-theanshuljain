"""
print_fires.py

Command line interface for extracting forest fire data for a chosen country
from the Agrofood_co2_emission.csv dataset. Optionally performs a statistical
operation (mean, median, or stddev) on the extracted values.
"""

import argparse
import sys
from my_utils import (
    get_column,
    calculate_mean,
    calculate_median,
    calculate_stddev,
)


def main():
    """Main function to handle command line arguments and print results."""
    parser = argparse.ArgumentParser(
        description=(
            "Extract forest fire data for a given country from "
            "Agrofood_co2_emission.csv and optionally perform "
            "a statistical operation."
        )
    )

    parser.add_argument(
        "--country",
        type=str,
        required=True,
        help="Country of interest."
        )

    parser.add_argument(
        "--country_column",
        type=int,
        required=True,
        help="Column number for the country of interest."
        )

    parser.add_argument(
        "--fires_column",
        type=int,
        required=True,
        help="Column number for the forest fires."
        )

    parser.add_argument(
        "--file_name",
        type=str,
        required=True,
        help="Path to the .csv file that contains the dataset."
        )

    parser.add_argument(
        "--operation",
        type=str,
        choices=["mean", "median", "stddev"],
        help="Optional statistical operation (mean, median, stddev)."
        )

    args = parser.parse_args()

    try:
        fires = get_column(
            args.file_name,
            query_column=args.country_column,
            query_value=args.country,
            result_column=args.fires_column
        )

        if args.operation == "mean":
            result = calculate_mean(fires)
            print(f"Mean number of forest fires in {args.country}: {result}")
        elif args.operation == "median":
            result = calculate_median(fires)
            print(f"Median number of forest fires in {args.country}: {result}")
        elif args.operation == "stddev":
            result = calculate_stddev(fires)
            print(
                f"Standard deviation of forest fires in {args.country}: "
                f"{result}"
            )
        else:
            print(f"Number of forest fires in {args.country}: {fires}")

    except FileNotFoundError as fnf_error:
        print(fnf_error, file=sys.stderr)
        sys.exit(1)
    except ValueError as ve:
        print(ve, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
