from seat_finder import SeatFinder

with(open("day_5/solution/seat_codes.txt", "r")) as f:
    data = f.readlines()
list_of_rows = [code.strip() for code in data]

max_id = 0
taken_seats = set()

for code in list_of_rows:
    seat_finder = SeatFinder(code)
    actual_seat_id = seat_finder.get_seat()
    taken_seats.add(actual_seat_id)
    if actual_seat_id > max_id:
        max_id = actual_seat_id

list_of_existing_seats = set(range(71, 956))
print(list_of_existing_seats.difference(taken_seats))
