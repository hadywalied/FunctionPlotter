from unittest import TestCase

import pytest
import sympy

from equation_parsing import translate


class Test(TestCase):
    cases = [['x^2', 'x**2'], ['Ln(x)', 'ln(x)'], ['12x+2x^3+x^2', '2x**3+x**2+12x']]

    def test_translate_x_squared(self):
        x = sympy.Symbol('x')
        y = translate('x^2')
        assert y == x ** 2

    def test_translate_polynomial(self):
        x = sympy.Symbol('x')
        y = translate('x^2+x+1')
        assert y == x ** 2 + x + 1

    def test_translate_sine_x(self):
        x = sympy.Symbol('x')
        y = translate('sin(x)')
        assert y == sympy.sin(x)

    def test_translate_exp_x(self):
        x = sympy.Symbol('x')
        y = translate('exp(x)')
        assert y == sympy.exp(x)

    def test_translate(self):
        x = sympy.Symbol('x')
        y = translate('e(x)')
        assert y != sympy.exp(x)
