# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:14:14 2026

@author: peterp
"""

def distance(x):
    a = x * 1.609344        # x = miles
    return a

def temperature(x):
    c = (x - 32) * 5/9      # x = Fahrenheit
    return c

def weight(x):
    b = x * 0.45359327      # x = Pounds
    return b

def main():
    print('\n')
    print('Conversion Program')
    print('--------------------')
    miles = float(input('Enter miles: '))
    km = distance(miles)
    print('Miles: ',miles,' ','kilometers: ',km)
    print('--------------------')
    ft = float(input('Enter Fahrenheit: '))
    cs = temperature(ft)
    print('Fahrenheit: ',ft,' ','Celsius: ',cs)
    print('--------------------')
    pounds = float(input('Enter Pounds: '))
    kg = weight(pounds)
    print('Pound: ',pounds,' ','Kilograms: ',kg)
    print('--------------------')
    print('--done')
    
main()