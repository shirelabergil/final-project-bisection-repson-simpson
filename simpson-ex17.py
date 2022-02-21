import math
import sympy as sym
import numpy as np
from datetime import datetime
now = datetime.now()
add = '00000' + str(now.day) + str(now.hour) + str(now.minute)
def simps(f,a,b,N=50):
    '''
    Approximate the integral of f(x) from a to b by Simpson's rule.

    Simpson's rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/3) \sum_{k=1}^{N/2} (f(x_{2i-2} + 4f(x_{2i-1}) + f(x_{2i}))
    where x_i = a + i*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : (even) integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using
        Simpson's rule with N subintervals of equal length.
    '''
    print("\n*** SIMPSON METHOD ***\n")
    print(f'N = {N}')
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    for i in range(len(y)):
        print(f'i = {i} , x = {x[i]} , f(x) = {y[i]}')
    print('\n')
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


f = lambda x: x * float(math.e)**(-1*x**2+5*x) * (2*x**2 - 3*x - 5)

print(f'FINAL RESULT : {str(simps(f, 0.5, 1, 10)) + add}\n')

x = sym.Symbol('x')
f = x * float(math.e)**(-1*x**2+5*x) * (2*x**2 - 3*x - 5)
derivative_f = (((f.diff(x)).diff(x)).diff(x)).diff(x)
error = 1/90*((1-0.5)/2)**5*derivative_f.subs(x, 1)
print(f'ESTIMATED ERROR : {str(error) + add}\n')

