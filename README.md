# RookPoly

Simple recursive tool for finding [Rook Polynomial](https://en.m.wikipedia.org/wiki/Rook_polynomial)

Be aware that recursion is not efficient enough, and it's using random choices

## Install
Just clone the project:

```bash
$ git clone git@github.com:itsamirhn/RookPoly.git

$ cd RookPoly
```

## Usage

For example for a board like this:

<img alt="Sample Board" height="100" src="https://github.com/itsamirhn/RookPoly/blob/master/sample.png?raw=true" width="150" height="150"/>

Use the following input to find the rook polynomial:

```bash
Enter numberEnter number of rows: 5

00001
01010
01100
10010
00000
```
* `0: Rook can be placed in this place`
* `1: Rook can't be placed here`