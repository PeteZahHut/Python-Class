# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:10:48 2026

@author: peterp
"""

pounds_amount = float(input("Enter the number of pounds to be purchased: "))
if pounds_amount>0:
    price = 0.99
    gross_sales = pounds_amount * price
    
    if (pounds_amount<=99.99) and (pounds_amount>=10):
            discount_percent = 0.1
    elif (pounds_amount<=999.99) and (pounds_amount>=100):
            discount_percent = 0.2
    elif (pounds_amount<=9999.99) and (pounds_amount>=1000):
        discount_percent = 0.3   
    elif (pounds_amount>=10000):
            discount_percent = 0.4
    else:
        discount_percent = 0    
    
    print('Number of pounds:',pounds_amount)
    print('Gross sales: ',gross_sales)
    discount_amount = gross_sales * discount_percent
    print('Discount: ',discount_amount)
    final_amount = gross_sales - discount_amount
    print('Final Amount: ',final_amount)
else:
    print('Pounds cannot be zero or negative')
