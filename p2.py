# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:09:58 2026

@author: peterp
"""

print('\n'*3)
recwidth = int(input('Enter the width of the rectangle: '))
recheight = int(input('Enter the height of the rectangle: '))
recarea = recwidth * recheight
print('The area of the rectangle is:', recarea)

tribase = int(input('Enter the base for the triangle: '))
triheight = int(input('Enter the height for the triangle: '))
triarea = int(1 / 2 * tribase * triheight)
print('The area of the triangle is:', triarea)

pi = 3.1459
radius = int(input('Enter the radius of the circle: '))
circlearea = pi * radius ** 2
print('The area of the circle is:', circlearea)

