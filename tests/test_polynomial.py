import unittest

from rookpoly.polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def setUp(self):
        self.p1 = Polynomial(1, 2, 3)
        self.p2 = Polynomial(3, 2, 1)
        self.scalar = 5
        self.zero_poly = Polynomial()

    def test_init(self):
        # Test various ways of initializing a Polynomial
        self.assertEqual(Polynomial(1, 2, 3).coeffs, [1, 2, 3])
        self.assertEqual(Polynomial([1, 2, 3]).coeffs, [1, 2, 3])
        self.assertEqual(Polynomial(self.p1).coeffs, self.p1.coeffs)
        self.assertEqual(Polynomial(5).coeffs, [5])
        self.assertEqual(Polynomial().coeffs, [])
        self.assertEqual(Polynomial([1, 2, 3, 0, 0, 0]).coeffs, [1, 2, 3])

    def test_trim(self):
        # Test the trimming of trailing zeros in a polynomial's coefficients
        p = Polynomial([1, 0, 0, 0, 2])
        p.trim()
        self.assertEqual(p.coeffs, [1, 0, 0, 0, 2])

    def test_call(self):
        # Test polynomial evaluation at given values
        self.assertEqual(self.p1(0), 1)
        self.assertEqual(self.p1(1), 6)
        self.assertEqual(self.p1(2), 17)

    def test_eq(self):
        # Test equality comparisons between polynomials and a polynomial with a scalar
        self.assertTrue(self.p1 == Polynomial(1, 2, 3))
        self.assertFalse(self.p1 == self.p2)

        # Test case for a zero polynomial with a single zero coefficient
        zero_poly_single_coef = Polynomial(0)
        self.assertTrue(zero_poly_single_coef == 0)

        # Adjusting the test for a zero polynomial with no coefficients
        # A zero polynomial (with no coefficients) should be considered equal to the scalar 0
        self.assertTrue(self.zero_poly == 0)

    def test_add(self):
        # Test addition of polynomials and a polynomial with a scalar
        self.assertEqual((self.p1 + self.p2).coeffs, [4, 4, 4])
        self.assertEqual((self.p1 + self.scalar).coeffs, [6, 2, 3])

    def test_sub(self):
        # Test subtraction of polynomials and a polynomial with a scalar
        self.assertEqual((self.p1 - self.p2).coeffs, [-2, 0, 2])
        self.assertEqual((self.p1 - self.scalar).coeffs, [-4, 2, 3])

    def test_neg(self):
        # Test negation of a polynomial
        self.assertEqual((-self.p1).coeffs, [-1, -2, -3])

    def test_mul(self):
        # Test multiplication of polynomials and a polynomial with a scalar
        self.assertEqual((self.p1 * self.p2).coeffs, [3, 8, 14, 8, 3])
        self.assertEqual((self.p1 * self.scalar).coeffs, [5, 10, 15])

    def test_radd(self):
        # Test right-hand addition (scalar + polynomial)
        self.assertEqual((self.scalar + self.p1).coeffs, [6, 2, 3])

    def test_rmul(self):
        # Test right-hand multiplication (scalar * polynomial)
        self.assertEqual((self.scalar * self.p1).coeffs, [5, 10, 15])

    def test_rsub(self):
        # Test right-hand subtraction (scalar - polynomial)
        self.assertEqual((self.scalar - self.p1).coeffs, [4, -2, -3])

    def test_repr(self):
        # Test the __repr__ method for a polynomial
        self.assertEqual(repr(self.p1), "Polynomial([1, 2, 3])")

    def test_str(self):
        # Test the string representation of a polynomial
        self.assertEqual(str(self.p1), "3X^2 + 2X + 1")
        self.assertEqual(str(self.zero_poly), "0")

    def test_pow(self):
        # Test polynomial exponentiation (should raise NotImplementedError)
        with self.assertRaises(NotImplementedError):
            _ = self.p1 ** 2


if __name__ == '__main__':
    unittest.main()
