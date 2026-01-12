# This will be a simple calculator app with tkinter
from tkinter import *
import tkinter.messagebox

# ---------- Settings ---------

root = Tk()
root.geometry('400x150')
root.title('Calculator')
color='gray'
root.configure(bg=color)
root.resizable(width=False, height=False)

# ---------- Varaibles ---------

num1 = StringVar()
num2 = StringVar()
res_value = StringVar()

# ---------- Frames ---------

top_first = Frame(root, width=800, height=40, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=800, height=40, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=800, height=40, bg=color)
top_third.pack(side=TOP)

top_fourth = Frame(root, width=800, height=40, bg=color)
top_fourth.pack(side=TOP)

# ---------- Functions ---------

def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_value.set(value)
    except: 
        errorMsg('Error')

def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_value.set(value)
    except: 
        errorMsg('Error')

def multiply():
    try:
        value = float(num1.get()) * float(num2.get())
        res_value.set(value)
    except: 
        errorMsg('Error')

def divide():
    if num2.get() == "0":
        errorMsg('divisionerror')
    elif num2.get() != "0":
        try:
            value = float(num1.get()) / float(num2.get())
            res_value.set(value)
        except: 
            errorMsg('Error')

def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error!', 'Something went really wrong!')
    elif ms == 'divisionerror':
        tkinter.messagebox.showerror('Division Error!', 'Cannot Divide by zero')


# ---------- Button ---------

btn_plus = Button(top_third, text='+', width=6, highlightbackground=color, command=lambda : plus())
btn_plus.pack(side=LEFT, padx=3, pady=3)

btn_minus = Button(top_third, text='-', width=6, highlightbackground=color, command=lambda : minus())
btn_minus.pack(side=LEFT, padx=3, pady=3)

btn_mul = Button(top_third, text='*', width=6, highlightbackground=color, command=lambda : multiply())
btn_mul.pack(side=LEFT, padx=3, pady=3)

btn_div = Button(top_third, text='/', width=6, highlightbackground=color, command=lambda : divide())
btn_div.pack(side=LEFT, padx=3, pady=3)


# ---------- Entry + Labels ---

label_first_num = Label(top_first, text="Input Number 1:", bg=color)
label_first_num.pack(side=LEFT, padx=5, pady=5)

first_num = Entry(top_first, highlightbackground=color, textvariable=num1)
first_num.pack(side=LEFT)

label_second_num = Label(top_second, text="Input Number 2:", bg=color)
label_second_num.pack(side=LEFT, padx=5, pady=5)

second_num = Entry(top_second, highlightbackground=color, textvariable=num2)
second_num.pack(side=LEFT)

res = Label(top_fourth, text="Result:", bg=color)
res.pack(side=LEFT, padx=5, pady=5)

res_num = Entry(top_fourth, highlightbackground=color, textvariable=res_value)
res_num.pack(side=LEFT)

root.mainloop()


