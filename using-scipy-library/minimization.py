import numpy as np
from scipy.optimize import minimize

def objective(x):
    return x[0]**2 + 2*x[1]**2 + 3*x[2]**2

def constraint1(x):
    return 5*x[0] - x[1] - 3*x[2] - 3

def constraint2(x):
    return 2*x[0] + x[1] + 2*x[2] - 6

# constraints
cons1 = {'type': 'ineq', 'fun': constraint1}
cons2 = {'type': 'ineq', 'fun': constraint2}
cons = [cons1, cons2]

# initial values for x
x0 = np.array([0, 0, 0])

# create bounds
b = (0, None)
bounds = [b, b, b]

solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=cons)
x = solution.x

print(f'\nOptimal values: \nx1 = {x[0]}, \r\nx2 = {x[1]}, \r\nx3 = {x[2]}')
print(f'\nOptimal function: {solution.fun}')