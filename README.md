# RookPoly

Simple recursive tool for finding [Rook Polynomial](https://en.m.wikipedia.org/wiki/Rook_polynomial)

Be aware that recursion is not efficient enough, and it's using random choices. So maybe it gets slow for large numbers.

## Install
Just clone the project:

```shell
$ git clone https://github.com/itsamirhn/RookPoly.git

$ cd RookPoly
```

## Usage

Run the main program:
```shell
$ python3 main.py
```

For example, for a board like this:

<img alt="Sample Board" height="150" src="https://github.com/itsamirhn/RookPoly/blob/master/sample.png?raw=true" width="150"/>

Use the following input to find the rook polynomial:

```shell
Enter numberEnter number of rows: 5

00001
01010
01100
10010
00000
```
* `0`: Rook can be placed in this place
* `1`: Rook can't be placed here

Sample output for this example:
```
24X^5 + 164X^4 + 226X^3 + 104X^2 + 18X + 1
```

## Tests
Tests, instructions for running them and test report can be found in [tests](tests) folder.