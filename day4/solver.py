import sys
sys.path.append("..")
from helpers import read_csv
import re

def get_input_data(source="input"):
	if source == "test":
		return ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
				"byr:1937 iyr:2017 cid:147 hgt:183cm",
				"",
				"iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
				"hcl:#cfa07d byr:1929",
				"",
				"hcl:#ae17e1 iyr:2013",
				"eyr:2024",
				"ecl:brn pid:760753108 byr:1931",
				"hgt:179cm",
				"",
				"hcl:#cfa07d eyr:2025 pid:166559648",
				"iyr:2011 ecl:brn hgt:59in"]
	elif source == "test2":
		return ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
				"byr:1937 iyr:2017 cid:147 hgt:183cm",
				"",
				"iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
				"hcl:#cfa07d byr:1929",
				"",
				"hcl:#ae17e1 iyr:2013",
				"eyr:2024",
				"ecl:brn pid:760753108 byr:1931",
				"hgt:179cm",
				"",
				"hcl:#cfa07d eyr:2025 pid:166559648",
				"iyr:2011 ecl:brn hgt:59in",
				"",
				"iyr:2010 hgt:158cm hcl:#b6652a ecl:grn byr:2003 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:158cm hcl:#b6652a ecl:grn byr:2002 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:60in hcl:#b6652a ecl:grn byr:1944 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:190cm hcl:#b6652a ecl:grn byr:1944 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:190in hcl:#b6652a ecl:grn byr:1944 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:190 hcl:#b6652a ecl:grn byr:1944 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:158cm hcl:#123abc ecl:grn byr:1944 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:158cm hcl:#123abz ecl:grn byr:1944 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:158cm hcl:123abc ecl:grn byr:1944 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:158cm hcl:#b6652a ecl:brn byr:1944 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:158cm hcl:#b6652a ecl:wat byr:1944 eyr:2021 pid:093154719",
				"",
				"iyr:2010 hgt:158cm hcl:#b6652a ecl:grn byr:1944 eyr:2021 pid:000000001",
				"",
				"iyr:2010 hgt:158cm hcl:#b6652a ecl:grn byr:1944 eyr:2021 pid:0123456789"]
	else:
		return read_csv.file_read_lines("input.csv")

def passport_parser(data):
	passport_dict = {}
	fields = data.split()
	for field in fields:
		seperated = field.split(":")
		if seperated[0] == "byr":
			seperated[1] = int(seperated[1])
		if seperated[0] == "iyr":
			seperated[1] = int(seperated[1])
		if seperated[0] == "eyr":
			seperated[1] = int(seperated[1])
		passport_dict.update({seperated[0]:seperated[1]})
	return passport_dict

def is_valid_passport(passport_dict):
	required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

	""" byr (Birth Year) - four digits; at least 1920 and at most 2002.
		iyr (Issue Year) - four digits; at least 2010 and at most 2020.
		eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
		hgt (Height) - a number followed by either cm or in:
			If cm, the number must be at least 150 and at most 193.
			If in, the number must be at least 59 and at most 76.
		hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
		ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
		pid (Passport ID) - a nine-digit number, including leading zeroes.
		cid (Country ID) - ignored, missing or not.

		examples
		byr valid:   2002
		byr invalid: 2003

		hgt valid:   60in
		hgt valid:   190cm
		hgt invalid: 190in
		hgt invalid: 190

		hcl valid:   #123abc
		hcl invalid: #123abz
		hcl invalid: 123abc

		ecl valid:   brn
		ecl invalid: wat

		pid valid:   000000001
		pid invalid: 0123456789 """

	hair_color_pattern = "^#[0-9a-f]{6}$"
	pid_pattern = "^\d{9}$"
	height_pattern = "^\d*(cm|in)$"
	#ignored field
	passport_dict.pop("cid", None)
	keys_in_passport = list(passport_dict.keys())
	keys_in_passport.sort()
	required_fields.sort()

	if keys_in_passport != required_fields:
		#required fields not found
		#print("Not all required fields")
		return False
	
	if passport_dict["byr"] < 1920 or passport_dict["byr"] > 2002:
		#print("byr (Birth Year) - four digits; at least 1920 and at most 2002.")
		return False

	if passport_dict["iyr"] < 2010 or passport_dict["iyr"] > 2020:
		#print("iyr (Issue Year) - four digits; at least 2010 and at most 2020.")
		return False

	if passport_dict["eyr"] < 2020 or passport_dict["eyr"] > 2030:
		#print("eyr (Expiration Year) - four digits; at least 2020 and at most 2030.")
		return False

	if not re.match(height_pattern, passport_dict["hgt"]):
		#print("a number followed by either cm or in:")
		return False
	
	if passport_dict["hgt"].lower().endswith("cm"):
		end = passport_dict["hgt"].index('cm')
		height = int(passport_dict["hgt"][:end])
		if height < 150 or height > 193:
			#print("If cm, the number must be at least 150 and at most 193.")
			return False
	
	if passport_dict["hgt"].lower().endswith("in"):
		end = passport_dict["hgt"].index('in')
		height = int(passport_dict["hgt"][:end])
		if height < 59 or height > 76:
			#print("If in, the number must be at least 59 and at most 76.")
			return False

	if not re.match(hair_color_pattern, passport_dict["hcl"]):
		#print("hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.")
		return False

	if passport_dict["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
		#print("ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.")
		return False

	if not re.match(pid_pattern, passport_dict["pid"]):
		#print("pid (Passport ID) - a nine-digit number, including leading zeroes.")
		return False

	return True		 

def part_1():
	print("Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?")
	data = get_input_data()
	data.append("") #add end to determine passport last line

	required_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

	valid_passports = 0
	passport_data = ""
	total_number_of_passports = 0

	for line in data:
		#check if there is empty line where passport data ends and other begins
		if line == "" or line == "\n":
			#print(f"Analysing passport data: {passport_data}")
			#find occurances of required fields
			fields_found = 0
			for field in required_fields:
				found = passport_data.find(field)
				if found >= 0:
					fields_found += 1
				if fields_found == len(required_fields):
					#print(f"Valid passport data: {passport_data}")
					valid_passports += 1
					break
			total_number_of_passports += 1
			#print(f"{passport_data} is the {total_number_of_passports}. passport")
			passport_data = ""
		else:
			passport_data += line + " "
	
	print(f"There are {valid_passports} valid passports of {total_number_of_passports} ") 

def part_2():
	print("Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?")
	data = get_input_data()
	data.append("") #add end to determine passport last line

	valid_passports = 0
	passport_data = ""
	total_number_of_passports = 0

	for line in data:
		#check if there is empty line where passport data ends and other begins
		if line == "" or line == "\n":
			#print(f"Analysing passport data: {passport_data}")
			#print(passport_parser(passport_data))
			if is_valid_passport(passport_parser(passport_data)):
				valid_passports += 1
			total_number_of_passports += 1
			#print(f"{passport_data} is the {total_number_of_passports}. passport")
			passport_data = ""
		else:
			passport_data += line + " "
	
	print(f"There are {valid_passports} valid passports of {total_number_of_passports} ") 

part_1()
part_2()