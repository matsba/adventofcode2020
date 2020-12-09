import sys
sys.path.append("..")
from helpers import read_csv

def get_input_data(source="input"):
	if source == "test":
		#part 1: in this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.
		#part 2 concnesus: the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.
		return ["abc",
				"",
				"a",
				"b",
				"c",
				"",
				"ab",
				"ac",
				"",
				"a",
				"a",
				"a",
				"a",
				"",
				"b",
				""]
	else:
		return read_csv.file_read_lines("input.csv")

def to_groups(data):
	groups = []
	group = []

	for row in data:
		if row != "" and row !="\n":
			group.append(row)
		else:
			groups.append(group)
			group = []
	return groups

def group_answers_count(group_str):
	#convert string to list of chars and make dict that has unique keys
	distinct_answers = list(dict.fromkeys((list(group_str))))
	return len(distinct_answers)

def group_concensus_answer_count(group_list):
	group_str = "".join(map(str, group_list))
	group_size = len(group_list)
	consensus_count = 0
	
	group_list.sort()
	shortest_answers_of_group = group_list[0]

	if group_size == 1:
		consensus_count = len(group_str)
	else:
		for answer in shortest_answers_of_group:
			if group_str.count(answer) == group_size:
				consensus_count += 1

	return consensus_count
		
def main():
	print("For each group, count the number of questions to which anyone answered 'yes'. What is the sum of those counts?")
	data = get_input_data()
	groups = to_groups(data)

	sum_of_answers = 0
	sum_of_concesus_in_groups = 0

	for group in groups:
		answer_count = group_answers_count("".join(map(str, group)))
		concensus_in_groups = group_concensus_answer_count(group)
		sum_of_answers += answer_count
		sum_of_concesus_in_groups += concensus_in_groups
	
	print(f"Sum of all {len(groups)} groups answers is {sum_of_answers} and group consensus sum is {sum_of_concesus_in_groups}")

main()