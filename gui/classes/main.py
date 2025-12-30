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
    self.btn = Button(master, text='Click Me', command=self.btn_action)
    self.btn.pack()
    self.btn2 = Button(master, text='Quit', command=self.quit)
    self.btn2.pack()

  def btn_action(self):
    print('This button is clicked')

  def quit(self):
    self.master.quit()


root = Tk() 
my_app = MyFirstUI(root)
root.mainloop()