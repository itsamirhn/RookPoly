from collections import abc
import itertools


class Polynomial(object):

    def __init__(self, *args):
        """
        Initialize a Polynomial in one of three ways:
        - Polynomial(poly) from another Polynomial (copy constructor)
        - Polynomial([1, 2, 3, ...]) from a sequence of coefficients
        - Polynomial(1, 2, 3, ...) from a list of scalars as coefficients
        """
        super(Polynomial, self).__init__()
        if len(args) == 1:
            val = args[0]
            if isinstance(val, Polynomial):  # Copy constructor
                self.coeffs = val.coeffs[:]
            elif isinstance(val, abc.Iterable):  # From sequence
                self.coeffs = list(val)
            else:  # From single scalar
                self.coeffs = [val + 0]
        else:  # From multiple scalars
            self.coeffs = [i + 0 for i in args]
        self.trim()

    def trim(self):
        """Remove trailing 0-coefficients"""
        while self.coeffs and self.coeffs[-1] == 0:
            self.coeffs.pop()

    def __call__(self, val):
        """Evaluate at X == val"""
        return sum(co * (val ** po) for po, co in enumerate(self.coeffs))

    def __eq__(self, val):
        """Test self == val"""
        if isinstance(val, Polynomial):
            return self.coeffs == val.coeffs
        else:
            return (len(self.coeffs) == 1 and self.coeffs[0] == val) or (len(self.coeffs) == 0 and val == 0)

    def __add__(self, val):
        """Return self + val"""
        if isinstance(val, Polynomial):
            res = [a + b for a, b in itertools.zip_longest(self.coeffs, val.coeffs, fillvalue=0)]
        else:
            res = self.coeffs[:]
            res[0] += val
        return Polynomial(res)

    def __sub__(self, val):
        """Return self - val"""
        return self + (-val)

    def __neg__(self):
        """Return -self"""
        return Polynomial([-co for co in self.coeffs])

    def __mul__(self, val):
        """Return self * val"""
        if isinstance(val, Polynomial):
            res = [0] * (len(self.coeffs) + len(val.coeffs) - 1)
            for self_pow, self_co in enumerate(self.coeffs):
                for val_pow, val_co in enumerate(val.coeffs):
                    res[self_pow + val_pow] += self_co * val_co
        else:
            res = [co * val for co in self.coeffs]
        return Polynomial(res)

    def __radd__(self, val):
        """Return val + self"""
        return self + val

    def __rmul__(self, val):
        """Return val * self"""
        return self * val

    def __rsub__(self, val):
        """Return val - self"""
        return -self + val

    def __repr__(self):
        return f"Polynomial({self.coeffs})"

    def __str__(self):
        if not self.coeffs:
            return "0"
        terms = []
        for po, co in enumerate(self.coeffs):
            if co:
                term = f"{co}"
                if po >= 1:
                    term += "X"
                if po >= 2:
                    term += f"^{po}"
                terms.append(term)
        return " + ".join(reversed(terms))

    # Not implemented yet
    def __pow__(self, y, z=None):
        raise NotImplementedError
