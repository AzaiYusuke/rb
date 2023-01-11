
import tkinter as tk
root =tk.Tk()
root.geometry("900x600")

canvas=tk.Canvas(root,bg="white")

canvas.pack(fill=tk.BOTH,expand=1)

canvas.create_rectangle(200,10,300,100,fill='black')
canvas.create_rectangle(100,100,400,200,fill='black')
canvas.create_oval(130,200,200,270,fill='black')
canvas.create_oval(300,200,370,270,fill='black')

canvas.create_line(50,300,70,320,width=5,tag="line")
canvas.create_line(90,300,70,320,width=5,tag="line")
canvas.create_line(70,320,70,340,width=5,tag="line")

canvas.create_line(100,300,100,340,width=5,tag="line")
canvas.create_line(98,340,143,340,width=5,tag="line")
canvas.create_line(140,300,140,340,width=5,tag="line")

canvas.create_line(150,300,190,300,width=5,tag="line")
canvas.create_line(150,300,150,310,width=5,tag="line")
canvas.create_line(150,310,190,330,width=5,tag="line")
canvas.create_line(190,330,190,340,width=5,tag="line")
canvas.create_line(150,340,190,340,width=5,tag="line")

canvas.create_line(200,300,200,340,width=5,tag="line")
canvas.create_line(198,340,243,340,width=5,tag="line")
canvas.create_line(240,300,240,340,width=5,tag="line")

canvas.create_line(250,300,250,340,width=5,tag="line")
canvas.create_line(250,320,290,300,width=5,tag="line")
canvas.create_line(260,315,290,340,width=5,tag="line")

canvas.create_line(300,300,300,340,width=5,tag="line")
canvas.create_line(300,300,340,300,width=5,tag="line")
canvas.create_line(300,320,340,320,width=5,tag="line")
canvas.create_line(300,340,340,340,width=5,tag="line")

canvas.create_line(400,340,420,300,width=5,tag="line")
canvas.create_line(420,300,440,340,width=5,tag="line")
canvas.create_line(407,326,433,326,width=5,tag="line")

canvas.create_line(450,300,490,300,width=5,tag="line")
canvas.create_line(490,300,450,340,width=5,tag="line")
canvas.create_line(450,340,490,340,width=5,tag="line")

canvas.create_line(500,340,520,300,width=5,tag="line")
canvas.create_line(520,300,540,340,width=5,tag="line")
canvas.create_line(507,326,533,326,width=5,tag="line")

canvas.create_line(567,300,575,300,width=5,tag="line")
canvas.create_line(570,300,570,340,width=5,tag="line")
canvas.create_line(567,340,575,340,width=5,tag="line")
root.mainloop()
