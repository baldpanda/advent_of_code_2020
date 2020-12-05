from passport_reader import PassportReader
from passport_validator import PassportValidator

valid_passport_counter = 0
passport_reader = PassportReader()
parsed_passports = passport_reader.read_in_data("day_4/solution/passport_data.txt")
counter = 0
for passport in parsed_passports:
    passport_validator = PassportValidator(passport)
    try:
        passport_validator.validate_passport()
        counter += 1
    except:
        pass
print(f"Counter: {counter}")