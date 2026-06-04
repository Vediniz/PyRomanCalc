HELP_TEXT = """
================ ROMAN EXPRESSION CALCULATOR ================
Valid Roman Numerals:
  I = 1
  V = 5
  X = 10
  L = 50
  C = 100
  D = 500
  M = 1000

Supported Operators:
  +   Addition
  -   Subtraction
  *   Multiplication
  /   Division
  ^   Power

Grouping:
  ( ) Parentheses are supported.

Roman Decimal Numbers:
  Use square brackets to represent the decimal part.
  [V]      = 0.05
  [L]      = 0.50
  [LXXV]   = 0.75

Commands:
  help
  exit
============================================================
"""

INPUT_TEXT = '[help | exit]\nExpression: '

ERROR_EMPTY_INPUT = 'Input cannot be empty'
ERROR_NOT_REPEATABLE = '{} is not repeatable'
ERROR_MAX_REPETITIONS = '{} can be repeated 3 times'
ERROR_INVALID_SUBTRACTION_CHAR = '{} cannot be used as subtraction'
ERROR_INVALID_SUBTRACTION = 'Invalid subtraction: {}'
ERROR_INVALID_CHARACTER = 'Invalid character: {}'
ERROR_INVALID_PARENTHESES = 'Invalid parentheses'
ERROR_INVALID_OPERATOR_SEQUENCE = 'Invalid operator sequence: {}{}'
ERROR_MISSING_OPERATOR = 'Missing operator between {} and {}'
ERROR_EXPRESSION_START_OPERATOR = 'Expression cannot start with operator'
ERROR_EXPRESSION_END_OPERATOR = 'Expression cannot end with operator'
ERROR_EXPRESSION_IN_DECIMAL = 'Expressions inside [] are not supported'
