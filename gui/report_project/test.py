import os
import json

def file():
    config_path = os.path.join(os.getcwd(), "./office_codes/offices_and_codes.json")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror(
            "Missing Configuration",
            "office_codes.json not found.\nThe application cannot continue."
        )

test_file = file()
for t in test_file:
    print(t)


