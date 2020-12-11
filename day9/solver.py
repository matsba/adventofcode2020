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
	#print(arr)
	for item in arr:
		#print(f"Summing {num} with {item}")
		r_arr.add(int(num) + int(item))
	return r_arr

def summed_set(arr):
	summed = set()
	for num in arr:
		summed.update(sum_with_list(num, arr))
	return summed

def sum_of_numbers_in_arr(arr):
	summed = 0
	for item in arr:
		summed += int(item)
	return summed

def is_valid_value(arr, num_to_find):
	if num_to_find not in summed_set(arr):
		return False
	else:
		return True

def smallest_numbers_in_set(compare_set, to_set):
	compare_set.sort()
	to_set.sort()
	if int(compare_set[0]) + int(compare_set[-1]) < int(to_set[0]) + int(to_set[-1]):
		return True
	else:
		return False

def smaller_and_larger_numbers(compare_set, to_set):
	compare_set.sort()
	to_set.sort()
	if int(compare_set[0]) < int(to_set[0]) and int(compare_set[-1]) > int(to_set[-1]):
		return True
	else:
		return False

def shorter_set(compare_set, to_set):
	return len(compare_set) < len(to_set)

def find_weak_set(arr, weakness):
	best_test_range = None
	j = 0
	while j < len(arr):
		i = j + 1
		while i < len(arr):
			test_range = arr[j:i]
			#print(f"Testing {test_range}")
			if len(test_range) > 1:
				if weakness == sum_of_numbers_in_arr(test_range):
					if best_test_range is None or smaller_and_larger_numbers(test_range, best_test_range): # (smaller_numbers_in_set(test_range, best_test_range) and shorter_set(test_range, best_test_range)):
						best_test_range = test_range
					else:
						break
			i += 1
		j += 1
	best_test_range.sort()
	return best_test_range

def find_invalid_value(arr, preamble):

	i = 0
	while i < len(arr):
		if (i + preamble) > len(arr):
			break
		current_num = int(arr[i + preamble])
		previous_nums = arr[i:i + preamble]
		if not is_valid_value(previous_nums, current_num):
			return current_num
		else:
			i += 1
	
	print("No invalid values")
	return -1

def main():
	print("The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?")
	data = get_input_data()
	preamble = 25

	invalid_value = find_invalid_value(data, preamble)
	print(f"Number that does not follow this rule is {invalid_value}")

	if invalid_value != -1:
		weak_set = find_weak_set(data, invalid_value)
		if weak_set:
			print(weak_set)
			answer = int(weak_set[0]) + int(weak_set[-1])
		else:
			answer = "not found"

	print(f"Encryption weakness in XMAS-encrypted list of numbers is {answer}")
	
main()