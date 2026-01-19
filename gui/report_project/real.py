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
			'./new_month_report/new_report.xlsx',
			sheet_name=None,
			engine='openpyxl'
		)
		self.CLP_DF = self.monthly_report["CLP"]
		self.EXC_DF = self.monthly_report["EXC"]
		self.WIGI_DF = self.monthly_report["WIGI"]
		self.csv_folder = './csv_holding_area/'
		config_path = "./office_codes/offices_and_codes.json"
		if not os.path.exists(config_path):
			raise FileNotFoundError(f"Config file not found: {config_path}")
		with open(config_path, "r") as f: 
			self.office_codes = json.load(f)
		self.selected_office = ""
		self.selected_month = ""
	
	def program_starting(self):
		print('Program now starting')
	
	def select_office_and_month(self):
		self.selected_office = input("Please enter what office you want report built for: ")
		self.selected_month = input("Please enter what month the report is for: ")
	
	def export_all_sheets_to_csv(self): #DONE 
		for sheet_name, df in self.monthly_report.items():
			csv_path = os.path.join(self.csv_folder, f"{sheet_name}.csv")
			df.to_csv(csv_path, index=False)
	
	def filter_clps_by_office(self): # Working 
		clp_path = os.path.join(self.csv_folder, "CLP.csv")
		df = pd.read_csv(clp_path, dtype=str)
		df.columns = df.columns.str.strip().str.upper()
		org_field = "ORG CODE"
		sort_field = "ENTER PRES GR"
		df_filtered = df[df[org_field].isin(self.office_codes[self.selected_office])]
		df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
		office = self.selected_office
		csv_path = os.path.join(self.csv_folder, f"{office}_CLP.csv")
		df_filtered.to_csv(csv_path, index=False)
	
	def filter_EXC_by_office(self):
		exc_path = os.path.join(self.csv_folder, "EXC.csv")
		df = pd.read_csv(exc_path, dtype=str)
		df.columns = df.columns.str.strip().str.upper()
		org_field = "ORG_CODE"
		sort_field = "APPNT EFF DATE"
		df_filtered = df[df[org_field].isin(self.office_codes[self.selected_office])]
		df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
		office = self.selected_office
		csv_path = os.path.join(self.csv_folder, f"{office}_EXC.csv")
		df_filtered.to_csv(csv_path, index=False)

	def filter_WIGI_by_office(self):
		office = self.selected_office
		wigi_path = os.path.join(self.csv_folder, "WIGI.csv")
		df = pd.read_csv(wigi_path, dtype=str)
		org_field = "Organization Cd"
		sort_field = "WGI DATE"
		stripped_office_codes = [code[2:] for code in self.office_codes[office]]
		# Normalize the WIGI org code to be a clean string (strip, zero-pad to match length)
		df[org_field] = (
			df[org_field]
			.astype(str)
			.str.strip()
			.str.zfill(len(stripped_office_codes[0]))   # ensures "2" becomes "02"
		)
		# Also normalize your office codes the same way
		stripped_office_codes = [
			code.zfill(len(stripped_office_codes[0])) for code in stripped_office_codes
    	]
		df_filtered = df[df[org_field].isin(stripped_office_codes)]
		df_filtered = df_filtered.sort_values(by=sort_field, ascending=True)
		office = self.selected_office
		csv_path = os.path.join(self.csv_folder, f"{office}_WIGI.csv")
		df_filtered.to_csv(csv_path, index=False)

	def get_old_month_report(self):
		office = self.selected_office
		excel_path = f'./Old_Month_Report/{office}_Old_report.xlsx'
		old_monthly_report = pd.read_excel(
			f'./Old_Month_Report/{office}_Old_report.xlsx',
			sheet_name=None,
			engine='openpyxl'
		)
		# Loop through each sheet and export
		for sheet_name, df in old_monthly_report.items():
			#df.columns = df.columns.str.strip().str.upper()
			df.columns = df.columns.astype(str).str.strip().str.upper()
			csv_filename = f"{office}_old_{sheet_name}.csv"
			csv_path = os.path.join(self.csv_folder, csv_filename)
			df.to_csv(csv_path, index=False)
	
	def build_new_clp_report(self):
		import pandas as pd 
		from pandas.errors import EmptyDataError

		def safe_read_csv(path):
			try: 
				return pd.read_csv(path, dtype=str)
			except EmptyDataError:
				return pd.DataFrame()
		office = self.selected_office
		#load both CSV's 
		old_clp_path = os.path.join(self.csv_folder, f"{office}_old_CLP.csv")
		new_clp_path = os.path.join(self.csv_folder, f"{office}_CLP.csv")
		df_old = pd.read_csv(old_clp_path, dtype=str)
		df_new = pd.read_csv(new_clp_path, dtype=str)
		if df_new.empty: 
			df_new.to_csv(os.path.join(self.csv_folder, f"{office}_MERGED_CLP.csv"), index=False)
			return
		df_old.columns = df_old.columns.str.strip().str.upper()
		df_new.columns = df_new.columns.str.strip().str.upper()
		if "EMPLOYEE NAME" not in df_old.columns: 
			df_old["EMPLOYEE NAME"] = ""
		if "NOTES" not in df_old.columns:
			df_old["NOTES"] = ""
		if "EMPLOYEE NAME" not in df_new.columns:
			df_new["EMPLOYEE NAME"] = ""
		df_old_reduced = df_old[["EMPLOYEE NAME", "NOTES"]]
		df_merged = df_new.merge(
			df_old_reduced,
			on="EMPLOYEE NAME",
			how="left"
		)
		cols = ["NOTES"] + [c for c in df_merged.columns if c != "NOTES"]
		df_merged = df_merged[cols]
		# Save Result 
		csv_path = os.path.join(self.csv_folder, f"{office}_MERGED_CLP.csv")
		df_merged.to_csv(csv_path, index=False)
	
	def build_new_EXC_report(self):
		import pandas as pd 
		from pandas.errors import EmptyDataError

		def safe_read_csv(path):
			try: 
				return pd.read_csv(path, dtype=str)
			except EmptyDataError:
				return pd.DataFrame()
		office = self.selected_office
		old_EXC_path = os.path.join(self.csv_folder, f"{office}_old_EXC.csv")
		new_EXC_path = os.path.join(self.csv_folder, f"{office}_EXC.csv")
		df_old = pd.read_csv(old_EXC_path, dtype=str)
		df_new = pd.read_csv(new_EXC_path, dtype=str)
		if df_new.empty: 
			df_new.to_csv(os.path.join(self.csv_folder, f"{office}_MERGED_EXC.csv"), index=False)
			return
		df_old.columns = df_old.columns.str.strip().str.upper()
		df_new.columns = df_new.columns.str.strip().str.upper()
		if "EMPLOYEE NAME" not in df_old.columns: 
			df_old["EMPLOYEE NAME"] = ""
		if "NOTES" not in df_old.columns:
			df_old["NOTES"] = ""
		if "EMPLOYEE NAME" not in df_new.columns:
			df_new["EMPLOYEE NAME"] = ""
		df_old_reduced = df_old[["EMPLOYEE NAME", "NOTES"]]
		df_merged = df_new.merge(
			df_old_reduced,
			on="EMPLOYEE NAME",
			how="left"
		)
		cols = ["NOTES"] + [c for c in df_merged.columns if c != "NOTES"]
		df_merged = df_merged[cols]
		csv_path = os.path.join(self.csv_folder, f"{office}_MERGED_EXC.csv")
		df_merged.to_csv(csv_path, index=False)
	
	def build_final_report(self): 
		office = self.selected_office
		month = self.selected_month
		clp_path = os.path.join(self.csv_folder, f"{office}_MERGED_CLP.csv")
		exc_path = os.path.join(self.csv_folder, f"{office}_MERGED_EXC.csv")
		wigi_path = os.path.join(self.csv_folder, f"{office}_WIGI.csv")
		df_clp = pd.read_csv(clp_path, dtype=str)
		df_exc = pd.read_csv(exc_path, dtype=str)
		df_wigi = pd.read_csv(wigi_path, dtype=str)
		output_excel = os.path.join(self.csv_folder, f"{office}_{month}_Monthly_Report.xlsx")
		with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
			df_clp.to_excel(writer, sheet_name="CLP", index=False)
			df_exc.to_excel(writer, sheet_name="EXC", index=False)
			df_wigi.to_excel(writer, sheet_name="WIGI", index=False)
	
	def delete_all_csv_files(self):
		csv_files = glob.glob(os.path.join(self.csv_folder, "*.csv"))
		for file in csv_files: 
			try: 
				os.remove(file)
			except Exception as e: 
				print(f"Could not delete {file}: {e}")
		print("All CSV files deleted!")
		print("Program Done!")


report_object = Reports()
report_object.program_starting()
report_object.select_office_and_month()
report_object.export_all_sheets_to_csv()
report_object.filter_clps_by_office()
report_object.filter_EXC_by_office()
report_object.filter_WIGI_by_office()
report_object.get_old_month_report()
report_object.build_new_clp_report() 
report_object.build_new_EXC_report()
report_object.build_final_report()
report_object.delete_all_csv_files()