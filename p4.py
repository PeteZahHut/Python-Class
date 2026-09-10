# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:50:02 2026

@author: peterp
"""

print('\n'*3)
Name = input('Please enter your name: ')

nd = len(Name)

if nd == 0:
    print('Name cannot be blank')
elif Name.isspace():
    print('Name cannot be blank')
elif nd < 3:
    print('Name too short')
elif (Name.isalpha()):
    print('valid')
else:
    print('Name must be alphabetic')

accnum = input('Please enter your account name: ')

ad = len(accnum)

if ad == 0:
    print('Account number cannot be blank')
elif accnum.isspace():
    print('Account number cannot be blank')
elif (accnum.isalpha()):
    print('Account number must be numeric')
elif ad < 9 and ad > 0:
    print('Account number must be 9 digits')
else:
    print('valid')
    
paymentamount = input('Please enter your payment amount: ')

if paymentamount.isspace():
    print('Payment cannot be blank')
else:
    if len(paymentamount)==0:
        print('Payment cannot be blank')
    else:
        

        pamt=float(paymentamount)
            

        if pamt == 0:
            print('Payment cannot be zero')
        elif pamt < 0:
            print('Payment cannot be negative')
        else:
            print('valid')
    