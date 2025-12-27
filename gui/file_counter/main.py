from tkinter import *
from tkinter import filedialog

root = Tk()

count_result = dict()

def clear_text():
    word_list.delete(0, END)  
    answer.delete("1.0", END)  

def open_file(): 
    root.filename = filedialog.askopenfilename()

def count_text(file): 
    file_open = open(str(file), 'r')
    full_text = file_open.readlines()
    file_open.close()
    for word in word_list.get().split(', '):
        for text in full_text:
            if word in count_result:
                count_result[word] = count_result[word] + text.count(word)
            else: 
               count_result[word] = text.count(word)
    answer.delete('1.0', END)
    for k,v in count_result.items():
        answer.insert('1.0', '{0} {1} \n'.format(k,v))
    count_result.clear()


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
count = Button(root, text='Count Words', width=50, highlightbackground=color, command=lambda : count_text(root.filename))
count.place(x=0, y=60)
clear = Button(root, text='Clear Text', width=50, highlightbackground=color, command=lambda : clear_text())
clear.place(x=0, y=90)

#text field 
answer = Text(root, height=30, width=70, bg='gray77')
answer.place(x=0, y=120)

root.mainloop()