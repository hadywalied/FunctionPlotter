from __future__ import print_function

import re

from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_application,
                                        implicit_multiplication)

symbol_map = {
    '^': '**',
    'Ln': 'log ',
    'Sin': 'sin ',
    'Cos': 'cos '
}


def translate(bad_text):
    """My custom string-to-Equation-ready SymPy expression translation function

    Arguments:
        bad_text (str): text that is in some bad format that requires string manipulation
            including custom string modifications to math functions, symbols, and operators
            defined by the global symbol_map dictionary (for substitutions), and the regexs
            compiled herein. More advanced manipulations providied by SymPy are defined by
            the global variable `transformations` are inputs to the SymPy parser
    Returns:
        expr (sympy expression): A SymPy expresion created by the SymPy expression parser
            after first doing custom string modifications to math functions, symbols, and operators
    """
    to_symbols = re.compile('|'.join(re.escape(key) for key in symbol_map.keys()))
    bad_text = to_symbols.sub(lambda x: symbol_map[x.group()], bad_text)
    bad_text = re.sub('\n', '', bad_text)
    text = re.sub(r"\s+a(\d)", r"a_\1", bad_text)
    transformations = standard_transformations + (implicit_multiplication, implicit_application)
    expr = parse_expr(text, transformations=transformations)
    return expr
