#!/bin/bash
# Functional tests for print_fires.py using ssshtest framework

# Ensure ssshtest is available
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# --- Working case: raw values ---
run fires_raw python3 print_fires.py \
  --file_name test/func/test_data.csv \
  --country "United States of America" \
  --country_column 0 \
  --fires_column 3
assert_in_stdout "Number of forest fires in United States of America"
assert_exit_code 0

# --- Working case: mean ---
run fires_mean python3 print_fires.py \
  --file_name test/func/test_data.csv \
  --country "United States of America" \
  --country_column 0 \
  --fires_column 3 \
  --operation mean
assert_in_stdout "Mean number of forest fires in United States of America"
assert_exit_code 0

# --- Working case: median ---
run fires_median python3 print_fires.py \
  --file_name test/func/test_data.csv \
  --country "United States of America" \
  --country_column 0 \
  --fires_column 3 \
  --operation median
assert_in_stdout "Median number of forest fires in United States of America"
assert_exit_code 0

# --- Working case: stddev ---
run fires_stddev python3 print_fires.py \
  --file_name test/func/test_data.csv \
  --country "United States of America" \
  --country_column 0 \
  --fires_column 3 \
  --operation stddev
assert_in_stdout "Standard deviation of forest fires in United States of America"
assert_exit_code 0

# --- Error case: invalid file ---
run fires_invalid_file python3 print_fires.py \
  --file_name test/func/missing.csv \
  --country "United States of America" \
  --country_column 0 \
  --fires_column 3
assert_in_stderr "No such file"
assert_exit_code 1

# --- Error case: invalid column ---
run fires_invalid_column python3 print_fires.py \
  --file_name test/func/test_data.csv \
  --country "United States of America" \
  --country_column 10 \
  --fires_column 15
assert_in_stderr "No data found"
assert_exit_code 1