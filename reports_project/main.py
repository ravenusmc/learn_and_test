# This project will focus on how to take csv files, filter them for data and then bring 
# them back together to make one excel file. 

# importing supporting libraries
import pandas as pd
import os

class Reports():

  def __init__(self):
    self.monthly_report = pd.read_excel(
        './new_month_report/Oct_monthly.xlsx',
        sheet_name=None,
        engine='openpyxl'
    )
    self.CLP_DF = self.monthly_report["CLP"]
    self.EXC_DF = self.monthly_report["EXC"]
    self.WIGI_DF = self.monthly_report["WGI"]
    self.csv_folder = './csv_holding_area'

  def program_starting(self):
    print('Program Now Starting...')
  
  def export_all_sheets_to_csv(self):
    for sheet_name, df in self.monthly_report.items():
        # Build the full file path inside the folder
        csv_path = os.path.join(self.csv_folder, f"{sheet_name}.csv")
        df.to_csv(csv_path, index=False)
        print(f"Saved {csv_path}")
  
  def filter_clps_by_office(self):
    pass



report_object = Reports()
report_object.program_starting()
report_object.export_all_sheets_to_csv()


