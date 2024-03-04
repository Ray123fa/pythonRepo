from sympy import symbols, Eq, solve
from math import log, sqrt, isqrt
from fractions import Fraction
import re

def addition(first, second):
    result = first + second

    if str(first)[-2:] == ".0":
        first = int(first)
    if str(second)[-2:] == ".0":
        second = int(second)

    if str(result)[-2:] == ".0":
        result = int(result)

        print(f"Hasil dari {first} + {second} adalah {result}")
    else:
        print(f"Hasil dari {first} + {second} adalah {result}")

def substraction(first, second):
    result = first - second

    if str(first)[-2:] == ".0":
        first = int(first)
    if str(second)[-2:] == ".0":
        second = int(second)

    if str(result)[-2:] == ".0":
        result = int(result)

        print(f"Hasil dari {first} - {second} adalah {result}")
    else:
        print(f"Hasil dari {first} - {second} adalah {result}")

def multiplication(first, second):
    result = first * second

    if str(first)[-2:] == ".0":
        first = int(first)
    if str(second)[-2:] == ".0":
        second = int(second)

    if str(result)[-2:] == ".0":
        result = int(result)

        print(f"Hasil dari {first} × {second} adalah {result}")
    else:
        print(f"Hasil dari {first} × {second} adalah {result}")

def division(first, second):
    result = first / second

    if str(first)[-2:] == ".0":
        first = int(first)
    if str(second)[-2:] == ".0":
        second = int(second)

    if str(result)[-2:] == ".0":
        result = int(result)

        print(f"Hasil dari {first} : {second} adalah {result}")
    else:
        print(f"Hasil dari {first} : {second} adalah {result}")

def powered(first, second):
    result = first ** second

    if str(first)[-2:] == ".0":
        first = int(first)
    if str(second)[-2:] == ".0":
        second = int(second)

    if str(result)[-2:] == ".0":
        result = int(result)

        print(f"Hasil dari {first}^{second} adalah {result}")
    else:
        print(f"Hasil dari {first}^{second} adalah {result}")

def mod(first, second):
    result = first % second

    if str(first)[-2:] == ".0":
        first = int(first)
    if str(second)[-2:] == ".0":
        second = int(second)

    if str(result)[-2:] == ".0":
        result = int(result)

        print(f"Hasil dari {first} mod {second} adalah {result}")
    else:
        print(f"Hasil dari {first} mod {second} adalah {result}")

def logarithm(basis, numerus):
    result = log(numerus, basis)

    if str(basis)[-2:] == ".0":
        basis = int(basis)
    if str(numerus)[-2:] == ".0":
        numerus = int(numerus)

    if str(result)[-2:] == ".0":
        result = int(result)

        print(f"Hasil dari ^{basis} log({numerus}) adalah {result}")
    else:
        result = round(result, 5)
        print(
            f"Hasil aproksimasi dari ^{basis} log({numerus}) adalah {result}")

def quadratic_eq(a, b, c):
    x = symbols("x")

    y = a*x**2 + (b*x) + (c)
    y = Eq(y, 0)  # persamaan y memiliki hasil 0
    # fungsi untuk menyelesaikan persamaan y dan mencari nilai x
    result = solve(y, x)

    D = b**2 - 4*a*c  # diskriminan
    if D < 0:
        min_b = round(float(-1*b), 3)
        D = round(float(D), 3)
        a2 = round(float(2*a), 3)

        if str(min_b)[-2:] == ".0":
            min_b = int(min_b)
        if str(D)[-2:] == ".0":
            D = int(D)
        if str(a2)[-2:] == ".0":
            a2 = int(a2)

        x1 = f"({min_b} + √({D}))/({a2})"
        x2 = f"({min_b} - √({D}))/({a2})"
        print(
            f"\nAkar-akar dari persamaan yang anda input adalah:\n{x1} dan {x2}")
    elif D == 0:
        x = round(float(result[0]), 3)
        if str(x)[-2:] == ".0":
            x = int(x)
        print(
            f"\nAkar-akar dari persamaan yang anda input adalah:\n{x} dan {x}")
    elif (D == int(D)) and (D > 0):
        D = int(D)
        if sqrt(D) == isqrt(D):
            x1 = result[0]
            x2 = result[1]
            print(
                f"\nAkar-akar dari persamaan yang anda input adalah:\n{x1} dan {x2}")
        elif sqrt(D) != isqrt(D):
            x1 = f"({-1*b} + √{D})/({2*a})"
            x2 = f"({-1*b} - √{D})/({2*a})"
            print(
                f"\nAkar-akar dari persamaan yang anda input adalah:\n{x1} dan {x2}")
    elif (D > 0) and re.findall("/", str(result)):
        x1 = float(result[0])
        x1 = round(x1, 3)
        x2 = float(result[1])
        x2 = round(x2, 3)

        if str(x1)[-2:] == ".0":
            x1 = int(x1)
        if str(x2)[-2:] == ".0":
            x2 = int(x2)
        print(
            f"\nAkar-akar dari persamaan yang anda input adalah:\n{x1} dan {x2}")