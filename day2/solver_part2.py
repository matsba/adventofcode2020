print("Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement. How many passwords are valid according to their policies?")

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
	required_first_placement = splitted[0]
	required_second_placement = splitted[1].split(" ")[0]
	required_char = partition[0][-1]

	#get password from partition and remove unneccacery white space
	password = partition[2].strip(" ")

	return {"required_first_placement": int(required_first_placement), "required_second_placement": int(required_second_placement), "required_char": required_char, "password": password}

def is_valid_password(input_dict):
	#check how many times password contains the required char
	if input_dict["required_char"] in input_dict["password"]:
		required_char_in_first_placement = input_dict["password"][-1 + input_dict["required_first_placement"]] == input_dict["required_char"]
		required_char_in_second_placement = input_dict["password"][-1 + input_dict["required_second_placement"]] == input_dict["required_char"]

		if (required_char_in_first_placement or required_char_in_second_placement) and not (required_char_in_first_placement and required_char_in_second_placement):
			return True
		else:
			return False
	else:
		return False

passwords = file_read_lines("input.csv")

#test ac
#passwords = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

valid_password_count = 0
for password in passwords:
	#dubug
	#print(f"Password policy dict: {parse_policy_and_password(password)}")
	#print(f"{password} is valid: {is_valid_password(parse_policy_and_password(password))}")
	if is_valid_password(parse_policy_and_password(password)):
		valid_password_count += 1

print(f"There are {len(passwords)} password from which {valid_password_count} are valid passwords")

