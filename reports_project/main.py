# This project will focus on how to take csv files, filter them for data and then bring 
# them back together to make one excel file. 

# importing supporting libraries
import pandas as pd
import os
import json

class Reports():

  def __init__(self):
    self.monthly_report = pd.read_excel(
        './new_month_report/new_report_1.xlsx',
        sheet_name=None,
        engine='openpyxl'
    )
    self.CLP_DF = self.monthly_report["CLP"]
    self.EXC_DF = self.monthly_report["EXC"]
    self.WIGI_DF = self.monthly_report["WIGI"]
    self.csv_folder = './csv_holding_area'
    config_path = "./office_codes/offices_and_codes.json"
    if not os.path.exists(config_path):
      raise FileNotFoundError(f"Config file not found: {config_path}")
    with open(config_path, "r") as f:
        self.office_codes = json.load(f)
    self.selected_office = ""

  def program_starting(self):
    print('Program Now Starting...')
  
  def select_office(self): 
    self.selected_office = input('Please enter what office you want report built for: ')
  
  def export_all_sheets_to_csv(self):
    for sheet_name, df in self.monthly_report.items():
        # Build the full file path inside the folder
        csv_path = os.path.join(self.csv_folder, f"{sheet_name}.csv")
        df.to_csv(csv_path, index=False)
        # print(f"Saved {csv_path}")
  
  def filter_clps_by_office(self):
    clp_path = os.path.join(self.csv_folder, "CLP.csv")
    df = pd.read_csv(clp_path, dtype=str)
    org_field = "ORG CODE"
    sort_field = "ENTER PRES GR"
    df_filtered = df[df[org_field].isin(self.office_codes[self.selected_office])]
    # Sort by Enter Pres GR
    df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
    office = self.selected_office
    csv_path = os.path.join(self.csv_folder, f"{office}_CLP.csv")
    df_filtered.to_csv(csv_path, index=False)
  
  def filter_EXC_by_office(self):
    exc_path = os.path.join(self.csv_folder, "EXC.csv")
    df = pd.read_csv(exc_path, dtype=str)
    org_field = "ORG_CODE"
    sort_field = "APPNT EFF DATE"
    df_filtered = df[df[org_field].isin(self.office_codes[self.selected_office])]
    # Sorting by the appointment field 
    df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
    office = self.selected_office
    csv_path = os.path.join(self.csv_folder, f"{office}_EXC.csv")
    print(csv_path)
    df_filtered.to_csv(csv_path, index=False)

  def filter_WIGI_by_office(self):
    pass

report_object = Reports()
report_object.program_starting()
report_object.select_office()
report_object.export_all_sheets_to_csv()
report_object.filter_clps_by_office()
report_object.filter_EXC_by_office()

