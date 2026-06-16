"""HIDDEN grader for calc.evaluate -- never copied into the agent's workdir
until after it finishes. Run: python3 grade.py

Covers the three bugs:
  - precedence (* / over + -)
  - truncate-toward-zero division (NOT Python floor //)
  - unary minus
plus parentheses, whitespace, and nesting. Prints "HIDDEN x/y" as last line.
"""

from calc import evaluate

CASES = [
    # precedence
    ("2+3*4", 14),
    ("1+2*3", 7),
    ("2*3+4", 10),
    ("2+3*4-6/2", 11),
    ("5-2*3", -1),
    # parentheses / nesting
    ("(2+3)*4", 20),
    ("(1+2)*(3+4)", 21),
    ("((2))", 2),
    ("2*(3+4*(5-1))", 38),
    # left-to-right subtraction
    ("10-2-3", 5),
    ("2-3-4", -5),
    ("0-5", -5),
    # division truncates toward zero
    ("7/2", 3),
    ("8/3", 2),
    ("6/4", 1),
    ("-7/2", -3),
    ("7/-2", -3),
    ("-8/3", -2),
    ("-6/4", -1),
    ("10/3*3", 9),
    # unary minus
    ("-3+2", -1),
    ("3*-2", -6),
    ("2*-3", -6),
    ("-(3+4)", -7),
    ("-(3+4)*2", -14),
    # whitespace
    ("  2 +  3 * 4 ", 14),
    ("100", 100),
]


def main() -> None:
    passed = 0
    for expr, want in CASES:
        try:
            got = evaluate(expr)
        except Exception as e:  # noqa: BLE001
            print(f"FAIL {expr!r}: want {want}, raised {type(e).__name__}: {e}")
            continue
        if got == want:
            passed += 1
        else:
            print(f"FAIL {expr!r}: want {want}, got {got}")
    print(f"HIDDEN {passed}/{len(CASES)}")
    raise SystemExit(0 if passed == len(CASES) else 1)


if __name__ == "__main__":
    main()
