from tkinter import *

root = Tk()
root.title('Food Price App')
root.geometry('300x200')
root.resizable(width=False, height=False)
root.configure(bg='gray77')

label = Label(root, text='Choose An Item')
label.place(x=100, y=5)

r_btn = Radiobutton(root, text='Banana')
r_btn.place(x=5, y=30)

r_btn2 = Radiobutton(root, text='Apple')
r_btn2.place(x=5, y=60)

r_btn3 = Radiobutton(root, text='Orange')
r_btn3.place(x=5, y=90)


root.mainloop()
