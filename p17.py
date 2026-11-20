# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:46:18 2026

@author: wrl123u
"""

def powerball():
    print('\n')
    
    pb = []
    while len(pb) < 5:
           a = random.randint(1,69)
           if a not in pb:
               pb.append(a)
    pb.sort()
    print('powerball ',pb)
    
def megamilly():
    print('\n')
    mmnum1 = random.randint(1,70)
    mmnum2 = random.randint(1,70)
    mmnum3 = random.randint(1,70)
    mmnum4 = random.randint(1,70)
    mmnum5 = random.randint(1,70)
    
    while (mmnum1 == mmnum2) or (mmnum1 == mmnum3) or (mmnum1 == mmnum4) or (mmnum1 == mmnum5):
        mmnum1 = random.randint(1,70)
    while (mmnum2 == mmnum1) or (mmnum2 == mmnum3) or (mmnum2 == mmnum4) or (mmnum2 == mmnum5):
        mmnum2 = random.randint(1,70)
    while (mmnum3 == mmnum1) or (mmnum3 == mmnum2) or (mmnum3 == mmnum4) or (mmnum3 == mmnum5):
        mmnum3 = random.randint(1,70)
    while (mmnum4 == mmnum1) or (mmnum4 == mmnum2) or (mmnum4 == mmnum3) or (mmnum4 == mmnum5):
        mmnum4 = random.randint(1,70)
    while (mmnum5 == mmnum1) or (mmnum5 == mmnum2) or (mmnum5 == mmnum3) or (mmnum5 == mmnum4):
        mmnum5 = random.randint(1,70)
    
    mmlist = [mmnum1,mmnum2,mmnum3,mmnum4,mmnum5]
    mmlist.sort()
    
    print(mmlist)
        
def luckyday():
    print('\n')
    ldnum1 = random.randint(1,45)
    ldnum2 = random.randint(1,45)
    ldnum3 = random.randint(1,45)
    ldnum4 = random.randint(1,45)
    ldnum5 = random.randint(1,45)
    
    while (ldnum1 == ldnum2) or (ldnum1 == ldnum3) or (ldnum1 == ldnum4) or (ldnum1 == ldnum5):
        ldnum1 = random.randint(1,45)
    while (ldnum2 == ldnum1) or (ldnum2 == ldnum3) or (ldnum2 == ldnum4) or (ldnum2 == ldnum5):
        ldnum2 = random.randint(1,45)
    while (ldnum3 == ldnum1) or (ldnum3 == ldnum2) or (ldnum3 == ldnum4) or (ldnum3 == ldnum5):
        ldnum3 = random.randint(1,45)
    while (ldnum4 == ldnum1) or (ldnum4 == ldnum2) or (ldnum4 == ldnum3) or (ldnum4 == ldnum5):
        ldnum4 = random.randint(1,45)
    while (ldnum5 == ldnum1) or (ldnum5 == ldnum2) or (ldnum5 == ldnum3) or (ldnum5 == ldnum4):
        ldnum5 = random.randint(1,45)
    
    ldlist = [ldnum1,ldnum2,ldnum3,ldnum4,ldnum5]
    ldlist.sort()
    
    print(ldlist)
    
def lotto():
    print('\n')
    lnum1 = random.randint(1,52)
    lnum2 = random.randint(1,52)
    lnum3 = random.randint(1,52)
    lnum4 = random.randint(1,52)
    lnum5 = random.randint(1,52)
    lnum6 = random.randint(1,52)
    
    while (lnum1 == lnum2) or (lnum1 == lnum3) or (lnum1 == lnum4) or (lnum1 == lnum5) or (lnum1 == lnum6):
        lnum1 = random.randint(1,52)
    while (lnum2 == lnum1) or (lnum2 == lnum3) or (lnum2 == lnum4) or (lnum2 == lnum5) or (lnum2 == lnum6):
        lnum2 = random.randint(1,52)
    while (lnum3 == lnum1) or (lnum3 == lnum2) or (lnum3 == lnum4) or (lnum3 == lnum5) or (lnum3 == lnum6):
        lnum3 = random.randint(1,52)
    while (lnum4 == lnum1) or (lnum4 == lnum2) or (lnum4 == lnum3) or (lnum4 == lnum5) or (lnum4 == lnum6):
        lnum4 = random.randint(1,52)
    while (lnum5 == lnum1) or (lnum5 == lnum2) or (lnum5 == lnum3) or (lnum5 == lnum4) or (lnum5 == lnum6):
        lnum5 = random.randint(1,52)
    while (lnum6 == lnum1) or (lnum6 == lnum2) or (lnum6 == lnum3) or (lnum6 == lnum4) or (lnum6 == lnum5):
        lnum6 = random.randint(1,52)
    
    llist = [lnum1,lnum2,lnum3,lnum4,lnum5,lnum6]
    llist.sort()
    
    print(llist)
    
import random

def machine():
        

    menuselection = ''
    
    while menuselection == '':
        print('1. Powerball')
        print('2. Mega Million')
        print('3. Lucky Day lotto')
        print('4. Lotto')
        print('\n\n9. Quit\n')
        menuselection = input('Select lottery or quit: ')
        if menuselection == '1':
            powerball()
            print('\n')
            machine()
        elif menuselection == '2':
            megamilly()
            print('\n')
            machine()
        elif menuselection == '3':
            luckyday()
            print('\n')
            machine()
        elif menuselection == '4':
            lotto()
            print('\n')
            machine()
        else:
            print('Invalid selection, pick 1,2,3,or 4.')
    
        menuselection = input('Select lottery or quit: ')
        
        
machine()
    
