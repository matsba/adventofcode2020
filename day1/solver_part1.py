input_arr = []

print("find the two entries that sum to 2020 and then multiply those two numbers together.")

with open("input.csv", "r") as file:
    for line in file:
        input_arr.append(int(line.rstrip("\n")))

for value in input_arr:
	for other_value in input_arr:
		if value + other_value == 2020:
			print(f'{value} + {other_value} = 2020, which means the correct answer is {value * other_value}')
			break
	else:
		continue

	break