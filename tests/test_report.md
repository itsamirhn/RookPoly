Herman Lazarchyk, Maksim Zdobnikau

# Comprehensive Test Report for the RookPoly Project

## Project Context and Mathematical Basis
- **Project Name**: RookPoly
- **Subject Area**: Discrete Mathematics – Chess Polynomial
- **Mathematical Source**: [Wikipedia: Rook Polynomial](https://en.wikipedia.org/wiki/Rook_polynomial)
- **Project Description**: The RookPoly project focuses on the implementation and analysis of the chess polynomial. It consists of two main components: the `Board` class, responsible for representing and manipulating the state of the board, and the `Polynomial` class, which allows for mathematical operations on polynomials.

## Testing Goals
### `Board` Class
- **Goal**: Ensure that the `Board` class accurately handles operations on the board, which is crucial for calculations of the chess polynomial.
- **Importance**: The accuracy of each operation in the `Board` class is critical for the mathematical credibility of the chess polynomial results.

### `Polynomial` Class
- **Goal**: Ensure that the `Polynomial` class correctly performs mathematical operations on polynomials.
- **Importance**: The accuracy and mathematical correctness of the `Polynomial` class's operations are essential for reliable mathematical calculations.

## Testing Process
### Testing Method
- **Unit Testing**: Utilized the `unittest` framework in Python for testing functions of both classes.
- **Mathematical Verification**: Checked the consistency of both classes' operations with the mathematical principles of the chess polynomial.

### Metrics Used in the Testing Process
- **Test Cases**: The number and variety of tests, measuring the comprehensiveness of tests for both classes.
- **Test Results**: The number of tests concluded positively and negatively, indicating the quality of the code and the effectiveness of testing.
- **Mathematical Correctness**: Assessment of the consistency of both classes' operations with the mathematical principles of the chess polynomial, including calculation accuracy.

## Conducted Tests
### `Board` Class

| Test Name                    | Description                                       | Result   |
|------------------------------|---------------------------------------------------|----------|
| test_init                    | Proper board initialization                       | PASS ✅   |
| test_n                       | Number of rows (`n` property)                     | PASS ✅   |
| test_m                       | Number of columns (`m` property)                  | PASS ✅   |
| test_is_empty                | Check if the board is empty                       | PASS ✅   |
| test_get                     | Retrieve value from the board                     | PASS ✅   |
| test_set                     | Set value on the board                            | PASS ✅   |
| test_flip                    | Flip the board                                    | PASS ✅   |
| test_rotate                  | Rotate the board                                  | PASS ✅   |
| test_rtrim                   | Trim empty spaces on the right side               | PASS ✅   |
| test_remove_filled_rows      | Remove filled rows                                | PASS ✅   |
| test_simplify                | Simplify the board                                | PASS ✅   |
| test_get_empty_squares       | Identify empty squares                            | PASS ✅   |
| test_get_set                 | Read and write board cells                        | PASS ✅   |
| test_is_valid_cut_column     | Check if a column can be cut                      | PASS ✅   |
| test_get_cuttable_columns    | Identify columns that can be cut                  | PASS ✅   |
| test_cut_columns             | Cut columns                                       | PASS ✅   |
| test_get_sub_board           | Retrieve a sub-board                              | PASS ✅   |
| test_get_poly                | Generate polynomial based on the board            | PASS ✅   |
| test_eq                      | Compare two boards                                | PASS ✅   |
| test_repr                    | Object representation (__repr__ method)           | PASS ✅   |
| test_str                     | String representation (__str__ method)            | PASS ✅   |

### `Polynomial` Class

| Test Name                    | Description                                           | Result   |
|------------------------------|-------------------------------------------------------|----------|
| test_init                    | Initialize polynomial in different ways               | PASS ✅   |
| test_trim                    | Remove trailing zero coefficients                     | PASS ✅   |
| test_call                    | Evaluate polynomial at a given value                  | PASS ✅   |
| test_eq                      | Test equality of polynomial and other values          | PASS ✅   |
| test_add                     | Add two polynomials or a polynomial and scalar        | PASS ✅   |
| test_sub                     | Subtract a polynomial or scalar from a polynomial     | PASS ✅   |
| test_neg                     | Negate the polynomial                                 | PASS ✅   |
| test_mul                     | Multiply two polynomials or a polynomial and scalar   | PASS ✅   |
| test_radd                    | Right-hand addition with a scalar                     | PASS ✅   |
| test_rmul                    | Right-hand multiplication with a scalar               | PASS ✅   |
| test_rsub                    | Right-hand subtraction with a scalar                  | PASS ✅   |
| test_repr                    | Test the representation of the polynomial             | PASS ✅   |
| test_str                     | Test the string representation of the polynomial      | PASS ✅   |
| test_pow                     | Raise polynomial to a power (not implemented)         | PASS ✅   |

## Analysis and Future Directions
- **Consistency with Mathematical Theory**: The tests of both classes confirm their consistency with the principles of the chess polynomial, which is crucial for the credibility of the project.
- **Development Opportunities**: Considering the implementation of additional functions and test scenarios, especially for the `Polynomial` class, may enrich the project's functionality.
- **Recommendations**: It is recommended to conduct additional tests in more complex scenarios to fully utilize the potential of both classes in a mathematical context.

## Summary
The unit tests of the `Board` and `Polynomial` classes have successfully confirmed their correctness and effectiveness in the context of the RookPoly project. Both classes meet the mathematical requirements associated with the chess polynomial and provide a solid foundation for further research and development in the field of discrete mathematics. The test results provide strong foundations for further work on the project.
