import tkinter as tk
root =tk.Tk()
root.geometry("1000x1000")

canvas=tk.Canvas(root,bg="white")

canvas.pack(fill=tk.BOTH,expand=1)

canvas.create_rectangle(150,10,350,100,fill='red')
canvas.create_rectangle(100,100,400,200,fill='red')
canvas.create_oval(130,200,200,270,fill='black')
canvas.create_oval(300,200,370,270,fill='black')

canvas.create_rectangle(400,310,800,490,fill='blue')
canvas.create_rectangle(300,490,900,690,fill='blue')
canvas.create_oval(360,690,500,830,fill='black')
canvas.create_oval(700,690,840,830,fill='black')
root.mainloop()