import sys
sys.path.append("..")
from helpers import read_csv

def get_input_data(source="input"):
	if source == "test":
		return [
			"L.LL.LL.LL",
			"LLLLLLL.LL",
			"L.L.L..L..",
			"LLLL.LL.LL",
			"L.LL.LL.LL",
			"L.LLLLL.LL",
			"..L.L.....",
			"LLLLLLLLLL",
			"L.LLLLLL.L",
			"L.LLLLL.LL"
		]
	else:
		return read_csv.file_read_lines("input.csv")

def get_adjacent_seats(seat, seat_index, row_index, all_rows):

	x = seat_index
	y = row_index
	max_x = len(all_rows[row_index]) - 1
	max_y = len(all_rows) - 1

	adjacent = ""

	is_top_row = y == 0
	is_bottom_row = y == max_y
	is_first_seat = x == 0
	is_last_seat = x == max_x
	
	top_row = None
	current_row = all_rows[row_index]
	bottom_row = None

	range_first = x - 2 if x > 1 else 0
	range_last = x + 2 if x + 2 <= max_x else max_x

	if is_first_seat:
		seat_range = slice(x, range_last)
	elif is_last_seat:
		seat_range = slice(range_first, x)
	else:
		seat_range = slice(range_first, range_last)

	#if its top row, only get current row and one bottom of it
	if is_top_row:
		bottom_row = all_rows[y + 1]

		adjacent += current_row[seat_range]
		adjacent += bottom_row[seat_range]

	#if its bottom row, get top and current rows
	elif is_bottom_row:
		top_row = all_rows[y - 1]

		adjacent += top_row[seat_range]
		adjacent += current_row[seat_range]
	
	#else get surrounding seats
	else:
		top_row = all_rows[y - 1]
		bottom_row = all_rows[y + 1]

		adjacent += bottom_row[seat_range]
		adjacent += current_row[seat_range]
		adjacent += top_row[seat_range]		

	#remove current seat
	adjacent = adjacent.replace(seat, "", 1)

	return adjacent

def main():
	print("Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?")
	seating = get_input_data("test")

	empty = "L"
	occupied = "#"
	floor = "."

	repeated = False
	previous_seating = seating
	new_seating = []

	while not repeated:
		if "".join(new_seating) is "".join(previous_seating):
			break
		if new_seating:
			previous_seating = new_seating

		new_seating = []

		for j in range(0, len(previous_seating)):
			row = previous_seating[j]
			new_row = ""
			#print(f"Row is {row}")

			for i in range(0, len(row)):
				seat = row[i]
				adjacent = get_adjacent_seats(seat, i, j, previous_seating)
				#print(f"Seat is {i}. {seat} and has adjacent {adjacent}")	

				if seat is empty and occupied not in adjacent:
					new_row += occupied
				elif seat is occupied and adjacent.count(occupied) >= 4:
					new_row += empty
				else:
					new_row += seat
			
			new_seating.append(new_row)

		print("")
		print("NEW SEATING")
		print("")

		for row in new_seating:
			print(row)

						

	answer = previous_seating.count(empty)

	print(f"There are {answer} occupied seats")
main()