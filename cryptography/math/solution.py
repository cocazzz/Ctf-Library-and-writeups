#decryption_function
from sympy.solvers import solve
from sympy import Symbol

#sympy is a math library in python used to solve equations
# x**3+(x+1)*(x+2)= x**3 + x**2 + 3*x +2

def decrypt(cipher) :
	S=""
	x = Symbol('x')
	for i in cipher :
		S=S+chr(int(solve(x**3 + x**2 + 3*x +2 - i, x)[0]))
	print (S)
