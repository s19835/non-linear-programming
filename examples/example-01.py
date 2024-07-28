import math

# x**2 - 10*exp(0.1x) -- minimize, x = 0.36474508437578823, function value = -10.238439675035924
def f(x):
    return x**2 - 10*math.exp(0.1*x)

# Interval
a, b = -10, 5

# MT 316 - Non-Linear Programming Chapter 5: Single Variable Optimization
print('\n')
print('MT 316 - Non-Linear Programming\r\nChapter 5: Single Variable Optimization')
print('\n')


# golden section search method
def golden_section_search(f, a, b, tol=0.1):
    golden_ratio = (math.sqrt(5) - 1) / 2

    while abs(b - a) > tol:
        c = b - golden_ratio * (b - a)
        d = a + golden_ratio * (b - a)
        if (f(c) < f(d)):
            b = d
        else :
            a = c
    return (a + b) / 2

minimum_point1 = golden_section_search(f, a, b)
print('# golden section search method')
print('Minimum Point: ', minimum_point1) 
print('Minimum value of function: ', f(minimum_point1))
print('\n')

# fibonacci search method
def fibonacci(n):
    if n <= 0:
        return 'input should a positive value'
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

def fibonacci_search(f, a, b, n, tol=0.1):
    k = n

    while abs(b - a) / 2 > tol:
        c = a + (fibonacci(k - 2)/ fibonacci(k)) * (b - a)
        d = b - (fibonacci(k - 2)/ fibonacci(k)) * (b - a)

        if (f(c) < f(d)):
            b = d
        else:
            a = c
    
    return (a + b) / 2

minimum_point2 = fibonacci_search(f, a, b, 10)
print('# fibonacci search method')
print('Minimum Point: ', minimum_point2) 
print('Minimum value of function: ', f(minimum_point2))
print('\n')

# three point interval search method
def three_point_interval_search(f, a, b, tol=0.1):
    while abs(b - a) > tol:
        x1 = a + (b - a) / 4
        x2 = a + (b - a) / 2
        x3 = a + 3 * (b - a) / 4

        if f(x1) < f(x2) < f(x3):
            b = x3
        elif f(x3) < f(x2):
            a = x1
        else:
            a, b = x2, x3
    
    return (a + b) / 2

minimum_point3 = three_point_interval_search(f, a, b)
print('# three point interval search method')
print('Minimum Point: ', minimum_point3) 
print('Minimum value of function: ', f(minimum_point3))
print('\n')