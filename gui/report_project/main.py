# This is a test program for an application that I want to build for my work. 

# importing supporting libraries for project
from tkinter import * 
from tkinter import filedialog
from io import StringIO
import pandas as pd
import os
import json
import glob
from tkinter import messagebox


class ReportGui:
  
  def __init__(self, master):
    # GUI Parameters 
    self.master = master
    self.master.title('Report Makr')
    self.master.geometry('400x300')
    self.master.color = 'gray55'
    self.master.configure(bg=self.master.color)
    # Office codes JSON set up 
    self.office_code_map = self.load_office_codes()
    #Reports Parameters 
    self.monthly_report = ""
    self.CLP_DF = ""
    self.EXC_DF = ""
    self.WIGI_DF = ""
    # These are the CSV files 
    self.CLP_OLD = ""
    self.EXC_OLD = ""
    self.WIGI_OLD = ""
    # These are the sorted and cleaned CSV files 
    self.CLP_Filtered_Old = ""
    self.office = ""
    self.offices = ['ABC', 'DEF', 'GHI']
    self.office_var = StringVar()
    self.office_var.set(self.offices[0])
    self.month = ""
    self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    self.month_var = StringVar()
    self.month_var.set(self.months[0])

    self.month_var = StringVar()
    # Entry Office code: 
    row = Frame(master, bg=self.master.color)
    row.pack(pady=10)
    Label(row, text="Office:", bg=self.master.color).pack(side=LEFT, padx=(0, 5))
    self.office_menu = OptionMenu(
      row,
      self.office_var,
      *self.offices
    )
    self.office_menu.config(bg=self.master.color)
    self.office_menu.pack(side=LEFT)

    # Entry Month Code: 
    row_2 = Frame(master, bg=self.master.color)
    row_2.pack(pady=10)
    Label(row_2, text="Month:", bg=self.master.color).pack(side=LEFT, padx=(0, 5))
    self.month_menu = OptionMenu(
        row_2,
        self.month_var,
        *self.months
    )
    self.month_menu.config(bg=self.master.color)
    self.month_menu.pack(side=LEFT)

    # Buttons 
    self.btn = Button(master, text='Select New Report', command=self.get_new_monthly_report)
    self.btn.pack()
    self.btn = Button(master, text='Select Old Monthly Report', command=self.get_new_monthly_report)
    self.btn.pack()
    self.btn = Button(master, text='Execute Program', command=self.build_new_report)
    self.btn.pack()
  
  def get_new_monthly_report(self):
    self.office = self.office_var.get().strip()
    self.month = self.month_var.get().strip()
    if not self.office:
      messagebox.showerror("Missing Office", "Please enter an office name.")
      return
    if not self.month:
      messagebox.showerror("Missing Month", "Please enter a month")
      return
    # print("Office entered:", self.office) 
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
    self.export_all_sheets_to_csv()
  
  def export_all_sheets_to_csv(self):
      self.csv_buffers = {}
      for sheet_name, df in self.monthly_report.items():
          csv_text = self.df_to_csv_string(df)
          self.csv_buffers[sheet_name] = csv_text
          if sheet_name == "CLP":
              self.CLP_OLD = csv_text
          elif sheet_name == "EXC":
              self.EXC_OLD = csv_text
          elif sheet_name == "WIGI":
              self.WIGI_OLD = csv_text
  
  def build_new_report(self):
    self.filter_clps_by_office()
  
  def filter_clps_by_office(self):
    df = pd.read_csv(StringIO(self.CLP_OLD))
    df.columns = df.columns.str.strip().str.upper()
    org_field = "ORG CODE"
    sort_field = "ENTER PRES GR"
    df_filtered = df[df[org_field].isin(self.office_code_map[self.office])]
    df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
    self.CLP_Filtered_Old = self.df_to_csv_string(df_filtered)
    # print(self.CLP_Filtered_Old.splitlines()[:5])

  
  def break_up_new_monthly_report(self):
    pass

  # The methods below here are support methods...maybe one day move to another class...
  # This method is for the JSON file. 
  def load_office_codes(self):
    print(os.getcwd())
    config_path = os.path.join(os.getcwd(), "./office_codes/offices_and_codes.json")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror(
            "Missing Configuration",
            "office_codes.json not found.\nThe application cannot continue."
        )
        self.master.destroy()
        return {}
  
  def df_to_csv_string(self, df):
    buffer = StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue()




root = Tk() 
my_app = ReportGui(root)
root.mainloop()