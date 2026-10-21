# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:34:14 2026

@author: wrl123u
"""
def main():
    # set up the dictionary
    romandt = { 1: 'I',
                2: 'II',
                3: 'III',
                4: 'IV',
                5: 'V',
                6: 'VI',
                7: 'VII',
                8: 'VIII',
                9: 'IX',
                10: 'X',
                11: 'XI',
                12: 'XII',
                13: 'XIII',
                14: 'XIV',
                15: 'XV',
                16: 'XVI',
                17: 'XVII',
                18: 'XVIII',
                19: 'XIX',
                20: 'XX',
                21: 'XXI',
                22: 'XXII',
                23: 'XXIII',
                24: 'XXIV'}
    print(romandt)
    
    ans = 'y'
    while (ans == 'y') or (ans == 'Y'):
        try:
            normalnumber = int(input('Give me a number: '))
            if normalnumber in romandt:
                print(romandt[normalnumber])
               
            elif (normalnumber <= 0) or (normalnumber < 1):
                print('Invalid number')
                
            else:
                    print('not in the dictionary')
                    ans = input('Would you like to add this number to the dictionary? y/n: ')
                    if (ans == 'y') or (ans == 'Y'):
                        romanumeral = input('What is the roman numeral that you want to store this number as? ')
                        romandt[normalnumber] = romanumeral
        
        except:
            print('\nError')
        ans = input('Would you like to continue? y/n: ')
main()