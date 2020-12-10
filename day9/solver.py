import sys
sys.path.append("..")
from helpers import read_csv

def get_input_data(source="input"):
	if source == "test":
		return ["35",
				"20",
				"15",
				"25",
				"47",
				"40",
				"62",
				"55",
				"65",
				"95",
				"102",
				"117",
				"150",
				"182",
				"127",
				"219",
				"299",
				"277",
				"309",
				"576"]
	else:
		return read_csv.file_read_lines("input.csv")

def sum_with_list(num, arr):
	r_arr = set()
	for item in arr:
		r_arr.add(int(num) + int(item))
	return r_arr

def is_valid_value(arr, num_to_find):
	summed = set()
	i = 1

	for num in arr:
		summed.update(sum_with_list(num, arr))

	print(summed)
	if num_to_find not in summed:
		return False

	return True

def main():
	print("The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?")
	data = get_input_data()
	preamble = 25

	i = 0
	while i < len(data):
		current_num = int(data[i + preamble + 1])
		previous_nums = data[i:i + preamble]
		if not is_valid_value(previous_nums, current_num):
			print(f"Number that does not follow this rule is {current_num}")
			break
		else:
			i += 1
main()