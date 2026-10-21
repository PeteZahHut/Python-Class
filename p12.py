# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:05:58 2026

@author: wrl123u
"""

def main():
    rainfall = []
    raindirectory = 'c:/temp/weather_data.txt'
    raindata = open(raindirectory, 'r')
    rainline = raindata.readline()
    
    while rainline != '':
        rainline = rainline.strip()
        rf = float(rainline)
        rainfall.append(rf)
        rainline = raindata.readline()
    raindata.close()
    
    print(rainfall)
    input("enter to continue")
    lowest = min(rainfall)
    highest = max(rainfall)
    total = sum(rainfall)
    average = total / len(rainfall)
    print('Data list:\n')
    print(rainfall,'\n')
    print('Highest:', highest)
    print('Lowest:', lowest)
    print('Total:', total)
    print('Average:', average)
    
    
    
main()
   
   










