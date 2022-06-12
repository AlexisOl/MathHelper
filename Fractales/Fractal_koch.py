from turtle import *

shape("turtle")
speed(0)

def kohr(lenght, level):
    if level ==0:
        forward(lenght)
        return

    lenght /= 3.0
    kohr(lenght, level-1)
    left(60)
    kohr(lenght, level-1)
    right(120)
    kohr(lenght, level-1)
    left(60)
    kohr(lenght, level-1)

def createKohr(side, lenght):
    for _ in range(side):
        kohr(lenght, side)
        right(360/side)

createKohr(4,300)
mainloop()