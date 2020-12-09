import sys
sys.path.append("..")
from helpers import read_csv

def get_input_data(source="input"):
	if source == "test":
		return ["BBFFFFBRRR", "BBFFFFFRRR", "FBFBBFFRLR","BFFFBBFRRR", "FFFBBBFRRR","BBFFBBFRLL"]
	else:
		return read_csv.file_read_lines("input.csv")

def valid_board_pass(board_pass):
	return len(board_pass) == 10

def half_board_pass(data, max_value):
	r = list(range(0, max_value+1))

	for letter in data:
		#print(f"Input letter: {letter}")
		half_index = int((len(r) -1)/2)+1
		if letter == "F" or letter == "L":
			r = r[:half_index]
		if letter == "B" or letter == "R":
			r = r[half_index:]
		#print(f"Output range: {r}")

	#print(r[0])
	return r[0]

def get_row(board_pass):
	max_rows = 127
	row_part_of_board_pass = board_pass[:7]
	return half_board_pass(row_part_of_board_pass, max_rows)

def get_column(board_pass):
	max_columns = 7
	column_part_of_board_pass = board_pass[7:]
	return half_board_pass(column_part_of_board_pass, max_columns)

def calculate_seat_id(row, column):
	return row * 8 + column

def find_my_seat(seat_ids):
	seat_ids.sort()
	missing = None

	for key, seat_id in enumerate(seat_ids):
		if key == len(seat_ids) - 1:
			continue

		seat_id_after = seat_ids[key + 1]

		if seat_id + 1 != seat_id_after:
			print(f"Seat ID {seat_id} doesn't have seat id after it.")
			missing = seat_id + 1

	return missing

def main():
	""" 
		For example, consider just the first seven characters of FBFBBFFRLR:

		Start by considering the whole range, rows 0 through 127.
		F means to take the lower half, keeping rows 0 through 63.
		B means to take the upper half, keeping rows 32 through 63.
		F means to take the lower half, keeping rows 32 through 47.
		B means to take the upper half, keeping rows 40 through 47.
		B keeps rows 44 through 47.
		F keeps rows 44 through 45.
		The final F keeps the lower of the two, row 44.
		
		For example, consider just the last 3 characters of FBFBBFFRLR:

		Start by considering the whole range, columns 0 through 7.
		R means to take the upper half, keeping columns 4 through 7.
		L means to take the lower half, keeping columns 4 through 5.
		The final R keeps the upper of the two, column 5.

		Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

		Example of board passes
		BFFFBBFRRR: row 70, column 7, seat ID 567.
		FFFBBBFRRR: row 14, column 7, seat ID 119.
		BBFFBBFRLL: row 102, column 4, seat ID 820.
	"""
	data = get_input_data()
	seat_ids = []

	for board_pass in data:
		if valid_board_pass(board_pass):
			row = get_row(board_pass)
			column = get_column(board_pass)
			seat_id = calculate_seat_id(row, column)
			#print(f"{board_pass}: row {row}, column {column}, sear ID {seat_id}.")	

			if seat_id in seat_ids:
				print("Seat ID already exists!")
				break

			seat_ids.append(seat_id)

	seat_ids.sort()
	my_seat_id = find_my_seat(seat_ids)

	print(f"Highest seat ID is {seat_ids[-1]}")
	print(f"And my seat id is {my_seat_id}")

main()

