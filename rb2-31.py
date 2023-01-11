# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 11:36:32 2022

@author: azale
"""

import tkinter as tk
root =tk.Tk()
root.geometry("600x600")

canvas=tk.Canvas(root,bg="white")

canvas.pack(fill=tk.BOTH,expand=1)
for num in range(10):
    for num2 in range(10):
        if num%2==0:
            if num2%2==0:
                canvas.create_rectangle(num*40+50,num2*40+10,num*40+60,num2*40+20,fill='red')
                canvas.create_rectangle(num*40+40,num2*40+20,num*40+70,num2*40+30,fill='red')
                canvas.create_oval(num*40+43,num2*40+30,num*40+50,num2*40+37,fill='black')
                canvas.create_oval(num*40+60,num2*40+30,num*40+67,num2*40+37,fill='black')
            else:
                canvas.create_rectangle(num*40+50,num2*40+10,num*40+60,num2*40+20,fill='blue')
                canvas.create_rectangle(num*40+40,num2*40+20,num*40+70,num2*40+30,fill='blue')
                canvas.create_oval(num*40+43,num2*40+30,num*40+50,num2*40+37,fill='black')
                canvas.create_oval(num*40+60,num2*40+30,num*40+67,num2*40+37,fill='black')
        if num%2==1:
            if num2%2==1:
                canvas.create_rectangle(num*40+50,num2*40+10,num*40+60,num2*40+20,fill='red')
                canvas.create_rectangle(num*40+40,num2*40+20,num*40+70,num2*40+30,fill='red')
                canvas.create_oval(num*40+43,num2*40+30,num*40+50,num2*40+37,fill='black')
                canvas.create_oval(num*40+60,num2*40+30,num*40+67,num2*40+37,fill='black')
            else:
                canvas.create_rectangle(num*40+50,num2*40+10,num*40+60,num2*40+20,fill='blue')
                canvas.create_rectangle(num*40+40,num2*40+20,num*40+70,num2*40+30,fill='blue')
                canvas.create_oval(num*40+43,num2*40+30,num*40+50,num2*40+37,fill='black')
                canvas.create_oval(num*40+60,num2*40+30,num*40+67,num2*40+37,fill='black')

val=input()
if int(val)<100 and int(val)>=0:
    canvas.create_rectangle(int(val)%10*40+50,int(int(val)/10)*40+10,int(val)%10*40+60,int(int(val)/10)*40+20,fill='white',outline='white')
    canvas.create_rectangle(int(val)%10*40+40,int(int(val)/10)*40+20,int(val)%10*40+70,int(int(val)/10)*40+30,fill='white',outline='white')
    canvas.create_oval(int(val)%10*40+43,int(int(val)/10)*40+30,int(val)%10*40+50,int(int(val)/10)*40+37,fill='white',outline='white')
    canvas.create_oval(int(val)%10*40+60,int(int(val)/10)*40+30,int(val)%10*40+67,int(int(val)/10)*40+37,fill='white',outline='white')
    root.mainloop()  
else:
    print('Error 再入力してください')
              