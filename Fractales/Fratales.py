import matplotlib.pyplot as plt
from math import sqrt
from random import randint 


def medio(first, second):
    x = (first[0]+ second[0])/2
    y = (first[1]+second[1])/2
    return(x,y)


def addPoint(cantidad):
    global puntos
    for i in range(cantidad):
        valores = randint(0, 2)
        nuevo = medio(puntos[valores], puntos[-1])
        puntos.append(nuevo)

if __name__ == '__main__':
    puntos = [(0,0), (1,0), (1/2, sqrt(3)/2)]
    fig, ax = plt.subplots()
    addPoint(10**6)
    ax.scatter([x[0] for x in puntos], [y[1] for y in puntos], 
    s=0.00001, color= "red")
    ax.set_axis_off()
    plt.show()