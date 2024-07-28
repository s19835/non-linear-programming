import math

def f(x):
    return -2*x**2 + 4*x # Maximization

# intervals
a, b = 0, 1.5
tol = 0.1

# MT 316 - Non-Linear Programming Chapter 5: Single Variable Optimization
print('\n')
print('MT 316 - Non-Linear Programming\r\nChapter 5: Single Variable Optimization')
print('\n')

# golden section search method
def golden_section_search(f, a, b, tol):
    golden_ratio = (math.sqrt(5) - 1) / 2
    while abs(b - a) > tol:
        c = b - golden_ratio * (b - a)
        d = a + golden_ratio * (b - a)

        if f(c) < f(d):
            a = c
        else:
            b = d
    
    return (a + b) / 2

maximum_value1 = golden_section_search(f, a, b, tol)
print('# golden section search method')
print('maximum value: ', maximum_value1)
print('maximum function value: ', f(maximum_value1))
print('\n')

# fibonacci search method
def fib(n):
    if n <= 0:
        raise ValueError('input should be a positive value')
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

def fibonacci_search(f, a, b, n, tol):
    k = n
    while abs(b - a) / 2 > tol:
        c = a + (fib(k - 2) / fib(k)) * (b - a)
        d = b - (fib(k-2) / fib(k)) * (b - a)

        if f(c) < f(d):
            a = c
        else:
            b = d
    return (a + b) / 2

maximum_value2 = fibonacci_search(f, a, b, 10, tol)
print('# fibonacci search method')
print('maximum value: ', maximum_value2)
print('maximum function value: ', f(maximum_value2))
print('\n')

# three-point search method
def three_point_search(f, a, b, tol):
    while abs(b - a) > tol:
        x1 = a + (b - a) / 4
        x2 = a + (b - a) / 2
        x3 = a + 3 * (b - a) / 4

        f1, f2, f3 = f(x1), f(x2), f(x3)

        if f1 < f2 < f3:
            a = x1
        elif f3 < f2:
            b = x3
        else:
            a, b = x2, x3
    
    return (a + b) / 2

maximum_value3 = three_point_search(f, a, b, tol)
print('# three-point search method')
print('maximum value: ', maximum_value3)
print('maximum function value: ', f(maximum_value3))