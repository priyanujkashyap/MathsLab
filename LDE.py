#Method 1
from sympy import *
from sympy.abc import x,a 
v=Function('v')(x)
IF=0
p= -cot(x)
q= cot(x)-1
r= exp(x)*sin(x)
if 1+p+q==0:
    IF= exp(x)
elif 1-p+q==0:
    IF= exp(-x)
elif a**2+a*p+q==0:
    IF= exp(a*x)
elif expand(p+q*x)==0:
    IF= x
elif 2+2*p*x+q*x**2==0:
    IF= x**2
if IF:
    print("The integral of CF is =",IF)
    eqn= diff(v,x,2) + (p+(2/IF) + (diff(IF,x,1)))*diff(v,x,1) - (r/IF) 
    sol= dsolve(eqn)
    pprint("y =",sol.rhs*IF)
else:
    print("There is no integral of CF")