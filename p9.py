# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:05:31 2026

@author: peterp
"""

def a2h():
    try:
        a = float(input('Enter acres: '))
        h = a * 0.4047
        if (a > 0):
            print(a, 'converts to', h, 'hectares')
            print('----------')
    except:
            print('Input error - acres')
            print('----------')
            
        

def q2l():
    try:
        q = float(input('Enter quarts: '))
        l = q * 0.946353
        if (q > 0):
            print(q, 'converts to', l, ('liters'))
            print('----------')
    except:
            print('Input error - quarts')
            print('----------')

def f2k():
    try:
        f = float(input('Enter Fahrenheit: '))
        k = (f-32)*(5/9) + 273.15
        print(f, 'converts to', k, 'Kelvins')
        print('----------')
    except: 
            print('Input error - fahrenheit')
            print('----------')
ans = 'y'
while (ans == 'y') or (ans == "Y"):
    a2h()
    q2l()
    f2k()
    ans = input('again y/n? ')
print('done')
   
        