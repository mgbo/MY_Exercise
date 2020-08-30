
# -*- coding:utf-8 -*-

from sympy import*
x = Symbol('x')
y = Symbol('y')

ans = x+y+x-y
print (ans)

# пример expand
ans1 = expand((x+y)**2)
pprint (ans1)

# пример simplify
eq = simplify((x+x*y)/x)
print eq

# пример  solve
res = solve([x + 5*y -2 ,-3*x + 6*y - 15],[x,y])
print res

# пример Differential Equation
f = Function('f')
eq = f(x).diff(x,x) + f(x)
pprint (eq)
res1 = dsolve(f(x).diff(x,x) + f(x),f(x))
pprint (res1)

res2 = res1.rhs
print res2

pprint(Integral(x**2,x),use_unicode=True)

pprint(integrate(x**2,x))

pprint (Derivative(x**3,x))

# подстановки

t = symbols ('t')
x = Function ('x')

f_1 = diff(x(t),t) + x(t)
pprint (f_1)

print "--------"
f_2 = f_1.replace(x,sin)
pprint (f_2)

f_f = dsolve(diff(x(t),t) + x(t),x(t))
pprint (f_f)

f_3 = f_1.replace(x,sin).doit() #solve
pprint (f_3)
