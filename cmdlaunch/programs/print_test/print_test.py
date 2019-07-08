from tkinter import *

root = Tk()


class MyFirstGUI:
    def __init__(self, master):
        self.master = master


my_gui = MyFirstGUI(root)
root.mainloop()
