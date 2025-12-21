# This is the first file learning the basics of tkinter. It will be a basic food price app.
# Other than that not that impressive! 

from tkinter import *

root = Tk()
root.title('Food Price App')
root.geometry('300x200')
root.resizable(width=False, height=False)
color = 'gray77'
root.configure(bg=color)

v = IntVar()
res = IntVar()
# v = StringVar()

def cal_price():
    value = int(v.get())
    if value == 0: 
        res.set(int(entry_2.get()) * 4)
    elif value == 1:
        res.set(int(entry_2.get()) * 6) 
    elif value == 2: 
        res.set(int(entry_2.get()) * 10) 

label = Label(root, text='Choose An Item', bg=color)
label.place(x=100, y=5)

r_btn = Radiobutton(root, text='Banana', bg=color, variable=v, value=0)
r_btn.place(x=5, y=30)

r_btn2 = Radiobutton(root, text='Apple', bg=color, variable=v, value=1)
r_btn2.place(x=5, y=60)

r_btn3 = Radiobutton(root, text='Orange', bg=color, variable=v, value=2)
r_btn3.place(x=5, y=90)

entry = Entry(root, width=20, textvariable=res)
entry.place(x=80, y=130)

label_res = Label(root, text='Price', bg=color)
label_res.place(x=5, y=130)

entry_2 = Entry(root, width=20)
entry_2.place(x=80, y=160)

# highlight background 
btn_cal = Button(root, text="Cal", command=lambda:cal_price(), highlightbackground=color)
btn_cal.place(x=5, y=150)


root.mainloop()
