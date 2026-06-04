from CONST_TEXT import *

ROMAN_VALUES: dict[str, int] = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

VALID_SUBTRACTIONS = {
    'I': {'V', 'X'},
    'X': {'L', 'C'},
    'C': {'D', 'M'},
}

REPEATABLE = {'I', 'X', 'C', 'M'}
NON_REPEATABLE = {'V', 'L', 'D'}

OPERATORS = {'+', '-', '*', '/', '^'}
SPECIAL_CHARS = {'(', ')', '[', ']'}


def roman_expression_calculator() -> float:
    expression = get_user_input()
    tokens = tokenize(expression)
    decimal_tokens = convert_tokens(tokens)

    return calculate(decimal_tokens)


def get_user_input() -> str:
    expression = input(INPUT_TEXT).strip().upper()
    if expression == 'HELP':
        print(HELP_TEXT)
        return get_user_input()

    if expression.lower() == 'exit':
        raise SystemExit

    return expression


def validate_roman(roman: str) -> None:
    if not roman:
        raise ValueError(ERROR_EMPTY_INPUT)

    count = 1
    for i in range(1, len(roman)):
        if roman[i] == roman[i - 1]:
            count += 1

            if roman[i] in NON_REPEATABLE:
                raise ValueError(ERROR_NOT_REPEATABLE.format(roman[i]))

            if count > 3:
                raise ValueError(ERROR_MAX_REPETITIONS.format(roman[i]))
        else:
            count = 1

    for i in range(len(roman) - 1):
        current = roman[i]
        nxt = roman[i + 1]

        if ROMAN_VALUES[current] < ROMAN_VALUES[nxt]:
            if current not in VALID_SUBTRACTIONS:
                raise ValueError(ERROR_INVALID_SUBTRACTION_CHAR.format(current))

            if nxt not in VALID_SUBTRACTIONS[current]:
                raise ValueError(ERROR_INVALID_SUBTRACTION.format(f'{current}{nxt}'))

            if i > 0 and roman[i - 1] == current:
                raise ValueError(ERROR_INVALID_SUBTRACTION.format(roman))


def validate_expression(tokens: list[str]) -> None:
    if not tokens:
        raise ValueError(ERROR_EMPTY_INPUT)

    if tokens[0] in OPERATORS:
        raise ValueError(ERROR_EXPRESSION_START_OPERATOR)

    if tokens[-1] in OPERATORS:
        raise ValueError(ERROR_EXPRESSION_END_OPERATOR)

    balance = 0

    for i, token in enumerate(tokens):
        if token == '(':
            balance += 1

        elif token == ')':
            balance -= 1

            if balance < 0:
                raise ValueError(ERROR_INVALID_PARENTHESES)

        elif token == '[':
            j = i + 1

            while j < len(tokens) and tokens[j] != ']':
                if tokens[j] in OPERATORS:
                    raise ValueError(
                        ERROR_EXPRESSION_IN_DECIMAL
                    )
                j += 1

        if i == len(tokens) - 1:
            continue

        current = token
        nxt = tokens[i + 1]

        if current in OPERATORS and nxt in OPERATORS:
            raise ValueError(
                ERROR_INVALID_OPERATOR_SEQUENCE.format(current, nxt)
            )

    if balance != 0:
        raise ValueError(ERROR_INVALID_PARENTHESES)


def tokenize(expression: str) -> list[str]:
    tokens = []
    current = ''

    for char in expression.replace(' ', ''):
        if char in OPERATORS or char in SPECIAL_CHARS:
            if current:
                tokens.append(current)
                current = ''

            tokens.append(char)

        elif char in ROMAN_VALUES:
            current += char

        else:
            raise ValueError(ERROR_INVALID_CHARACTER.format(char))

    if current:
        tokens.append(current)

    validate_expression(tokens)

    return tokens


def convert_tokens(tokens: list[str]) -> list:
    result = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token in OPERATORS or token in {'(', ')'}:
            result.append(token)
            i += 1

        elif i + 2 < len(tokens) and tokens[i + 1] == '[' and tokens[i + 2] == ']':
            result.append(roman_float_to_decimal(tokens[i], ''))
            i += 3

        elif token == '[' and i + 1 < len(tokens) and tokens[i + 1] == ']':
            result.append(0.0)
            i += 2

        elif i + 3 < len(tokens) and tokens[i + 1] == '[' and tokens[i + 3] == ']':
            result.append(roman_float_to_decimal(tokens[i], tokens[i + 2]))
            i += 4

        elif token == '[' and i + 2 < len(tokens) and tokens[i + 2] == ']':
            result.append(roman_float_to_decimal('', tokens[i + 1]))
            i += 3

        else:
            result.append(roman_to_decimal(token))
            i += 1

    return result


def build_expression(tokens: list) -> str:
    expression = ""
    for token in tokens:
        if token == '^':
            expression += '**'

        else:
            expression += str(token)
    return expression


def roman_to_decimal(roman: str) -> int:
    validate_roman(roman)

    total = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and ROMAN_VALUES[roman[i]] < ROMAN_VALUES[roman[i + 1]]:
            total += (ROMAN_VALUES[roman[i + 1]] - ROMAN_VALUES[roman[i]])
            i += 2

        else:
            total += ROMAN_VALUES[roman[i]]
            i += 1

    return total


def roman_float_to_decimal(integer: str, decimal: str) -> float:
    integer_value = roman_to_decimal(integer) if integer else 0
    decimal_value = roman_to_decimal(decimal) if decimal else 0

    return integer_value + (decimal_value / 100)


def calculate(tokens: list) -> float:
    expression = build_expression(tokens)
    return eval(expression)


if __name__ == '__main__':
    while True:
        try:
            result = roman_expression_calculator()
            print(f'Result: {result}')

        except SystemExit:
            break

        except Exception as error:
            print(f'Error: {error}')
