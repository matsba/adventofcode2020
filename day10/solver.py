import sys
sys.path.append("..")
from helpers import read_csv

def get_input_data(source="input"):
	if source == "test":
		return [
			"16",
			"10",
			"15",
			"5",
			"1",
			"11",
			"7",
			"19",
			"6",
			"12",
			"4"
		]
	else:
		return read_csv.file_read_lines("input.csv")
		
def main():
	print("What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?")
	adapters = list(map(int, get_input_data("test")))
	default_adapter = 3
	charging_outlet = 0
	current_jolts = charging_outlet
	one_jolt_differences = []
	three_jolt_differences = []
	combinations = []

	adapters.sort()


	combination = []
	for i in range(0, len(adapters)):
		adapter_under_inspection = int(adapters[i])
		if adapter_under_inspection - current_jolts == 1:
			one_jolt_differences.append(adapter_under_inspection)
			combination.append(adapter_under_inspection)

		if adapter_under_inspection - current_jolts == 2:
			combination.append(adapter_under_inspection)

		if adapter_under_inspection - current_jolts == 3:
			three_jolt_differences.append(adapter_under_inspection)
			combination.append(adapter_under_inspection)

		current_jolts = adapter_under_inspection

	combinations.append(combination)
	
	print(combinations)
	three_jolt_differences.append(current_jolts + default_adapter)

	answer_to_part_1 = len(one_jolt_differences) * len(three_jolt_differences)

	print(f"There are {len(one_jolt_differences)} 1-jolt and {len(three_jolt_differences)} 3-jolt differences, which gives the answer of {answer_to_part_1}")
		
	print("What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?")
	print(f"There are {len(combinations)} different combinations to arrange adapters to")
	
main()