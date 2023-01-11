
import tkinter as tk
root =tk.Tk()
root.geometry("900x600")

canvas=tk.Canvas(root,bg="white")

canvas.pack(fill=tk.BOTH,expand=1)

canvas.create_rectangle(200,10,700,300,fill='black')
root.mainloop()
