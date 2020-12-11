import sys
sys.path.append("..")
from helpers import read_csv

def get_input_data(source="input"):
	if source == "test":
		return []
	else:
		return read_csv.file_read_lines("input.csv")
		
def main():
	
main()