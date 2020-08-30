
from sympy import Function, Symbol, dsolve
from sympy import init_printing

f = Function('f')
x = Symbol('x')

fun = f(x).diff(x,x)+f(x)

print ("fun : ")
print (fun)

sol = dsolve(f(x).diff(x,x)+f(x),f(x))

print ("ans")
print (sol)
