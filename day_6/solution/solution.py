from custom_declaration_form_reader import CustomDeclarationFormReader, CustomDeclarationFormReaderV2

PATH_TO_DATA = "/Users/patrickcallery/dev/advent_of_code_2020/day_6/solution/custom_declaration_form_data.txt"

declaration_forms = CustomDeclarationFormReader.read_in_forms(PATH_TO_DATA)
total_number_of_yes_answer = CustomDeclarationFormReader.get_total_number_of_yes_answers_from_different_groups(declaration_forms)

print(f"Total number of yes answers from different groups: {total_number_of_yes_answer}")


declaration_forms = CustomDeclarationFormReaderV2.read_in_forms(PATH_TO_DATA)
total_number_of_common_yes_answers = CustomDeclarationFormReaderV2.get_total_number_of_common_yes_answers_from_different_groups(declaration_forms)

print(f"Total number of common yes answers from different groups: {total_number_of_common_yes_answers}")