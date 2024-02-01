#!/bin/bash

# This script runs the program on all test cases in the test_cases directory
CASES_DIR="$(dirname "$0")/test_cases/correctness"
PROGRAM_PATH="python3 $(dirname "$0")/../../main.py"

# ANSI color codes
YELLOW='\033[1;93m'
GREEN='\033[1;32m'
RED='\033[1;31m'
RESET='\033[0m'

ok_count=0
fail_count=0
error_count=0

pushd "$(dirname "$0")" > /dev/null || exit 1

# Define the patterns to exclude
exclude_patterns="Calculating...|Enter number of rows|Time"

for input_file in "$CASES_DIR"/*.in; do
    test_name=$(basename "${input_file%.in}")
    expected_output_file="$CASES_DIR/$test_name.out"

    echo -e -n "Running test ${YELLOW}$test_name${RESET}..."

    # Redirect input from the input file
    output=$($PROGRAM_PATH < "$input_file")
    exit_code=$?

    if [ "$exit_code" -eq 0 ]; then
        # Simplify the output and expected output by excluding unnecessary output data
        simplified_output=$(echo "$output" | grep -vE "$exclude_patterns")
        simplified_expected_output=$(grep -vE "$exclude_patterns" "$expected_output_file")

        if [ "$simplified_output" == "$simplified_expected_output" ]; then
            ((ok_count++))
            echo -e " ${GREEN}[PASSED]${RESET}"
        else
            ((fail_count++))
            echo -e " ${RED}[FAILED]${RESET}"
            echo -e "Expected output:   ${GREEN}$simplified_expected_output${RESET}"
            echo -e "Actual output:     ${RED}$simplified_output${RESET}"
        fi
    else
          ((error_count++))
          echo -e "${RED}[ERROR]${RESET}"
    fi
done

popd > /dev/null || exit 1

echo -e "\nSummary:"
echo -e "Passed tests: ${GREEN}$ok_count${RESET}"
echo -e "Failed tests: ${RED}$fail_count${RESET}"
echo -e "Errored tests: ${RED}$error_count${RESET}"

[[ "$fail_count" == 0 && "$error_count" == 0 ]] || exit 1
