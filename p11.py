# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:41:34 2026

@author: wrl123u
"""
from datetime import date
from datetime import time
from datetime import datetime

def valgrade(pts):
    msg=""
    try:
        fscore = float(pts)
        if fscore < 0 or fscore > 1000:
            if fscore < 0:
                
                msg="score cannot be negative"
            else:
                msg="score cannot be over 1000"
        
    except:
        msg="score is not numeric"
    return msg

def main():
    print('Program has started on: ',datetime.date) # prints the date the program started
    eofm = "\n"
    filename = 'c:/temp/points.txt' # file directory
    datafile = open(filename,'r') # reads the file
    
    gradedir = 'c:/temp/grades.txt' # file directory to store grades
    error = 'c:/temp/error.txt' # file directory to store errors
    outgrade = open(gradedir,'w') # writes the grade file
    outerror = open(error, 'w') # writes the error file
    
    
    rcdcnt = 0 # record count (general)
    ercdcnt = 0 # error record count
    grcdnt = 0 # graded record count
    
    line = datafile.readline()
    
    while line !='':
        line=line.strip()
        sids,snames,sgrades = line.split(',') # omits the commas
        
        msg=valgrade(sgrades)
        if msg=="":
            print('scores are good')
            fscore=float(sgrades)
            
            
            lettergrade = ''
            
            if fscore > 899:
                lettergrade = 'A'
            elif fscore > 899 or fscore > 799:
                lettergrade = 'B'
            elif fscore > 799 or fscore > 699:
                lettergrade = 'C'
            elif fscore > 699 or fscore > 599:
                lettergrade = 'D'
            else:
                lettergrade = 'F'
            # print(fscore, ' ', lettergrade)
            
            line = line+' '+lettergrade
            outgrade.write(line + '\n')
            rcdcnt = rcdcnt+1
            grcdnt = grcdnt+1
            
        else:
            # print(msg)   
            # print(sgrades)
            
            outerror.write(line + ',' + msg + '\n')
            rcdcnt = rcdcnt+1
            ercdcnt = ercdcnt+1
        
        
        
        line = datafile.readline()  ###  end of the loop ###
    
    print('Number of Records Read: ',rcdcnt )
    print('Number of graded records: ',grcdnt)
    print('Number of error records: ',ercdcnt)
    print('Program ended on: ',datetime.date) # prints date the program was ended
    datafile.close()
    print('\na done deal')
    
    
    outgrade.write(sids+ ',' + snames + ',' + sgrades+eofm)
    outgrade.close()
    outerror.close()
    return
main()