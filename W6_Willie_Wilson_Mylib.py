"""
Wk3_Willie_wilson.py,
Willie Wilson,
ENTD220,
Professor Maxim Titley,
10/12/2024
"""


def add(x, y):

    return x + y

def subtract(x, y):

    return x - y

def multiply(x, y):

    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Error! Division by zero.")

def is_in_range(number, range_start, range_end):
    if range_start > range_end:
        raise ValueError("Range start must be less than or equal to range end.")
    return range_start <= number <= range_end

def scalc(p1):
    try:
        parts = p1.replace(" ", "").split(",")
        if len(parts) != 3:
            return "Invalid input format"

        N1 = float(parts[0])
        N2 = float(parts[1])
        operator = parts[2]

        if operator == '+':
            return add(N1, N2)
        elif operator == '-':
            return subtract(N1, N2)
        elif operator == '*':
            return multiply(N1, N2)
        elif operator == '/':
            return divide(N1, N2)
        else:
            return "Invalid operator"
    except ValueError:
        return "Invalid input format"

def allInOne(n1, n2):
        results = {
        'addition': add ( n1, n2 ),
        'subtraction': subtract ( n1, n2 ),
        'multiplication': multiply ( n1, n2 ),
        'division': divide ( n1, n2 ) if n2 != 0 else 'Error! Division by zero.'
        }
        return results


