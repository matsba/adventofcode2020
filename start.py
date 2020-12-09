import os
from datetime import datetime

code = """import sys
sys.path.append("..")
from helpers import read_csv

def get_input_data(source="input"):
	if source == "test":
		return []
	else:
		return read_csv.file_read_lines("input.csv")
		
def main():
	
main()"""

files = ["input.csv", "solver.py"]

for file in files:
	filename = f"./day{datetime.now().day}/{file}"

	if not os.path.exists(os.path.dirname(filename)):
		os.makedirs(os.path.dirname(filename))

	with open(filename, "w") as f:
		f.write("")
		if file == "solver.py":
			f.write(code)