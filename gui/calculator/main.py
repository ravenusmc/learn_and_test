# This will be a simple calculator app. 
from tkinter import *

# ---------- Settings 

root = Tk()
root.geometry('400x150')
root.title('Calculator')
color='gray'
root.configure(bg=color)

# ---------- Frames 

top_first = Frame(root, width=800, height=40, bg='red')
top_first.pack(side=TOP)

top_second = Frame(root, width=800, height=40, bg='black')
top_second.pack(side=TOP)

top_third = Frame(root, width=800, height=40, bg='blue')
top_third.pack(side=TOP)

top_fourth = Frame(root, width=800, height=40, bg='white')
top_fourth.pack(side=TOP)



root.mainloop()