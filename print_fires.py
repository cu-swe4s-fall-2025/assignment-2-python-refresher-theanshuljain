import argparse
from my_utils import get_column

def main():
    """
    print_fires.py

    Command line arguments to extract forest fire data for a chosen country from the
    Agrofood_co2_emission.csv dataset.
    """
    # Take command line arguments
    parser = argparse.ArgumentParser(
        description = "Print the number of forest fires for a given country from Agrofood_co2_emission.csv dataset."
    )

    # Command line argument for country
    parser.add_argument(
        "--country",
        type = str,
        required = True,
        help = "Country of interest"
    )

    # Command line argument for country_column
    parser.add_argument(
        "--country_column",
        type = int,
        required = True,
        help = "Column number for the country of interest"
    )
    
    # Command line argument for fires_column
    parser.add_argument(
        "--fires_column",
        type = int,
        required = True,
        help = "Column number for the forest fires"
    )

    # Command line argument for file_name
    parser.add_argument(
        "--file_name",
        type = str,
        required = True,
        help = ".csv file that has the data"
    )

    # Creating args object to hold the values
    args = parser.parse_args()

    # Call the get_column function
    try:
        fires = get_column(
            args.file_name,
            query_column = args.country_column,
            query_value = args.country,
            result_column = args.fires_column
        )
        print(f"Number of forest fires in {args.country} are: {fires}.")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Main function
if __name__ == "__main__":
    main()