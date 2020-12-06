class CustomDeclarationFormReader:
    @staticmethod
    def read_in_forms(path_to_data):
        with open(path_to_data, "r") as f:
            forms = f.read()
        forms = forms.split("\n\n")
        forms = [form_string.replace("\n", "") for form_string in forms]
        return forms

    @staticmethod
    def get_number_of_yes_answers(form):
        return len(set([a for a in form]))

    @staticmethod
    def get_total_number_of_yes_answers_from_different_groups(forms_from_groups):
        number_of_yes_answers = 0
        for form in forms_from_groups:
            number_of_yes_answers += CustomDeclarationFormReader.get_number_of_yes_answers(form)
        return number_of_yes_answers


class CustomDeclarationFormReaderV2:
    @staticmethod
    def read_in_forms(path_to_data):
        with open(path_to_data, "r") as f:
            forms = f.read()
        forms = forms.split("\n\n")
        forms = [[set(f) for f in form_string.split("\n")] for form_string in forms]
        return forms

    @staticmethod
    def get_number_of_common_yes_answers(form):
        return len(set.intersection(*form))

    @staticmethod
    def get_total_number_of_common_yes_answers_from_different_groups(forms_from_groups):
        number_of_yes_answers = 0
        for form in forms_from_groups:
            number_of_yes_answers += CustomDeclarationFormReaderV2.get_number_of_common_yes_answers(form)
        return number_of_yes_answers
