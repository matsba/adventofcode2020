import sys
sys.path.append("..")
from helpers import read_csv

def get_input_data(source="input"):
	if source == "test":
		return ["nop +0",
				"acc +1",
				"jmp +4",
				"acc +3",
				"jmp -3",
				"acc -99",
				"acc +1",
				"jmp -4",
				"acc +6"]
	else:
		return read_csv.file_read_lines("input.csv")

def main():
	print("Immediately before any instruction is executed a second time, what value is in the accumulator?")
	instructions = get_input_data("test")
	original_instructions = instructions.copy()
	accumulator  = 0
	i = 0
	run_times = 0
	jump_sum = 0
	after_infinite_loop = []
	accumulator_before_infinite_loop = 0 

	while i < len(instructions):
		run_times += 1
		print(f"{instructions[i]} | {run_times}")
		inst = instructions[i].split()

		if len(inst) > 2:
			loop_item = f"{inst[0]} {inst[1]}"
			if after_infinite_loop:
				accumulator_before_infinite_loop = accumulator
			
			if len(inst) > 3:
				infinite_loop = after_infinite_loop[1:]
				print("Loop started again!!!")
				print(f"The loop is {infinite_loop}")
				#change bad code
				middle = int((len(infinite_loop) - 1)/2)
				change = infinite_loop[middle]
				print(f"The loop was before going infinite: {original_instructions} and last index was {len(original_instructions)}")
				print(f"Fix this: {change}")
				break
			else:
				after_infinite_loop.append(loop_item)
			

		oper = inst[0]
		numb = int(inst[1])

		if "nop" in oper:
			instructions[i] = instructions[i] + " x"
			pass

		if "acc" in oper:
			instructions[i] = instructions[i] + " x"
			accumulator += numb
			pass

		if "jmp" in oper:
			# jump_sum += numb
			# if jump_sum == 0:
			# 	print(f"changed from {instructions[i]} to nop {numb}")
			# 	instructions[i] = f"nop {numb}"
			# 	continue

			instructions[i] = instructions[i] + " x"
			i += numb
			continue
		
		i += 1

	print(f"Immediately before the program would run an instruction a second time, the value in the accumulator is {accumulator}.")


main()