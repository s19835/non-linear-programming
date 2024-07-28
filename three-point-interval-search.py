def f(x):
    return -x**2 - (54/x)

def three_point_interval_search(f, a, b, tol):
    while abs(b - a) > tol:
        # Choose three points
        x1 = a + (b - a) / 4
        x2 = a + (b - a) / 2
        x3 = a + 3 * (b - a) / 4

        # Evaluate function at these points
        f1, f2, f3 = f(x1), f(x2), f(x3)

        # Update interval based on function values
        if f1 < f2 < f3:
            a = x1
        elif f3 < f2:
            b = x3
        else:
            a, b = x2, x3
        
    return (a + b) / 2

# Define the interval
a = 0
b = 5

# Find the optimal solution
solution = three_point_interval_search(f, a, b, 0.1)
print('Maximum point: ', solution)
print('Maximum function value: ', f(solution))