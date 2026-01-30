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
    self.old_monthly_report = ""
    self.CLP_DF = ""
    self.EXC_DF = ""
    self.WIGI_DF = ""
    self.CLP_DF_OLD = ""
    self.EXC_DF_OLD = ""
    self.WIGI_DF_OLD = ""
    # These are the CSV files 
    self.CLP_NEW = ""
    self.EXC_NEW = ""
    self.WIGI_NEW = ""
    self.CLP_OLD = ""
    self.EXC_OLD = ""
    self.WIGI_OLD = ""
    # These are the sorted and cleaned CSV files 
    self.CLP_Filtered_New = ""
    self.EXC_Filtered_New = ""
    self.WIGI_Filtered_New = ""
    # These are the filtered CSV files with notes added
    self.clp_with_notes_final = ""
    self.exc_with_notes_final = ""
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
    self.btn = Button(master, text='Select Old Monthly Report', command=self.get_old_month_report)
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
              self.CLP_NEW = csv_text
          elif sheet_name == "EXC":
              self.EXC_NEW = csv_text
          elif sheet_name == "WIGI":
              self.WIGI_NEW = csv_text

  def get_old_month_report(self):
    file_path = filedialog.askopenfilename(
        title="Select Monthly Report",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    if not file_path:
        return  # user cancelled
    self.old_monthly_report = pd.read_excel(
        file_path,
        sheet_name=None,
        engine='openpyxl'
    )
    self.CLP_DF_OLD = self.old_monthly_report["CLP"]
    self.EXC_DF_OLD = self.old_monthly_report["EXC"]
    self.WIGI_DF_OLD = self.old_monthly_report["WIGI"]
    self.export_all_sheets_to_csv_old_report()
  
  def export_all_sheets_to_csv_old_report(self):
    self.csv_buffers = {}
    for sheet_name, df in self.old_monthly_report.items():
        csv_text = self.df_to_csv_string(df)
        self.csv_buffers[sheet_name] = csv_text
        if sheet_name == "CLP":
            self.CLP_OLD = csv_text
        elif sheet_name == "EXC":
            self.EXC_OLD = csv_text
        elif sheet_name == "WIGI":
            self.WIGI_OLD = csv_text
  
  def build_new_report(self):
    self.office = self.office_var.get().strip()
    self.month = self.month_var.get().strip()
    if not self.office:
      messagebox.showerror("Missing Office", "Please enter an office name.")
      return
    if not self.month:
      messagebox.showerror("Missing Month", "Please enter a month")
      return
    if not self.monthly_report:
      messagebox.showerror("Missing New Month Report: Please Select")
      return
    if not self.old_monthly_report: 
       messagebox.showerror("Missing New Month Report: Please Select")
       return
    self.filter_clps_by_office()
    self.filter_EXC_by_office()
    self.filter_WIGI_by_office()
    self.build_new_clp_report()
    self.build_new_EXC_report()
    self.build_final_report()

  def filter_clps_by_office(self):
    df = pd.read_csv(StringIO(self.CLP_NEW))
    df.columns = df.columns.str.strip().str.upper()
    org_field = "ORG CODE"
    sort_field = "ENTER PRES GR"
    df_filtered = df[df[org_field].isin(self.office_code_map[self.office])]
    df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
    self.CLP_Filtered_New = self.df_to_csv_string(df_filtered)
    # print(self.CLP_Filtered_Old.splitlines()[:5])
  
  def filter_EXC_by_office(self):
    df = pd.read_csv(StringIO(self.EXC_NEW))
    df.columns = df.columns.str.strip().str.upper()
    org_field = "ORG_CODE"
    sort_field = "APPNT EFF DATE"
    df_filtered = df[df[org_field].isin(self.office_code_map[self.office])]
    df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
    self.EXC_Filtered_New = self.df_to_csv_string(df_filtered)
    
  def filter_WIGI_by_office(self):
    df = pd.read_csv(StringIO(self.WIGI_NEW))
    # Normalize columns
    df.columns = df.columns.str.strip().str.upper()
    org_field = "ORGANIZATION CD"
    sort_field = "WGI DATE"
    office_codes = self.office_code_map[self.office]
    stripped_office_codes = [value[2:] for value in office_codes]
    df[org_field] = df[org_field].astype(str).str.strip()
    df_filtered = df[df[org_field].isin(stripped_office_codes)]
    df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
    self.WIGI_Filtered_New = self.df_to_csv_string(df_filtered)
    # print(self.WIGI_Filtered_Old.splitlines()[:5])
  
  def build_new_clp_report(self):
    df_old = pd.read_csv(StringIO(self.CLP_OLD))
    df_new = pd.read_csv(StringIO(self.CLP_Filtered_New))
    # Normalize headers
    df_old = self.normalize_columns(df_old)
    df_new = self.normalize_columns(df_new)
    # Keep only the columns we need from the old file
    df_old_reduced = df_old[["EMPLOYEE_NAME", "NOTES"]]
    # Merge on the name column(s)
    df_merged = df_new.merge(
        df_old_reduced,
        on="EMPLOYEE_NAME",
        how="left"
    )
    cols = ["NOTES"] + [c for c in df_merged.columns if c != "NOTES"]
    df_merged = df_merged[cols]
    self.clp_with_notes_final = self.df_to_csv_string(df_merged)
  
  def build_new_EXC_report(self):
    df_old = pd.read_csv(StringIO(self.EXC_OLD))
    df_new = pd.read_csv(StringIO(self.EXC_Filtered_New))
    # Normalize headers
    df_old = self.normalize_columns(df_old)
    df_new = self.normalize_columns(df_new)
    # print("OLD columns:", df_old.columns.tolist())
    # print("NEW columns:", df_new.columns.tolist())
    # input()
    # Keep only the columns we need from the old file
    df_old_reduced = df_old[["EMPLOYEE_NAME", "NOTES"]]
    # Merge on the name column(s)
    df_merged = df_new.merge(
        df_old_reduced,
        on="EMPLOYEE_NAME",
        how="left"
    )
    cols = ["NOTES"] + [c for c in df_merged.columns if c != "NOTES"]
    df_merged = df_merged[cols]
    # Save result
    self.exc_with_notes_final = self.df_to_csv_string(df_merged)
  
  def build_final_report(self):
    # Read CSVs
    df_clp = pd.read_csv(StringIO(self.clp_with_notes_final))
    df_exc = pd.read_csv(StringIO(self.exc_with_notes_final))
    df_wigi = pd.read_csv(StringIO(self.WIGI_Filtered_New))
    office = self.office
    month = self.month
    # Default filename suggestion
    default_name = f"{office}_{month}_Monthly_report.xlsx"
    # Ask user where to save
    output_excel = filedialog.asksaveasfilename(
        title="Save Monthly Report",
        defaultextension=".xlsx",
        initialfile=default_name,
        filetypes=[("Excel Files", "*.xlsx")]
    )
    print('HERE')
    input()
    # User clicked Cancel
    if not output_excel:
        return
    # Write all three sheets into one Excel file
    try:
        with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
            df_clp.to_excel(writer, sheet_name="CLP", index=False)
            df_exc.to_excel(writer, sheet_name="EXC", index=False)
            df_wigi.to_excel(writer, sheet_name="WIGI", index=False)

        messagebox.showinfo(
            "Success",
            f"Report saved successfully:\n{output_excel}"
        )
    except Exception as e:
        messagebox.showerror(
            "Save Failed",
            f"Could not save report:\n{e}"
        )


  # The methods below here are support methods...maybe one day move to another class...
  # This method is for the JSON file. 
  def load_office_codes(self):
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
  
  # This method will make all the column names the same. 
  def normalize_columns(self, df):
    df.columns = (
        df.columns
        .str.strip()
        .str.upper()
        .str.replace(" ", "_")
    )
    return df




root = Tk() 
my_app = ReportGui(root)
root.mainloop()