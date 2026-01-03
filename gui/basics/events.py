from tkinter import * 

root = Tk() 

def key(event):
    print("pressed", event.char)

def callback(event):
    frame.focus_set()
    print("Eevent x", event.x, "Event y", event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()





root.mainloop() 