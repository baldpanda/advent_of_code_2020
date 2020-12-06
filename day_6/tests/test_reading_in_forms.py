import pytest

from custom_declaration_form_reader import CustomDeclarationFormReader

PATH_TO_TEST_DATA = "day_6/tests/test_data/example_form_data.txt"

def test_reading_in_forms():
    """ Test reading in form data """
    expected_form_data = ['abc', 'abc', 'abac', 'aaaa', 'b']
    actual_form_data = CustomDeclarationFormReader.read_in_forms(PATH_TO_TEST_DATA)
    assert type(actual_form_data) == list
    assert actual_form_data == expected_form_data

@pytest.mark.parametrize(
    "declaration_form, expected_number_of_yes_answers",
    [("abc", 3), ("abcyabc",4), ("aaa", 1)]
)
def test_getting_number_of_yes_answers(declaration_form, expected_number_of_yes_answers):
    actual_number_of_yes_answers = CustomDeclarationFormReader.get_number_of_yes_answers(declaration_form)
    assert actual_number_of_yes_answers == expected_number_of_yes_answers

def test_getting_total_number_of_yes_answers_from_different_groups():
    expected_number_of_yes_answers = 8
    forms_from_different_groups = ["abc", "abcyabc", "aaa"]
    actual_number_of_yes_answers = CustomDeclarationFormReader.get_total_number_of_yes_answers_from_different_groups(forms_from_different_groups)
    assert actual_number_of_yes_answers == expected_number_of_yes_answers

def test_counting_number_of_yes_answers_from_file():
    form_data = CustomDeclarationFormReader.read_in_forms(PATH_TO_TEST_DATA)
    expected_number_of_yes_answers = 11

    actual_number_of_yes_answers = CustomDeclarationFormReader.get_total_number_of_yes_answers_from_different_groups(form_data)
    assert actual_number_of_yes_answers == expected_number_of_yes_answers