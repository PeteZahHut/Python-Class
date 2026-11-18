# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:16:25 2026

@author: wrl123u
"""

from tkinter import *

from tkinter import messagebox

def calculate(txtbox1,txtbox2,txtbox3):
    try:
        
        kelvin = txtbox1.get()
        kelvin = float(kelvin)
        k2c = kelvin - 273.15
        k2f = 9/5 * (kelvin - 273) + 32
        
        txtbox2.insert(0,k2c)
        txtbox3.insert(0,k2f)
    except:
        
        messagebox.showinfo("Error message", "invalid kelvin number")

def cleare(txtbox1,txtbox2,txtbox3):
    
    txtbox1.delete(0, END)
    txtbox2.delete(0, END)
    txtbox3.delete(0, END)
    
def main():
    winmain = Tk()
    winmain.geometry('800x600+600+300')
    winmain.title("** Temperature Conversion Program**")
    winmain.configure(bg='black')
    
    lbltext = Label(winmain,text="Temperature Conversion",
                   fg="black",bg="red",font=("Arial Bold", 30))
    lbltext.place(x=150,y=1)
    
    l1 = Label(winmain,text="Kelvin:",bd=20,fg="red")
    l1.place(x=160,y=120)
    
    l2 = Label(winmain,text="Celsius:",bd=20,fg="red")
    l2.place(x=160,y=220)
    
    l3 = Label(winmain,text="Fahrenheit:",bd=20,fg="red")
    l3.place(x=160,y=320)
    print ('txtboxes')
    txtbox1 = Entry(winmain,width=30) # input box for Kelvin
    txtbox1.place(x=300,y=100)
   
    txtbox2 = Entry(winmain,width=30)
    txtbox2.place(x=300,y=200)
    
    txtbox3 = Entry(winmain,width=30)
    txtbox3.place(x=300,y=300)
    
    #    
    btn1 = Button(winmain, text="QUIT",command=lambda:winmain.destroy()) # lamba:winmain.destroy works as an alternative of "command=quit"
    btn1.place(x=400,y=550)
    
    btn2 = Button(winmain, text="CALC",command=lambda:calculate(txtbox1,txtbox2,txtbox3)) # calculates using Kelvin
    btn2.place(x=200,y=450)
    
    btn3 = Button(winmain, text="CLEAR",command=lambda:cleare(txtbox1,txtbox2,txtbox3)) # clears all textboxes
    btn3.place(x=400,y=450)


    winmain.mainloop()
main()
