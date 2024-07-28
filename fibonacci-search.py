
def f(x):
    return -2*x**2 + 4*x
    
def fibonacci(n):
    if n <= 0:
        return 'input should be a positive number'
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

def fibonacci_search(f, a, b, n, tol=0.1):
    k = n

    while abs(b - a) / 2 > tol:
        c = a + (fibonacci(k - 2) / fibonacci(k)) * (b - a)
        d = b - (fibonacci(k - 2) / fibonacci(k)) * (b - a)
        
        if (f(c) < f(d)):
            a = c
        else:
            b = d
        
    return (b + a) / 2

# Define the interval
a, b = 0, 1.5

# Find the optimal solution
solution = fibonacci_search(f, a, b, 10)
print('Optimal solution: ', solution)
print('Optimal function value: ', f(solution))