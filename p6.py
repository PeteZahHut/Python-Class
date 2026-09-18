# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:02:47 2026

@author: peterp
"""
ans = 'y'
while (ans == 'y') or (ans == 'Y'):
    print('-------------------------------')
    minutes = float(input('Enter running minutes: '))
    cr = 4.33
    starttime = 5
    endtime = minutes
    
    if minutes < 5:
        print('Minutes must be greater than 5')
    elif minutes >= 5:
        while (starttime<=endtime):
            cal=starttime*cr
            print('minutes: ', starttime, ' ','calories: ',cal)
            starttime = starttime + 5
            
    ans = input('\nContinue y/n -> ')
print('----done')
