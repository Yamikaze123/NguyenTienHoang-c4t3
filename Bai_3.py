from math import *

def trigonometry (x):
    y = []
    z = []

    for i in range(len(x)):
        y.append(round(pi/2 - x[i], 1))
        z.append(round(cos(radians(x[i])), 1) - round(sin(radians(x[i])), 1))

    return y, z
