import sympy as sp
import numpy as np
from sympy.matrices import Matrix

a,b,m,e,p,l,g = sp.symbols('a,b,m,e,p,l,g')

#####

det1 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*m)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), -2*a, (2*a + 2*a*m), 2*a],
[0, 2 + m, 0, -2 - m]]
)

d_1_0 = Matrix([[(1 + m)*4*a, e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*m)],
[0, e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[0, -2*a, (2*a + 2*a*m), 2*a],
[0, 2 + m, 0, -2 - m]]
)

d_3_0 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), (1 + m)*4*a, e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*m)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), 0, e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), 0, (2*a + 2*a*m), 2*a],
[0, 0, 0, -2 - m]]
)

f_1_0 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), (1 + m)*4*a, e**(-a*b)*(2*b*a**2*m + 2*m)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), 0, e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), -2*a, 0, 2*a],
[0, 2 + m, 0, -2 - m]]
)

f_3_0 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), (1 + m)*4*a],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), 0],
[(2*a + 2*a*m), -2*a, (2*a + 2*a*m), 0],
[0, 2 + m, 0, 0]]
)

#####

det2 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*a)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), -2*a, (2*a + 2*a*m), 2*a],
[0, 2 + m, 0, -2 - m]]
)

d_2_0 = Matrix([[0, e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*a)],
[(1 + m)*4*a, e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[0, -2*a, (2*a + 2*a*m), 2*a],
[0, 2 + m, 0, -2 - m]]
)

d_4_0 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), 0, e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*a)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), (1 + m)*4*a, e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), 0, (2*a + 2*a*m), 2*a],
[0, 0, 0, -2 - m]]
)

f_2_0 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), 0, e**(-a*b)*(2*b*a**2*m + 2*a)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), (1 + m)*4*a, e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), -2*a, 0, 2*a],
[0, 2 + m, 0, -2 - m]]
)

f_4_0 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), 0],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), (1 + m)*4*a],
[(2*a + 2*a*m), -2*a, (2*a + 2*a*m), 0],
[0, 2 + m, 0, 0]]
)

#####

det3 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*a)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), -2*a, (2*a + 2*a*m), 2*a],
[0, 2 + m, 0, -2 - m]]
)

d_1_1 = Matrix([[0, e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*a)],
[0, e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(1 + m)*4*a, -2*a, (2*a + 2*a*m), 2*a],
[0, 2 + m, 0, -2 - m]]
)

d_3_1 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), 0, e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*a)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), 0, e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), (1 + m)*4*a, (2*a + 2*a*m), 2*a],
[0, 0, 0, -2 - m]]
)

f_1_1 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), 0, e**(-a*b)*(2*b*a**2*m + 2*a)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), 0, e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), -2*a, (1 + m)*4*a, 2*a],
[0, 2 + m, 0, -2 - m]]
)

f_3_1 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), 0],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), 0],
[(2*a + 2*a*m), -2*a, (2*a + 2*a*m), (1 + m)*4*a],
[0, 2 + m, 0, 0]]
) 

#####

det4 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*a)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), -2*a, (2*a + 2*a*m), 2*a],
[0, 2 + m, 0, -2 - m]]
)

d_2_1 = Matrix([[0, e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*a)],
[0, e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[0, -2*a, (2*a + 2*a*m), 2*a],
[(1 + m)*4*a, 2 + m, 0, -2 - m]]
)

d_4_1 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), 0, e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), e**(-a*b)*(2*b*a**2*m + 2*a)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), 0, e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), 0, (2*a + 2*a*m), 2*a],
[0, (1 + m)*4*a, 0, -2 - m]]
)

f_2_1 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), 0, e**(-a*b)*(2*b*a**2*m + 2*a)],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), 0, e**(-a*b)*(2*g*b*a**2*m + 4*g*a + 2*a*l)],
[(2*a + 2*a*m), -2*a, 0, 2*a],
[0, 2 + m, (1 + m)*4*a, -2 - m]]
) 

f_4_1 = Matrix([[e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m), e**(a*b)*(2*b*a**2*m - 2*a), e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m), 0],
[e**(a*b)*(-2*g*b*a**2*m - 2*g*a*m + 2*a*l), e**(a*b)*(-2*g*b*a**2*m + 4*g*a + 2*a*l), e**(-a*b)*(-2*g*b*a**2*m + 2*g*a*m - 2*a*l), 0],
[(2*a + 2*a*m), -2*a, (2*a + 2*a*m), 0],
[0, 2 + m, 0, (1 + m)*4*a]]
)

#print(d_1_1.det())

######
# U_0[psi_1] matrix element 1
expr1 = e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m)
expr2 = e**(a*b)*(2*b*a**2*m - 2*a)
expr3 = e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m)
expr4 = e**(-a*b)*(2*b*a**2*m + 2*a)

res = d_1_1.det() * expr1 + d_3_1.det() * expr2 + f_1_1.det() * expr3 + f_3_1.det() * expr4
print(sp.expand(res))

# U_0[psi_1] matrix element 2
expr1 = e**(a*b)*(2*b*a**2*m + 2*a + 2*a*m)
expr2 = e**(a*b)*(2*b*a**2*m - 2*a)
expr3 = e**(-a*b)*(-2*b*a**2*m + 2*a + 2*a*m)
expr4 = e**(-a*b)*(2*b*a**2*m + 2*a)

res = d_2_1.det() * expr1 + d_4_1.det() * expr2 + f_2_1.det() * expr3 + f_4_1.det() * expr4
print(sp.expand(res))

# U_0[psi_1] matrix element 3
expr1 = e**(a*b)*(-2*b*a**2*m*g - 2*a*m*g + 2*a*l)
expr2 = e**(a*b)*(-2*b*a**2*m*g + 4*a*g + 2*a*l)
expr3 = e**(-a*b)*(-2*b*a**2*m*g + 2*a*m*g - 2*a*l)
expr4 = e**(-a*b)*(2*b*a**2*m*g + 4*a*g + 2*a*l)

res = d_1_1.det() * expr1 + d_3_1.det() * expr2 + f_1_1.det() * expr3 + f_3_1.det() * expr4
print(sp.expand(res))

# U_0[psi_1] matrix element 4
expr1 = e**(a*b)*(-2*b*a**2*m*g - 2*a*m*g + 2*a*l)
expr2 = e**(a*b)*(-2*b*a**2*m*g + 4*a*g + 2*a*l)
expr3 = e**(-a*b)*(-2*b*a**2*m*g + 2*a*m*g - 2*a*l)
expr4 = e**(-a*b)*(2*b*a**2*m*g + 4*a*g + 2*a*l)

res = d_2_1.det() * expr1 + d_4_1.det() * expr2 + f_2_1.det() * expr3 + f_4_1.det() * expr4
print(sp.expand(res))

######
# U_1[psi_0] matrix element 1
expr1 = (2*a + 2*a*m)
expr2 = (-2*a)
expr3 = (2*a + 2*a*m)
expr4 = (2*a)

res = d_1_0.det() * expr1 + d_3_0.det() * expr2 + f_1_0.det() * expr3 + f_3_0.det() * expr4
print(sp.expand(res))

# U_1[psi_0] matrix element 2
expr1 = (2*a + 2*a*m)
expr2 = (-2*a)
expr3 = (2*a + 2*a*m)
expr4 = (2*a)

res = d_2_0.det() * expr1 + d_4_0.det() * expr2 + f_2_0.det() * expr3 + f_4_0.det() * expr4
print(sp.expand(res))

# U_1[psi_0] matrix element 3
expr1 = 0
expr2 = (2 + m)
expr3 = 0
expr4 = (-2 - m)

res = d_1_0.det() * expr1 + d_3_0.det() * expr2 + f_1_0.det() * expr3 + f_3_0.det() * expr4
print(sp.expand(res))

# U_1[psi_0] matrix element 4
expr1 = 0
expr2 = (2 + m)
expr3 = 0
expr4 = (-2 - m)

res = d_2_0.det() * expr1 + d_4_0.det() * expr2 + f_2_0.det() * expr3 + f_4_0.det() * expr4
print(sp.expand(res))



