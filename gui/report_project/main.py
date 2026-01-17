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
    self.monthly_report = ""
    self.CLP_DF = ""
    self.EXC_DF = ""
    self.WIGI_DF = ""
    self.master.title('Report Makr')
    self.master.geometry('400x400')
    self.master.color = 'gray55'
    self.master.configure(bg=self.master.color)
    self.btn = Button(master, text='Select New Report', command=self.get_new_monthly_report)
    self.btn.pack()
    self.label = Label(master, text='This is label')
    self.label.pack()
  
  def get_new_monthly_report(self):
    file_path = filedialog.askopenfilename(
        title="Select Monthly Report",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    if not file_path:
        return  # user cancelled
    self.monthly_report = pd.read_excel(
        file_path,
        sheet_name=None,
        engine='openpyxl'
    )
    self.CLP_DF = self.monthly_report["CLP"]
    self.EXC_DF = self.monthly_report["EXC"]
    self.WIGI_DF = self.monthly_report["WIGI"]
  
  def break_up_new_monthly_report(self):
    pass




root = Tk() 
my_app = ReportGui(root)
root.mainloop()