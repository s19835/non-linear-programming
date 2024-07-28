import numpy as np
from scipy.optimize import minimize

# create a objective funcrion
def objective(x):
    return x[0]**2 + 5*x[1]**2 - 4*x[0]*x[1] - 10*x[0] - 4*x[1]

def constraint1(x):
    return 6 - (x[0] + x[1])

def constraint2(x):
    return 18 - (4*x[0] + x[1])

# create constraints
cons1 = {'type': 'ineq', 'fun': constraint1}
cons2 = {'type': 'ineq', 'fun': constraint2}
cons = [cons1, cons2]

# initial values for x
x0 = np.array([0, 0])

# define bounds
b = (0, None)
bounds = [b, b]

solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=cons)
x = solution.x

print(f'\nOptimal solutions: \nx1 = {x[0]}, \r\nx2 = {x[1]}')
print(f'\nOptimal function values: {-solution.fun}')