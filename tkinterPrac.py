#Animations with tkinter
import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello = tk.Button(self)
        self.hello["text"] = "Click me"
        self.hello["command"] = self.sayHello
        self.hello.pack(side = "top")
        
        self.quit = tk.Button(self,text = "EXIT",fg = "blue", command = root.destroy)
        self.quit.pack(side = "bottom")

    def sayHello(self):
        print("I am learning animation")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
