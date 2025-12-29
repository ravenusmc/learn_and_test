from tkinter import * 

class MyFirstUI:
  
  def __init__(self, master): 
    self.master = master 
    self.master.title('A Simple UI')
    self.master.geometry('400x400')
    self.master.color = 'gray55'
    self.master.configure(bg=self.master.color)
    self.label = Label(master, text='This is label')
    self.label.pack()




root = Tk() 
my_app = MyFirstUI(root)
root.mainloop()