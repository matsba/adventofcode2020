print("How many passwords are valid according to their policies?")

def file_read_lines(file_name):
	input_arr = []
	with open(file_name, "r") as file:
		for line in file:
			input_arr.append(line.rstrip("\n"))
	return input_arr

def parse_policy_and_password(line):
	#partion line into policy and password 
	#lines are in format: 1-4 n: nnnnn
	partition = line.partition(":")

	#split policy to min requirement and the required character
	splitted = partition[0].split("-")
	required_min_count = splitted[0]
	required_max_count = splitted[1].split(" ")[0]
	required_char = partition[0][-1]

	#get password from partition and remove unneccacery white space
	password = partition[2].strip(" ")

	return {"required_min_count": int(required_min_count), "required_max_count": int(required_max_count), "required_char": required_char, "password": password}

def is_valid_password(input_dict):
	#check how many times password contains the required char
	count_of_required_char = input_dict["password"].count(input_dict["required_char"])

	#and compare it to the min and max requirements
	required_min_amount = count_of_required_char >= input_dict["required_min_count"]
	required_max_amount = count_of_required_char <= input_dict["required_max_count"]

	if required_min_amount and required_max_amount:
		return True
	else:
		return False

passwords = file_read_lines("input.csv")
valid_password_count = 0
for password in passwords:
	#dubug
	#print(f"Password policy dict: {parse_policy_and_password(password)}")
	#print(f"{password} is valid: {is_valid_password(parse_policy_and_password(password))}")
	if is_valid_password(parse_policy_and_password(password)):
		valid_password_count += 1

print(f"There are {len(passwords)} password from which {valid_password_count} are valid passwords")

