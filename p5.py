# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:38:53 2026

@author: peterp
"""

print('--Program start')
print('A = add, S = subtract, M = multiple, D = divide')
tcode = input('Select table code: ')
tnumber = float(input('Enter number for table: '))
tnum = tnumber

if tcode == 'A':
    print('Add')
    for tnumber in range(1,11,1):
        print(tnumber+tnum, '=', tnum, '+', tnumber)
elif tcode == 'S':
    for tnumber in range(1,11,1):
        print(tnumber-tnum, '=', tnumber, '-', tnum)
elif tcode == 'M':
    for tnumber in range(1,11,1):
        print(tnumber*tnum, '=', tnumber, '*', tnum)
elif tcode == 'D':
    for tnumber in range(1,11,1):
        print(tnumber/tnum, '=', tnumber, '/', tnum)
print('---done')
