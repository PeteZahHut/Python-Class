# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:04:17 2026

@author: peterp

I call it the "raised eyebrow bald Bruce Rauner"
"""

from tkinter import *
def main():
    mainwin = Tk()
    color = 'gray'
    wcan = Canvas(mainwin,bg=color,
        width=600,height=800)
    wcan.create_oval(50, 50, 550, 625, # creates head
                     fill='pink', outline='black', width=5) # kind of like css
    wcan.create_line(300, 628, 300, 798,
                     fill='black', width=5)
    wcan.create_line(100, 200, 200, 225,  # first eyebrow
                     fill='gray', width=5)
    wcan.create_line(400, 200, 500, 200,  # second eyebrow
                     fill='gray', width=5)
    wcan.create_oval(125, 275, 175, 325,
                     fill='lightblue', outline='black', width=2) # first eye
    wcan.create_oval(450, 275, 400, 325,
                     fill='lightblue', outline='black', width=2) # second eye
    wcan.create_oval(130, 287, 150, 300, # eye pupil 1
                     fill='black')
    wcan.create_oval(430, 287, 450, 300, # eye pupil 2
                     fill='black')
    wcan.create_line(263, 301, 263, 400,
                     fill='black', width=5) # nose
    wcan.create_line(97, 367, 281, 424,
                     fill='black', width=5) # mouth part 1
    wcan.create_line(281, 424, 497, 367,
                     fill='black', width=5) # mouth part 2
    
    wcan.pack()
    
    mainwin.mainloop()
main()