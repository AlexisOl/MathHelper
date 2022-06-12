from turtle import *

speed(250)

def generatePolygon(sides, lenght):
    for i in range(0, sides):
        forward(lenght)
        left(360/sides)
    generatePolygon(sides, lenght-1)

generatePolygon(5, 200)