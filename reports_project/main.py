# This project will focus on how to take csv files, filter them for data and then bring 
# them back together to make one excel file. 

# importing supporting libraries
import pandas as pd
import os
import json
import glob

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
    df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
    office = self.selected_office
    csv_path = os.path.join(self.csv_folder, f"{office}_EXC.csv")
    df_filtered.to_csv(csv_path, index=False)

  def filter_WIGI_by_office(self):
    office = self.selected_office
    #NEED TO ADD CODE to STRIP OUT THE CI
    wigi_path = os.path.join(self.csv_folder, "WIGI.csv")
    df = pd.read_csv(wigi_path, dtype=str)
    org_field = "Organization Cd"
    sort_field = "WGI DATE"
    stripped_office_code = self.office_codes[office] = [value[2:] for value in self.office_codes[office]]
    df_filtered = df[df[org_field].isin(stripped_office_code)]
    df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
    office = self.selected_office
    csv_path = os.path.join(self.csv_folder, f"{office}_WIGI.csv")
    df_filtered.to_csv(csv_path, index=False)
  
  def get_old_month_report(self):
    print('here!')
    input()
    office = self.selected_office
    excel_path = f'./Old_Month_Report/{office}_Old_report.xlsx'
    old_monthly_report = pd.read_excel(
        f'./Old_Month_Report/{office}_Old_report.xlsx',
        sheet_name=None,
        engine='openpyxl'
    )
    # Loop through each sheet and export
    for sheet_name, df in old_monthly_report.items():
        csv_filename = f"{office}_old_{sheet_name}.csv"
        csv_path = os.path.join(self.csv_folder, csv_filename)
        df.to_csv(csv_path, index=False)
  
  def build_new_clp_report(self):
    office = self.selected_office
    # Load both CSVs
    old_clp_path = os.path.join(self.csv_folder, f"{office}_old_CLP.csv")
    new_clp_path = os.path.join(self.csv_folder, f"{office}_CLP.csv")
    df_old = pd.read_csv(old_clp_path, dtype=str)
    df_new = pd.read_csv(new_clp_path, dtype=str)
    # Keep only the columns we need from the old file
    df_old_reduced = df_old[["EMPLOYEE NAME", "Notes"]]
    # Merge on the name column(s)
    # Merge NOTES into the new CLP file
    df_merged = df_new.merge(
        df_old_reduced,
        on="EMPLOYEE NAME",
        how="left"
    )
    cols = ["Notes"] + [c for c in df_merged.columns if c != "Notes"]
    df_merged = df_merged[cols]
    # Save result
    csv_path = os.path.join(self.csv_folder, f"{office}_MERGED_CLP.csv")
    df_merged.to_csv(csv_path, index=False)
  
  def build_new_EXC_report(self):
    office = self.selected_office
    # Load both CSVs
    old_EXC_path = os.path.join(self.csv_folder, f"{office}_old_EXC.csv")
    new_EXC_path = os.path.join(self.csv_folder, f"{office}_EXC.csv")
    df_old = pd.read_csv(old_EXC_path, dtype=str)
    df_new = pd.read_csv(new_EXC_path, dtype=str)
    # Keep only the columns we need from the old file
    df_old_reduced = df_old[["Employee Name", "Notes"]]
    # Merge on the name column(s)
    # Merge NOTES into the new CLP file
    df_merged = df_new.merge(
        df_old_reduced,
        on="Employee Name",
        how="left"
    )
    cols = ["Notes"] + [c for c in df_merged.columns if c != "Notes"]
    df_merged = df_merged[cols]
    # Save result
    csv_path = os.path.join(self.csv_folder, f"{office}_MERGED_EXC.csv")
    df_merged.to_csv(csv_path, index=False)
    
  def build_final_report(self):
    office = self.selected_office
    # File paths
    clp_path = os.path.join(self.csv_folder, f"{office}_MERGED_CLP.csv")
    exc_path = os.path.join(self.csv_folder, f"{office}_MERGED_EXC.csv")
    wigi_path = os.path.join(self.csv_folder, f"{office}_WIGI.csv")
    # Read CSVs
    df_clp = pd.read_csv(clp_path, dtype=str)
    df_exc = pd.read_csv(exc_path, dtype=str)
    df_wigi = pd.read_csv(wigi_path, dtype=str)
    # Output Excel path
    output_excel = os.path.join(self.csv_folder, "FINAL_REPORT.xlsx")
    # Write all three sheets into one Excel file
    with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
        df_clp.to_excel(writer, sheet_name="CLP", index=False)
        df_exc.to_excel(writer, sheet_name="EXC", index=False)
        df_wigi.to_excel(writer, sheet_name="WIGI", index=False)

  def delete_all_csv_files(self):
    # Find all CSV files in the folder
    csv_files = glob.glob(os.path.join(self.csv_folder, "*.csv"))
    for file in csv_files:
        try:
            os.remove(file)
        except Exception as e:
            print(f"Could not delete {file}: {e}")
    print("All CSV files deleted.")

  
report_object = Reports()
report_object.program_starting()
report_object.select_office()
report_object.export_all_sheets_to_csv()
report_object.filter_clps_by_office()
report_object.filter_EXC_by_office()
report_object.filter_WIGI_by_office()
report_object.get_old_month_report()
report_object.build_new_clp_report() 
report_object.build_new_EXC_report()
report_object.build_final_report()
report_object.delete_all_csv_files()

