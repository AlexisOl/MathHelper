from scipy import *
from numpy import *
from sympy import *
#imports de las tres clases de opciones para el 
# analisis de datos
x = symbols('x', real = True)
f = sin(x)**4*exp(-5*x)
integrate(f,x)