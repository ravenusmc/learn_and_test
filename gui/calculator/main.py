# This will be a simple calculator app. 
from tkinter import *

# ---------- Settings 

root = Tk()
root.geometry('400x150')
root.title('Calculator')
color='gray'
root.configure(bg=color)
root.resizable(width=False, height=False)

# ---------- Frames 

top_first = Frame(root, width=800, height=40, bg='red')
top_first.pack(side=TOP)

top_second = Frame(root, width=800, height=40, bg='black')
top_second.pack(side=TOP)

top_third = Frame(root, width=800, height=40, bg=color)
top_third.pack(side=TOP)

top_fourth = Frame(root, width=800, height=40, bg='white')
top_fourth.pack(side=TOP)

# ---------- Button 

btn_plus = Button(top_third, text='+', width=6, highlightbackground=color)
btn_plus.pack(side=LEFT, padx=3, pady=3)

btn_minus = Button(top_third, text='-', width=6, highlightbackground=color)
btn_minus.pack(side=LEFT, padx=3, pady=3)

btn_mul = Button(top_third, text='*', width=6, highlightbackground=color)
btn_mul.pack(side=LEFT, padx=3, pady=3)

btn_div = Button(top_third, text='/', width=6, highlightbackground=color)
btn_div.pack(side=LEFT, padx=3, pady=3)



root.mainloop()