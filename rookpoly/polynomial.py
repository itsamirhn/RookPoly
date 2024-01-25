from collections import abc
import itertools


class Polynomial(object):
    def __init__(self, *args):
        """
        Create a polynomial in one of three ways:

        p = Polynomial(poly)           # copy constructor
        p = Polynomial([1,2,3 ...])    # from sequence
        p = Polynomial(1, 2, 3 ...)    # from scalars
        """
        super(Polynomial, self).__init__()
        if len(args) == 1:
            val = args[0]
            if isinstance(val, Polynomial):  # copy constructor
                self.coeffs = val.coeffs[:]
            elif isinstance(val, abc.Iterable):  # from sequence
                self.coeffs = list(val)
            else:  # from single scalar
                self.coeffs = [val + 0]
        else:  # multiple scalars
            self.coeffs = [i + 0 for i in args]
        self.trim()

    def __add__(self, val):
        """Return self+val"""
        if isinstance(val, Polynomial):  # add Polynomial
            res = [a + b for a, b in itertools.zip_longest(self.coeffs, val.coeffs, fillvalue=0)]
        else:  # add scalar
            if self.coeffs:
                res = self.coeffs[:]
                res[0] += val
            else:
                res = val
        return self.__class__(res)

    def __call__(self, val):
        """Evaluate at X==val"""
        res = 0
        pwr = 1
        for co in self.coeffs:
            res += co * pwr
            pwr *= val
        return res

    def __eq__(self, val):
        """Test self==val"""
        if isinstance(val, Polynomial):
            return self.coeffs == val.coeffs
        else:
            return len(self.coeffs) == 1 and self.coeffs[0] == val

    def __mul__(self, val):
        """Return self*val"""
        if isinstance(val, Polynomial):
            _s = self.coeffs
            _v = val.coeffs
            res = [0] * (len(_s) + len(_v) - 1)
            for selfpow, selfco in enumerate(_s):
                for valpow, valco in enumerate(_v):
                    res[selfpow + valpow] += selfco * valco
        else:
            res = [co * val for co in self.coeffs]
        return self.__class__(res)

    def __neg__(self):
        """Return -self"""
        return self.__class__([-co for co in self.coeffs])

    def __pow__(self, y, z=None):
        raise NotImplementedError

    def __radd__(self, val):
        """Return val+self"""
        return self + val

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, self.coeffs)

    def __rmul__(self, val):
        """Return val*self"""
        return self * val

    def __rsub__(self, val):
        """Return val-self"""
        return -self + val

    def __str__(self):
        """Return string formatted as aX^3 + bX^2 + c^X + d"""
        res = []
        for po, co in enumerate(self.coeffs):
            if co:
                if po == 0:
                    po = ''
                elif po == 1:
                    po = 'X'
                else:
                    po = 'X^' + str(po)
                res.append(str(co) + po)
        if res:
            res.reverse()
            return ' + '.join(res)
        else:
            return "0"

    def __sub__(self, val):
        """Return self-val"""
        return self.__add__(-val)

    def trim(self):
        """Remove trailing 0-coefficients"""
        _co = self.coeffs
        if _co:
            offs = len(_co) - 1
            if _co[offs] == 0:
                offs -= 1
                while offs >= 0 and _co[offs] == 0:
                    offs -= 1
                del _co[offs + 1:]
