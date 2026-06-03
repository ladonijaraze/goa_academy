def sum_factorial(lst):
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    return sum(factorial(n) for n in lst)


from math import sqrt

def area(diagonal, side):
    if diagonal <= side:
        return "Not a rectangle"
    return side * sqrt(diagonal**2 - side**2)