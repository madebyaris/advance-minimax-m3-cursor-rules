"""Integer arithmetic expression evaluator.

Contract (the spec the implementation must satisfy):

- Supports binary operators: + - * /
- Operator precedence: * and / bind tighter than + and -
- Parentheses override precedence: "(2+3)*4" == 20
- Division truncates TOWARD ZERO (like C), not toward negative infinity:
      7 / 2  ==  3
     -7 / 2  == -3
      7 / -2 == -3
- Unary minus is supported: "-3 + 2" == -1, "3 * -2" == -6, "-(3+4)" == -7
- Whitespace is insignificant: "  2 + 3 * 4 " == 14
- Operands are non-negative integer literals; results may be negative.

evaluate(expr) -> int
"""

from __future__ import annotations


def _tokenize(expr: str) -> list:
    tokens: list = []
    s = expr.replace(" ", "")
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit():
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            tokens.append(int(s[i:j]))
            i = j
        elif c in "+-*/()":
            tokens.append(c)
            i += 1
        else:
            raise ValueError(f"bad character {c!r}")
    return tokens


def _eval_seq(tokens: list):
    # NOTE: folds strictly left-to-right.
    value, tokens = _eval_atom(tokens)
    while tokens and tokens[0] in "+-*/":
        op = tokens[0]
        right, tokens = _eval_atom(tokens[1:])
        if op == "+":
            value = value + right
        elif op == "-":
            value = value - right
        elif op == "*":
            value = value * right
        else:  # "/"
            value = value // right
    return value, tokens


def _eval_atom(tokens: list):
    tok = tokens[0]
    if tok == "(":
        value, tokens = _eval_seq(tokens[1:])
        if not tokens or tokens[0] != ")":
            raise ValueError("missing closing parenthesis")
        return value, tokens[1:]
    if isinstance(tok, int):
        return tok, tokens[1:]
    raise ValueError(f"unexpected token {tok!r}")


def evaluate(expr: str) -> int:
    tokens = _tokenize(expr)
    if not tokens:
        raise ValueError("empty expression")
    value, rest = _eval_seq(tokens)
    if rest:
        raise ValueError(f"unexpected trailing tokens: {rest}")
    return value
