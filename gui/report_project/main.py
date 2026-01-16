# This is a test program for an application that I want to build for my work. 

# importing supporting libraries for project
from tkinter import * 
from tkinter import filedialog
import pandas as pd
import os
import json
import glob

class ReportGui:
  
  def __init__(self, master):
    self.master = master
    self.monthly_report = pd.read_excel(
        './new_month_report/new_report_1.xlsx',
        sheet_name=None,
        engine='openpyxl'
    ) 
    self.CLP_DF = self.monthly_report["CLP"]
    self.EXC_DF = self.monthly_report["EXC"]
    self.WIGI_DF = self.monthly_report["WIGI"]
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