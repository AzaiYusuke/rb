# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 12:31:18 2022

@author: azale
"""

import tkinter as tk
root =tk.Tk()
root.geometry("1000x1000")

canvas=tk.Canvas(root,bg="white")

canvas.pack(fill=tk.BOTH,expand=1)
for num in range(5):
    for num2 in range(5):
            canvas.create_rectangle(num*80+50,num2*80+10,num*80+60,num2*80+20,fill='red')
            canvas.create_rectangle(num*80+40,num2*80+20,num*80+70,num2*80+30,fill='red')
            canvas.create_oval(num*80+43,num2*80+30,num*80+50,num2*80+37,fill='black')
            canvas.create_oval(num*80+60,num2*80+30,num*80+67,num2*80+37,fill='black')
for num in range(5):
    for num2 in range(5):
            canvas.create_rectangle(num*80+90,num2*80+50,num*80+100,num2*80+60,fill='red')
            canvas.create_rectangle(num*80+80,num2*80+60,num*80+110,num2*80+70,fill='red')
            canvas.create_oval(num*80+83,num2*80+70,num*80+90,num2*80+77,fill='black')
            canvas.create_oval(num*80+100,num2*80+70,num*80+107,num2*80+77,fill='black')       
for num in range(5):
    for num2 in range(5):
            canvas.create_rectangle(num*80+90,num2*80+10,num*80+100,num2*80+20,fill='blue')
            canvas.create_rectangle(num*80+80,num2*80+20,num*80+110,num2*80+30,fill='blue')
            canvas.create_oval(num*80+83,num2*80+30,num*80+90,num2*80+37,fill='black')
            canvas.create_oval(num*80+100,num2*80+30,num*80+107,num2*80+37,fill='black')
for num in range(5):
    for num2 in range(5):
            canvas.create_rectangle(num*80+50,num2*80+50,num*80+60,num2*80+60,fill='blue')
            canvas.create_rectangle(num*80+40,num2*80+60,num*80+70,num2*80+70,fill='blue')
            canvas.create_oval(num*80+43,num2*80+70,num*80+50,num2*80+77,fill='black')
            canvas.create_oval(num*80+60,num2*80+70,num*80+67,num2*80+77,fill='black')       
      
root.mainloop()