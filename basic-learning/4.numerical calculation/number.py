# -*- coding: UTF-8 -*-   
import math


class LinearEquation2(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def lookroot(self):
        temp = math.pow(self.b, 2) - (4*self.a*self.c)
        root1 = (-self.b+math.sqrt(temp))/2*self.a
        root2 = (-self.b-math.sqrt(temp))/2*self.a
        print root1
        print root2

number = raw_input('输入abc三个系数:\n') 
NumbersChar = number.split()
print NumbersChar
NumbersFlo = [0, 0, 0]
i = 0
for g in NumbersChar:
    NumbersFlo[i] = int(g)
    print g
    i += 1
print NumbersFlo
group1 = LinearEquation2(NumbersFlo[0], NumbersFlo[1], NumbersFlo[2])
group1.lookroot()
