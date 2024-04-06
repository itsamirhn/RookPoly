#!/bin/bash

# This script runs the program on all test cases in the test_cases directory
CASES_DIR="$(dirname "$0")/test_cases/time"
PROGRAM_PATH="python3 $(dirname "$0")/../../main.py"

# ANSI color codes
YELLOW='\033[1;93m'
GREEN='\033[1;32m'
RED='\033[1;31m'
RESET='\033[0m'

ok_count=0
fail_count=0

pushd "$(dirname "$0")" > /dev/null || exit 1

for input_file in "$CASES_DIR"/*.in; do
    test_name=$(basename "${input_file%.in}")
    expected_output_file="$CASES_DIR/$test_name.out"

    echo -e -n "Running test ${YELLOW}$test_name${RESET}..."

    # Measure execution time using the time command
    output=$( { time -p $PROGRAM_PATH < "$input_file" >/dev/null; } 2>&1 )

    # Extract the real time from the time command output
    actual_time=$(echo "$output" | awk '/real/ {print $2}')

    # Read the expected time from the test case output file
    expected_time=$(grep -oE "[0-9.]+" "$expected_output_file" | cut -d' ' -f2)

    # Compare the actual and expected time
    if [ -n "$expected_time" ] && (( $(echo "$actual_time < $expected_time" | bc -l) )); then
        ((ok_count++))
        echo -e " ${GREEN}[PASSED]${RESET}"
    else
        ((fail_count++))
        echo -e " ${RED}[FAILED]${RESET}"
    fi

    echo -e "Actual time: ${actual_time} seconds"
    echo -e "Expected time: below ${expected_time} seconds"
done

popd > /dev/null || exit 1

echo -e "\nSummary:"
echo -e "Passed tests: ${GREEN}$ok_count${RESET}"
echo -e "Failed tests: ${RED}$fail_count${RESET}"

[[ "$fail_count" == 0 ]] || exit 1
