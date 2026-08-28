# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 20:01:56 2026

@author: Peter P
"""

print('\n'*20)
Fname = input('Enter first name: ')
Lname = input('Enter last name: ')

frstnlastname = (Fname + ' ' + Lname)

Addy = input('Enter address: ')
Cityname = input('Enter city: ')
Statename = input('Enter state: ')
Postalcode = input('Enter postal code: ')

citystnpostal = (Cityname + ',' + ' ' + Statename + ' ' + Postalcode)

print(frstnlastname)
print(Addy)
print(citystnpostal)
