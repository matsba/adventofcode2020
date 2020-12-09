import sys
sys.path.append("..")
from helpers import read_csv
import re

def get_input_data(source="input"):
	if source == "test":
		#part 1: in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.
		# return ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
		# 		"dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
		# 		"bright white bags contain 1 shiny gold bag.",
		# 		"muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
		# 		"shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
		# 		"dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
		# 		"vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
		# 		"faded blue bags contain no other bags.",
		# 		"dotted black bags contain no other bags."]
		
		#part 2: So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!
		return ["shiny gold bags contain 2 dark red bags.",
				"dark red bags contain 2 dark orange bags.",
				"dark orange bags contain 2 dark yellow bags.",
				"dark yellow bags contain 2 dark green bags.",
				"dark green bags contain 2 dark blue bags.",
				"dark blue bags contain 2 dark violet bags.",
				"dark violet bags contain no other bags."]
	else:
		return read_csv.file_read_lines("input.csv")
		
def extract_rule(rule_str):
	container = rule_str.partition("bags")[0].strip()
	contains = []

	for bag in rule_str.partition("contain ")[2].split(","):
		bag = bag.strip()

		if "no other bags" in bag:
			break

		amount = re.findall("^\d+", bag)
		bag_type = re.findall("(?!\d+\s)\S.*\S(?= bag)", bag)
		contains.append({ "amount": int(amount[0]), "bag": bag_type[0] })
	
	return { "bag": container, "contains": contains }

def find_bags_containing(bag, bag_rules):
	bags_that_can_contain = []
	for rule in bag_rules:
		if rule["contains"]:
			for bags in rule["contains"]:
				if bags["bag"] == bag:
					bags_that_can_contain.append(rule["bag"])
					break				
	return bags_that_can_contain

def bags_contains(bag, bag_rules):
	for rule in bag_rules:
		if rule["bag"] == bag:
			return rule["contains"]

def main():
	print("How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)")

	data = get_input_data()
	rules = []
	bag_to_find = "shiny gold"

	for rule in data:
		rules.append(extract_rule(rule))

	next_arr = []
	next_arr.append(find_bags_containing(bag_to_find, rules))
	seen_bags = set()

	for bag_arr in next_arr:
		for bag in bag_arr:	
			seen_bags.add(bag)
			found = find_bags_containing(bag, rules)
			if found:
				next_arr.append(found)

	print(f"The number of bag colors that can eventually contain at least one {bag_to_find} bag is {len(seen_bags)}. ")

	# part 2
	print("How many individual bags are required inside your single shiny gold bag?")

	second_arr = []
	second_arr.append(bags_contains(bag_to_find, rules))
	bags_that_are_needed = 0

	print(f"second_arr: {second_arr}")

	for arr in second_arr:
		for item in arr:
			amount = item["amount"]
			bags_that_are_needed += amount

			next_bags = bags_contains(item["bag"], rules)
			next_bags_copy = []
			for next_bag in next_bags:
				copy = next_bag.copy() #dont reference the actual rule dictionary, use copy
				copy["amount"] = next_bag["amount"] * amount
				next_bags_copy.append(copy)

			second_arr.append(next_bags_copy)

	print(f"In this example, a single {bag_to_find} bag must contain {bags_that_are_needed} bags.")

main()