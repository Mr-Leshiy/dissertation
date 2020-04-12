import sympy as sp
import numpy as np
from sympy.matrices import Matrix

a,b,m,e,p,l,g = sp.symbols('a,b,m,e,p,l,g')

M = Matrix([[2*a+2*a*m, a*m, 2*a+2*a*m, -a*m],
[0, 2+m, 0, -2-m],
[e**(a*b)*(b*a*a*m+2*a+2*a*m), e**(a*b)*(b*a*a*m+a*m), e**(-a*b)*(-b*a*a*m+2*a+2*a*m), e**(-a*b)*(b*a*a*m-a*m)],
[e**(a*b)*(-b*a*m), e**(a*b)*(2-b*a*m+m), e**(-a*b)*(b*a*m), e**(-a*b)*(-b*a*m-2-m)]])

C1 = Matrix([[0, a*m, 2*a+2*a*m, -a*m],
[0, 2+m, 0, -2-m],
[-p*a*a*4*(1+m), e**(a*b)*(b*a*a*m+a*m), e**(-a*b)*(-b*a*a*m+2*a+2*a*m), e**(-a*b)*(b*a*a*m-a*m)],
[-p*a*4*(1+m), e**(a*b)*(2-b*a*m+m), e**(-a*b)*(b*a*m), e**(-a*b)*(-b*a*m-2-m)]])

C2 = Matrix([[2*a+2*a*m, 0, 2*a+2*a*m, -a*m],
[0, 0, 0, -2-m],
[e**(a*b)*(b*a*a*m+2*a+2*a*m), -p*a*a*4*(1+m), e**(-a*b)*(-b*a*a*m+2*a+2*a*m), e**(-a*b)*(b*a*a*m-a*m)],
[e**(a*b)*(-b*a*m), -p*a*4*(1+m), e**(-a*b)*(b*a*m), e**(-a*b)*(-b*a*m-2-m)]])

C3 = Matrix([[2*a+2*a*m, a*m, 0, -a*m],
[0, 2+m, 0, -2-m],
[e**(a*b)*(b*a*a*m+2*a+2*a*m), e**(a*b)*(b*a*a*m+a*m), -p*a*a*4*(1+m), e**(-a*b)*(b*a*a*m-a*m)],
[e**(a*b)*(-b*a*m), e**(a*b)*(2-b*a*m+m), -p*a*4*(1+m), e**(-a*b)*(-b*a*m-2-m)]])

C4 = Matrix([[2*a+2*a*m, a*m, 2*a+2*a*m, 0],
[0, 2+m, 0, 0],
[e**(a*b)*(b*a*a*m+2*a+2*a*m), e**(a*b)*(b*a*a*m+a*m), e**(-a*b)*(-b*a*a*m+2*a+2*a*m), -p*a*a*4*(1+m)],
[e**(a*b)*(-b*a*m), e**(a*b)*(2-b*a*m+m), e**(-a*b)*(b*a*m), -p*a*4*(1+m)]])


SIGMA_M = Matrix([[e**(a*b)*(2*b*a*a*m + 2*a + 2*a*m), e**(a*b)*(2*b*a*a*m - 2*a), e**(-a*b)*(-2*b*a*a*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a*a*m + 2*a)],
[e**(a*b)*(-2*g*b*a*a*m - 2*g*a*m + 2*l*a), e**(a*b)*(-2*g*b*a*a*m + (2*g + l)*2*a), e**(-a*b)*(-2*g*b*a*a*m + 2*g*a*m -2*l*a), e**(-a*b)*(2*g*b*a*a*m + (2*g + l)*2*a)],
[2*a+2*a*m, -2*a, 2*a+2*a*m, 2*a],
[0, 2+m, 0, -2-m]])

SIGMA_C1 = Matrix([[0, e**(a*b)*(2*b*a*a*m - 2*a), e**(-a*b)*(-2*b*a*a*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a*a*m + 2*a)],
[-p*a*4*(1+m), e**(a*b)*(-2*g*b*a*a*m + (2*g + l)*2*a), e**(-a*b)*(-2*g*b*a*a*m + 2*g*a*m -2*l*a), e**(-a*b)*(2*g*b*a*a*m + (2*g + l)*2*a)],
[0, -2*a, 2*a+2*a*m, 2*a],
[0, 2+m, 0, -2-m]])

SIGMA_C2 = Matrix([[e**(a*b)*(2*b*a*a*m + 2*a + 2*a*m), 0, e**(-a*b)*(-2*b*a*a*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a*a*m + 2*a)],
[e**(a*b)*(-2*g*b*a*a*m - 2*g*a*m + 2*l*a), -p*a*4*(1+m), e**(-a*b)*(-2*g*b*a*a*m + 2*g*a*m -2*l*a), e**(-a*b)*(2*g*b*a*a*m + (2*g + l)*2*a)],
[2*a+2*a*m, 0, 2*a+2*a*m, 2*a],
[0, 0, 0, -2-m]])

SIGMA_C3 = Matrix([[e**(a*b)*(2*b*a*a*m + 2*a + 2*a*m), e**(a*b)*(2*b*a*a*m - 2*a), 0, e**(-a*b)*(2*b*a*a*m + 2*a)],
[e**(a*b)*(-2*g*b*a*a*m - 2*g*a*m + 2*l*a), e**(a*b)*(-2*g*b*a*a*m + (2*g + l)*2*a), -p*a*4*(1+m), e**(-a*b)*(2*g*b*a*a*m + (2*g + l)*2*a)],
[2*a+2*a*m, -2*a, 0, 2*a],
[0, 2+m, 0, -2-m]])

SIGMA_C4 = Matrix([[e**(a*b)*(2*b*a*a*m + 2*a + 2*a*m), e**(a*b)*(2*b*a*a*m - 2*a), e**(-a*b)*(-2*b*a*a*m + 2*a + 2*a*m), 0],
[e**(a*b)*(-2*g*b*a*a*m - 2*g*a*m + 2*l*a), e**(a*b)*(-2*g*b*a*a*m + (2*g + l)*2*a), e**(-a*b)*(-2*g*b*a*a*m + 2*g*a*m -2*l*a), -p*a*4*(1+m)],
[2*a+2*a*m, -2*a, 2*a+2*a*m, 0],
[0, 2+m, 0, 0]])

c1 = SIGMA_C1.det() / SIGMA_M.det()
c2 = SIGMA_C2.det() / SIGMA_M.det()
c3 = SIGMA_C3.det() / SIGMA_M.det()
c4 = SIGMA_C4.det() / SIGMA_M.det()

print(SIGMA_C4.det())