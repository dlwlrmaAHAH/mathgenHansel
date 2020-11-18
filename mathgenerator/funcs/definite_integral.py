from .__init__ import *
import scipy
from scipy.integrate import quad


def definiteIntegralFunc(max_coeff=100):
    def integrand(x, a, b, c):
        return a * x**2 + b * x + c

    a = random.randint(0, max_coeff)
    b = random.randint(0, max_coeff)
    c = random.randint(0, max_coeff)

    lbound = random.randint(-10, 10)
    ubound = random.randint(lbound, 11)

    result = quad(integrand, lbound, ubound, args=(a, b, c))[0]
    S = round(result, 4)

    problem = "The definite integral within limits " + str(lbound) " to " + str(ubound) " of the equation " + \
        str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is = "

    solution = str(S)

    return problem, solution


definite_integral = Generator(
    "Definite Integral of Quadratic Equation", 89,
    "The definite integral within limits M to N of quadratic equation ax^2+bx+c is = ",
    "S", definiteIntegralFunc)
