import math

def f(x):
    return x**2 - 10 * math.exp(0.1 * x)

def golden_section_search(f, a, b, tol=0.1):
    # Golden ratio
    golden_ratio = (math.sqrt(5) - 1) / 2

    # Initial points
    c = b - golden_ratio * (b - a)
    d = a + golden_ratio * (b - a)

    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c

        # Recomputer the points
        c = b - golden_ratio * (b - a)
        d = a + golden_ratio * (b - a)

    # The optimal solution is the midpoint of the final interval
    return (b + a) / 2

# Define the interval
a = -10
b = 5

# Find the optimal solution
solution = golden_section_search(f, a, b)
print('Minimum value: ', solution)
print('Minimum function value: ', f(solution))