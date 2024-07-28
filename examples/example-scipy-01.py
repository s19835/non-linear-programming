import numpy as np
from scipy.optimize import minimize

def objective(x):
    return -(x[0]*(300 - x[0]) + x[1]*(500 - 2*x[1]) - (30*x[0] + 50*x[1]) - 100*(x[0] + x[1]))

def constraint(x):
    return -x[0] - x[1] + 17.25

x0 = np.array([0, 0])

b = (0, None)
bounds = [b, b]

con = {'type': 'ineq', 'fun': constraint}
cons = [con]

solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=cons)
x = solution.x
print(f'\nOptimal solutions:\n x1 = {x[0]}\n x2 = {x[1]}')
print(f'\nOptimum function value: {-solution.fun}')