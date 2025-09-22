#!/bin/bash
echo "Working example: "
python3 print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --country_column 0 --fires_column 3

echo "First example with error: "
# Incorrect file name throws error
python3 print_fires.py --file_name Agrofood_emission.csv --country "United States of America" --country_column 0 --fires_column 3

echo "Second example with error: "
# Incorrect column index throws error
python3 print_fires.py --file_name Agrofood_co2_emission.csv --country "United States America" --country_column 0 --fires_column 3