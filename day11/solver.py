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

def get_seats_around(row, index, middle=False):
	adjacent_seats = ""

	if middle:
		if index == 0:
			adjacent_seats += row[index + 1]
		elif index + 1 > len(row) -1:
			adjacent_seats += row[index - 1]
		else:
			adjacent_seats += row[index - 1] + row[index + 1]
	else:
		if index == 0:
			adjacent_seats += row[index : index + 1]
		elif index + 1 > len(row) -1:
			adjacent_seats += row[index - 1 : index]
		else:		
			adjacent_seats += row[index - 1 : index + 1]

	return adjacent_seats

		
def get_adjent_seats(seat_index, row_index, all_rows):
	adjacent_seats = ""

	#no rows before
	if row_index is 0:
		middle_row = all_rows[row_index]
		bottom_row = all_rows[row_index + 1]

		adjacent_seats += get_seats_around(middle_row, seat_index, True)
		adjacent_seats += get_seats_around(bottom_row, seat_index)

	#no rows after
	elif row_index is len(all_rows) -1:
		top_row = all_rows[row_index - 1]
		middle_row = all_rows[row_index]

		adjacent_seats += get_seats_around(top_row, seat_index)
		adjacent_seats += get_seats_around(middle_row, seat_index, True)
	
	else:
		top_row = all_rows[row_index - 1]
		middle_row = all_rows[row_index]
		bottom_row = all_rows[row_index + 1]

		adjacent_seats += get_seats_around(top_row, seat_index)
		adjacent_seats += get_seats_around(middle_row, seat_index, True)
		adjacent_seats += get_seats_around(bottom_row, seat_index)

	return adjacent_seats

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

			for i in range(0, len(row)):
				seat = row[i]
				adjacent = get_adjent_seats(i, j, seating)
				#print(f"Seat is {seat} and has adjacent {adjacent}")			

				if seat is empty and occupied not in adjacent:
					new_row += occupied
				elif seat is occupied and adjacent.count(empty) > 3:
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