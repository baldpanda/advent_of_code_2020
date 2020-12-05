import pytest
from seat_finder import SeatFinder

@pytest.mark.parametrize(
    "seat_code, expected_seat_row",
    [("FBFBBFFRLR", 44),
    ("BFFFBBFRRR", 70),
    ("FFFBBBFRRR", 14),
    ("BBFFBBFRLL", 102)]
)
def test_getting_row(seat_code, expected_seat_row):
    SEAT_CODE = seat_code
    expected_row = expected_seat_row
    seat_finder = SeatFinder(SEAT_CODE)
    actual_row = seat_finder.get_row_location_code()

    assert actual_row == expected_row


@pytest.mark.parametrize(
    "seat_code, expected_seat_column",
    [("FBFBBFFRLR", 5),
    ("BFFFBBFRRR", 7),
    ("FFFBBBFRRR", 7),
    ("BBFFBBFRLL", 4)]
)
def test_getting_column(seat_code, expected_seat_column):
    seat_finder = SeatFinder(seat_code)
    actual_column = seat_finder.get_column_location_code()

    assert actual_column == expected_seat_column


@pytest.mark.parametrize(
    "seat_row, seat_column, expected_seat_column",
    [(44, 5, 357),
    (70, 7, 567),
    (14, 7, 119),
    (102, 4, 820)]
)
def test_getting_seat_id(seat_row, seat_column, expected_seat_column):
    seat_finder = SeatFinder("dummy")
    actual_id = seat_finder.get_seat_id(seat_column, seat_row)
    assert actual_id == expected_seat_column


@pytest.mark.parametrize(
    "seat_code, expected_seat_id",
    [("FBFBBFFRLR", 357),
    ("BFFFBBFRRR", 567),
    ("FFFBBBFRRR", 119),
    ("BBFFBBFRLL", 820)]
)
def test_getting_seat(seat_code, expected_seat_id):
    seat_finder = SeatFinder(seat_code)
    actual_seat_id = seat_finder.get_seat()
    assert actual_seat_id == expected_seat_id



