from sympy import *
from numpy import *

## Para resolver algunas ecuaciones
x = symbols('x')
y = symbols('y')
ecuacion1 = Eq(2*x-3*y, 0)
ecuacion2 = Eq(13*x+ y, 3)


# despues de definir las ecuaciones
soluciones = solve((ecuacion1, ecuacion2), (x,y))
print(f'{soluciones} estas son las soluciones')