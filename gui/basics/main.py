# This is from one of my udemy courses. 

from tkinter import *

root = Tk()
root.title('First Project')
root.geometry('300x300')
root.resizable(width=False, height=False)

# Working with labels 
# label = Label(root, text="Cool!")
# label.place(x=0, y=0)

name = StringVar()

def print_name():
    name.set('Hello')

#Adding buttons 
btn = Button(root, text="Click Me!", command= lambda : print_name())
btn.place(x=0, y=0)

label = Label(root, textvariable=name)
label.place(x=100,y=100)


root.mainloop()