import sympy
from tabulate import tabulate
import matplotlib.pyplot as plt
sympy.init_printing()
t=sympy.symbols('t',real=True)
s=sympy.symbols('s')
omega = sympy.Symbol('omega',real = True)
#define a constant
a=sympy.symbols('a',real=True,positive=True)
function_list = [sympy.exp(-a*t),sympy.exp(a*t), sympy.sin(omega*t), sympy.cos(omega*t),t,t**2,1]

result = [(sympy.laplace_transform(function,t,s,noconds=True)) for function in function_list]
head = ['Function','Laplace Transformation']
table = [[function,laplace] for function,laplace in zip(function_list,result)]
print('Function List and Their Laplace Transfomation : ')

print(tabulate(table,headers = head, tablefmt = 'grid' ))