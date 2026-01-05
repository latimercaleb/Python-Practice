#GoBall
from tkinter import *
import time

Width = 800
Height = 500
Size = 50
tk = Tk()
canvas = Canvas(tk,width = Width, height=Height,bg = "grey")
canvas.pack()
color = "black"
class Ball:
    def __init__(self):
        self.shape = canvas.create_oval(0,0,Size,Size,fill=color)
        self.speedx = 9
        self.speedy = 9
        self.active = True
        self.move_active()
        
    def ball_update(self):
        canvas.move(self.shape,self.speedx,self.speedy)
        pos = canvas.coords(self.shape)
        if  pos[2] >= Width or pos[0] <= 0:
            self.speedx*= -1
        if pos[3] >= Height or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self):
        if self.active :
            self.ball_update()
            tk.after(40,self.move_active)

ball = Ball()
tk.mainloop()
