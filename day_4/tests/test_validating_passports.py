import pytest

from passport_reader import PassportReader
from passport_validator import PassportValidator

def test_reading_in_data():
    passport_reader = PassportReader()
    parsed_passports = passport_reader.read_in_data("day_4/tests/test_data/test_data.txt")
    assert type(parsed_passports) == list 
    assert len(parsed_passports) == 4
    for passport in parsed_passports:
        assert type(passport) == dict


def test_validation_passes_for_valid_passport():
    valid_passport = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
    passport_validator = PassportValidator(valid_passport)
    passport_validator.validate_passport()

def test_exception_raised_for_invalid_passport():
    invalid_passport = {'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
    passport_validator = PassportValidator(invalid_passport)
    with pytest.raises(Exception):
        passport_validator.validate_passport()

def test_validating_passport():
    valid_passport_counter = 0
    passport_reader = PassportReader()
    parsed_passports = passport_reader.read_in_data("day_4/tests/test_data/test_data.txt")
    counter = 0
    for i in parsed_passports:
        passport_validator = PassportValidator(i)
        try:
            passport_validator.validate_passport()
            counter += 1
        except:
            1
    assert counter == 2


def test_raises_for_invalid_passports():
    passport_reader = PassportReader()
    parsed_passports = passport_reader.read_in_data("day_4/tests/test_data/invalid_passports.txt")
    for i in parsed_passports:
        passport_validator = PassportValidator(i)
        with pytest.raises(Exception):
            passport_validator.validate_passport()

def test_validating_valid_passport_does_not_raise():
    passport_reader = PassportReader()
    parsed_passports = passport_reader.read_in_data("day_4/tests/test_data/valid_passports.txt")
    for i in parsed_passports:
        passport_validator = PassportValidator(i)
        passport_validator.validate_passport()