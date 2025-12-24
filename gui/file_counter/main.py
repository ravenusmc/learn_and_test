from tkinter import *
from tkinter import filedialog

root = Tk()

def clear_text():
    word_list.delete(0, END)  
    answer.delete("1.0", END)  

def open_file(): 
    root.filename = filedialog.askopenfilename()

#setting program up
root.geometry('500x500')
root.title('File Counter')
color = 'gray'
root.configure(bg=color)

word_list = Entry(root, width=50)
word_list.place(x=0, y=0)

#Buttons 
file = Button(root, text='Select File', width=50, highlightbackground=color, command=lambda : open_file())
file.place(x=0, y=30)
count = Button(root, text='Count Words', width=50, highlightbackground=color).place(x=0, y=60)
clear = Button(root, text='Clear Text', width=50, highlightbackground=color, command=lambda : clear_text()).place(x=0, y=90)

#text field 
answer = Text(root, height=30, width=70, bg='gray77')
answer.place(x=0, y=120)

root.mainloop()