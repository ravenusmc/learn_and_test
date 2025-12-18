# This is the first file learning the basics of tkinter. It will be a basic food price app. 

from tkinter import *

root = Tk()
root.title('Food Price App')
root.geometry('300x200')
root.resizable(width=False, height=False)
color = 'gray77'
root.configure(bg=color)

v = StringVar()

label = Label(root, text='Choose An Item', bg=color)
label.place(x=100, y=5)

r_btn = Radiobutton(root, text='Banana', bg=color, variable=v, value='Banana')
r_btn.place(x=5, y=30)

r_btn2 = Radiobutton(root, text='Apple', bg=color, variable=v, value='Apple')
r_btn2.place(x=5, y=60)

r_btn3 = Radiobutton(root, text='Orange', bg=color, variable=v, value='Orange')
r_btn3.place(x=5, y=90)

entry = Entry(root, width=20)
entry.place(x=80, y=130)

label_res = Label(root, text='Price', bg=color)
label_res.place(x=5, y=130)

entry = Entry(root, width=20)
entry.place(x=80, y=130)

entry_2 = Entry(root, width=20)
entry_2.place(x=80, y=160)

# highlight background 
btn = Button(root, text='Cal', highlightbackground=color)
btn.place(x=5, y=160)


root.mainloop()
