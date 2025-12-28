from tkinter import * 

root = Tk()
root.geometry('500x500')
root.title('Frames')

frame1 = Frame(root, width=250, height=500, bg='red')
frame1.pack(side=LEFT)

frame2 = Frame(root, width=250, height=500, bg='blue')
frame2.pack(side=RIGHT)

root.mainloop()