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

def get_name():
    print(entry.get())
    entry.insert(0, 'This is my name: ')

#Adding buttons 
# btn = Button(root, text="Click Me!", command= lambda : print_name())
# btn.place(x=0, y=0)

# label = Label(root, textvariable=name)
# label.place(x=100,y=100)

#Adding Entry 
# entry = Entry(root)
# entry.place(x=45, y=0)

# label = Label(root, text='Name: ')
# label.place(x=0, y=0)

# btn = Button(root, text='Get Name', command= lambda : get_name())
# btn.place(x=100,y=100)



root.mainloop()