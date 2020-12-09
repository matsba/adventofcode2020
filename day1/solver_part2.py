input_arr = []

print("what is the product of the three entries that sum to 2020?")

with open("input.csv", "r") as file:
    for line in file:
        input_arr.append(int(line.rstrip("\n")))

for value in input_arr:
	for second_value in input_arr:
		for third_value in input_arr:
			if value + second_value + third_value == 2020:
				print(f'{value} + {second_value} + {third_value} = 2020, which means the correct answer is {value * second_value * third_value}')
				break
		else:
			continue

		break
	else:
		continue

	break