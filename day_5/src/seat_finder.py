import math 

class SeatFinder:
    NUMBER_OF_ROWS = 128
    NUMBER_OF_COLUMNS = 8

    def __init__(self, seat_code):
        self.seat_code = seat_code
    
    def get_row_location_code(self):
        row_code = self.seat_code[0:7]
        return self._binary_space_partitioning_resolver(lower_half_code="F", upper_half_code="B", seat_range=(0, self.NUMBER_OF_ROWS - 1), seat_code=row_code)

    def get_column_location_code(self):
        row_code = self.seat_code[7:10]
        return self._binary_space_partitioning_resolver(lower_half_code="L", upper_half_code="R", seat_range=(0, self.NUMBER_OF_COLUMNS - 1), seat_code=row_code)

    def _binary_space_partitioning_resolver(self, lower_half_code, upper_half_code, seat_range, seat_code):
        for c in seat_code:
            diff = (seat_range[1] - seat_range[0]) / 2
            if c == lower_half_code:
                seat_range = (seat_range[0], seat_range[1] - math.ceil(diff))
            elif c == upper_half_code:
                seat_range = (seat_range[0] + math.ceil(diff), seat_range[1])
            else:
                raise ValueError("Row code not recognised")
        if seat_range[0] != seat_range[1]:
            raise Exception("Unable to find seat")
        return seat_range[0]

    def get_seat_id(self, column_no, row_no):
        return (row_no * 8 + column_no)
    
    def get_seat(self):
        row = self.get_row_location_code()
        column = self.get_column_location_code()
        return self.get_seat_id(column, row)