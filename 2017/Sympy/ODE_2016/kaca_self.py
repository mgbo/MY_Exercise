
# -*- coding:utf-8 -*-

from sympy import*

def pprints(func,*funcs):
	pprint(func),
	if funcs is None: return
	for f in funcs:
		pprint(f),
init_printing()

#
#

x = symbols('x')
y = Function('y')(x)
z = symbols('z')

eq = x**4 + y**4 - 2

# Make a differential equation
d_eq = diff(eq,x)
pprint (d_eq)

roots = solve(d_eq, diff(y,x))

dydx = roots[0]
pprints(eq,d_eq,dydx)

dydx1 = dydx.subs(Function('y')(x),z)
slop = dydx1.subs([(x,1),(z,1)])
print 'The slop is ', slop














