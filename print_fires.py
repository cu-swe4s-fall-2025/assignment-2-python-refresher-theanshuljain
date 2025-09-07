from my_utils import get_column

# Give the arguments
file_name = 'Agrofood_co2_emission.csv'     # the dataset
country = 'United States of America'        # country of choice
country_column = 0                          # column number of country
fires_column = 3                            # forest fires column number

# Cal the function
fires = get_column(file_name, query_column = country_column, query_value = country, result_column = fires_column)

# Print the results
print(fires)