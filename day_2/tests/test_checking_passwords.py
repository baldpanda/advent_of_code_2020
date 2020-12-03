import pandas as pd


class PasswordReader:
    def __init__(self, file_path):
        passwords = self._read_in_passwords_from_file_path(file_path)
        self.passwords = self._parse_rules(passwords)

    def _read_in_passwords_from_file_path(self, file_path):
        passwords = pd.read_csv(file_path, header=None, delimiter=": ")
        passwords.columns = ["rules", "passwords"]
        return passwords

    def _parse_rules(self, passwords):
        rules = passwords["rules"].str.split(pat=" ", expand=True)
        passwords[["constrained_character"]] = rules.iloc[:, 1]
        character_contraints = rules[0].str.split(pat="-", expand=True)
        passwords[
            ["min_number_of_occurences", "max_number_of_occurences"]
        ] = character_contraints
        return passwords

    def get_password_df(self):
        return self.passwords


class PassworkValidator:
    def is_password_valid_iteration_1(self, kwargs):
        character_frequency = kwargs.get("passwords").count(
            kwargs.get("constrained_character")
        )
        if int(
            kwargs.get("min_number_of_occurences")
        ) <= character_frequency and character_frequency <= int(
            kwargs.get("max_number_of_occurences")
        ):
            return True
        return False

    def is_password_valid_iteration_2(self, kwargs):
        password = kwargs.get("passwords")
        if password[int(kwargs.get("min_number_of_occurences")) - 1] == kwargs.get(
            "constrained_character"
        ) and password[int(kwargs.get("max_number_of_occurences")) - 1] != kwargs.get(
            "constrained_character"
        ):
            return True
        if password[int(kwargs.get("min_number_of_occurences")) - 1] != kwargs.get(
            "constrained_character"
        ) and password[int(kwargs.get("max_number_of_occurences")) - 1] == kwargs.get(
            "constrained_character"
        ):
            return True
        else:
            return False

    def get_number_of_valid_passwords(self, password_df):
        return sum(
            map(self.is_password_valid_iteration_1, password_df.to_dict("records"))
        )

    def get_number_of_valid_passwords_iteration_2(self, password_df):
        return sum(
            map(self.is_password_valid_iteration_2, password_df.to_dict("records"))
        )


PATH_TO_PASSWORDS = "day_2/tests/test_data/test_data.csv"


class TestCheckingPasswords:
    def test_validating_single_valid_password(self):
        password_validator = PassworkValidator()
        password = "ahaaa"
        rule = "2-5 a"
        expected_response = True

        assert (
            password_validator.is_password_valid_iteration_1(
                {
                    "min_number_of_occurences": 2,
                    "max_number_of_occurences": 5,
                    "constrained_character": "a",
                    "passwords": password,
                }
            )
            == expected_response
        )

    def test_validating_single_invalid_password(self):
        password_validator = PassworkValidator()
        password = "ahaaa"
        rule = "2-3 a"
        expected_response = False

        assert (
            password_validator.is_password_valid_iteration_1(
                {
                    "min_number_of_occurences": 2,
                    "max_number_of_occurences": 3,
                    "constrained_character": "a",
                    "passwords": password,
                }
            )
            == expected_response
        )

    def test_number_of_valid_passwords_returned_is_correct(self):
        expected_number_of_valid_passwords = 2
        password_reader = PasswordReader(PATH_TO_PASSWORDS)
        password_validator = PassworkValidator()
        actual_number_of_passwords = password_validator.get_number_of_valid_passwords(
            password_reader.get_password_df()
        )
        assert actual_number_of_passwords == expected_number_of_valid_passwords

    def test_number_of_valid_passwords_returned_is_correct_iteration_2(self):
        expected_number_of_valid_passwords = 1
        password_reader = PasswordReader(PATH_TO_PASSWORDS)
        password_validator = PassworkValidator()
        actual_number_of_passwords = (
            password_validator.get_number_of_valid_passwords_iteration_2(
                password_reader.get_password_df()
            )
        )
        assert actual_number_of_passwords == expected_number_of_valid_passwords


password_reader = PasswordReader("day_2/tests/test_data/actual_data.csv")
password_validator = PassworkValidator()
passwords = password_reader.get_password_df()
print(password_validator.get_number_of_valid_passwords(passwords))
print(password_validator.get_number_of_valid_passwords_iteration_2(passwords))
