from tkinter import * 

root = Tk() 

def getV():
    print(s.get())

lang = ['Python', "JavaScript", "PHP", "C++"]
s = StringVar() 

s.set(lang[0])

menu = OptionMenu(root, s, *lang)
menu.pack()

btn = Button(root, text='click me', command=lambda : getV())
btn.pack()

root.mainloop() 