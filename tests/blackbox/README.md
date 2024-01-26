## Blackbox Testing

This folder contains scripts for blackbox testing of the program. Blackbox testing focuses on testing the program's functionality without considering its internal structure. 
Two types of tests are included: correctness tests and time tests.

### Correctness Tests

**Purpose:**
- To ensure that the program produces correct outputs for various input cases.
- Verifies if the program's logic and algorithms are functioning as expected.

**Running:**
```bash
./correctness_test.sh
```

**Note:** to add or modify test cases, navigate to [test_cases/correctness](test_cases/correctness). The format of each test case is as follows:
- `test_name.in`: input file containing the input to the program.
- `test_name.out`: output file containing the expected output of the program.

### Time Tests

**Purpose:**
- To measure and validate the program's execution time against expected time limits.
- Ensures that the program performs efficiently under different scenarios.

**Running:**
```bash
./time_test.sh
```

**Note:** to add or modify test cases, navigate to [test_cases/time](test_cases/time). The format of each test case is as follows:
- `test_name.in`: input file containing the input to the program.
- `test_name.out`: file containing the maximum expected execution time of the program in seconds.
