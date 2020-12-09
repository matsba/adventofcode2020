import sys
sys.path.append("..")
from helpers import read_csv

def get_pattern():
	input_file = read_csv.file_read_lines("input.csv")
	travel_path = []

	#extend base pattern
	for row in input_file:
		travel_path.append(''.join([row for s in range(len(input_file))]))

	return travel_path

def get_test_pattern():
	return [	"..##.........##.........##.........##.........##.........##.......",
				"#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..",
				".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.",
				"..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#",
				".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.",
				"..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....",
				".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#",
				".#........#.#........#.#........#.#........#.#........#.#........#",
				"#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...",
				"#...##....##...##....##...##....##...##....##...##....##...##....#",
				".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"]

def part_1():
	print("Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?")
	travel_path = get_pattern()

	current_pos_right = 1
	current_pos_down = 0
	trees_encountered = 0

	while True:
		#break loop if hit end of the pattern
		if current_pos_right + 3 > len(travel_path[current_pos_down]) or current_pos_down + 1 > len(travel_path) -1:
			break

		#move right 3 spaces and get the elements in path
		current_pos_right += 3
		path_to_right = travel_path[current_pos_down][current_pos_right:current_pos_right + 3]		

		#move down 1 space and get the elements in that spot
		current_pos_down += 1
		path_down = travel_path[current_pos_down][current_pos_right-1]

		if path_down == "#":
			trees_encountered += 1

	print(f"Encountered {trees_encountered} in path")

def part_2():
	print("What do you get if you multiply together the number of trees encountered on each of the listed slopes?")
	travel_path = get_pattern()

	patterns = [{ "right": 1, "down": 1 },
				{ "right": 3, "down": 1 },
				{ "right": 5, "down": 1 },
				{ "right": 7, "down": 1 },
				{ "right": 1, "down": 2 }]

	multiplied_trees_encountered = 1

	for pattern in patterns:
		current_pos_right = 0
		current_pos_down = 0
		trees_encountered = 0

		while True:
			#break loop if hit end of the pattern
			if current_pos_right + pattern["right"] > len(travel_path[current_pos_down]) -1 or current_pos_down + pattern["down"] > len(travel_path) -1:
				break

			#move right spaces
			current_pos_right += pattern["right"]

			#move down 1 space and get the elements in that spot
			current_pos_down += pattern["down"]
			path_down = travel_path[current_pos_down][current_pos_right]

			if path_down == "#":
				trees_encountered += 1
		
		print(f"Encountered {trees_encountered} in path")
		multiplied_trees_encountered = multiplied_trees_encountered * trees_encountered

	print(f"Multipied encountered tree {multiplied_trees_encountered} in path")

#part_1()
part_2()