from tkinter import *

root = Tk()

#setting program up
root.geometry('500x500')
root.title('File Counter')
color = 'gray'
root.configure(bg=color)

word_list = Entry(root, width=50).place(x=0, y=0)

#Buttons 
file = Button(root, text='Select File', width=50, highlightbackground=color).place(x=0, y=30)
count = Button(root, text='Count Words', width=50, highlightbackground=color).place(x=0, y=60)
clear = Button(root, text='Clear Text', width=50, highlightbackground=color).place(x=0, y=90)

#text field 
answer = Text(root, height=30, width=70, bg='gray77').place(x=0, y=120)

root.mainloop()