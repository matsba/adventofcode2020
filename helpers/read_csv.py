def file_read_lines(file_name, remove_dulicates=False):
	input_arr = []
	with open(file_name, "r") as file:
		for line in file:
			input_arr.append(line.rstrip("\n"))

	if remove_dulicates:
		return remove_duplicates(input_arr)
	return input_arr

def remove_duplicates(arr):
  	return list(dict.fromkeys(arr))
