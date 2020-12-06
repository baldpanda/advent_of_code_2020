import pytest

from custom_declaration_form_reader import CustomDeclarationFormReaderV2

PATH_TO_TEST_DATA = "day_6/tests/test_data/example_form_data.txt"

def test_reading_in_forms():
    """ Test reading in form data """
    expected_form_data = [[{'a','b','c'}], [{'a'},{'b'},{'c'}], [{'a','b'}, {'a','c'}], [{'a'},{'a'},{'a'},{'a'}], [{'b'}]]
    actual_form_data = CustomDeclarationFormReaderV2.read_in_forms(PATH_TO_TEST_DATA)
    assert type(actual_form_data) == list
    assert actual_form_data == expected_form_data


@pytest.mark.parametrize(
    "declaration_form, expected_common_yes_answers_count",
    [([{'a','b','c'}], 3), ([{'a'},{'b'},{'c'}],0), ([{'a','b'}, {'a','c'}], 1), ([{'a'},{'a'},{'a'},{'a'}], 1)]
)
def test_getting_number_of_common_yes_answers_for_group(declaration_form, expected_common_yes_answers_count):
    actual_common_yes = CustomDeclarationFormReaderV2.get_number_of_common_yes_answers(declaration_form)
    assert actual_common_yes == expected_common_yes_answers_count

def test_counting_number_of_yes_answers_from_file():
    form_data = CustomDeclarationFormReaderV2.read_in_forms(PATH_TO_TEST_DATA)
    expected_number_of_yes_answers = 6

    actual_number_of_yes_answers = CustomDeclarationFormReaderV2.get_total_number_of_common_yes_answers_from_different_groups(form_data)
    assert actual_number_of_yes_answers == expected_number_of_yes_answers
