# This is a test program for an application that I want to build for my work. 

from tkinter import * 
from tkinter import filedialog

class ReportGui:
  
  def __init__(self, master):
    self.master = master 
    self.master.title('Report Makr')
    self.master.geometry('400x400')
    self.master.color = 'gray55'
    self.master.configure(bg=self.master.color)
    self.btn = Button(master, text='Select New Report', command=self.get_new_monthly_report)
    self.btn.pack()
  
  def get_new_monthly_report(self):
    root.filename = filedialog.askopenfilename()
  
  def break_up_new_monthly_report(self):
    pass




root = Tk() 
my_app = ReportGui(root)
root.mainloop()