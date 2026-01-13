from tkinter import * 

class ReportGui:
  
  def __init__(self, master):
    self.master = master 
    self.master.title('Report Makr')
    self.master.geometry('400x400')
    self.master.color = 'gray55'
    self.master.configure(bg=self.master.color)




root = Tk() 
my_app = ReportGui(root)
root.mainloop()