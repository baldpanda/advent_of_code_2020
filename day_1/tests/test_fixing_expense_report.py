from expense_reader import ExpenseReader
from expense_fixer import ExpenseFixer

PATH_TO_EXPENSES = "./tests/test_data/expense_data.csv"

class TestFixingExpenseReport:
    def test_getting_entries_adding_up_to_2020(self):

        # Arrange
        expense_report = ExpenseReader.get_expenses_from_file(PATH_TO_EXPENSES)
        expected_expenses = [1721, 299]
        sut = ExpenseFixer(expense_report)

        # Act
        actual_expenses = sut._get_expenses_adding_up_to_target(2020, expenses=expense_report)

        # Assert
        assert actual_expenses == expected_expenses

    def test_fixing_report(self):

        # Arrange
        expense_report = ExpenseReader.get_expenses_from_file(PATH_TO_EXPENSES)
        expected = 514579
        sut = ExpenseFixer(expense_report)

        # Act
        actual = sut.fix_report(2)

        # Assert
        assert actual == expected
    
    def test_fixing_report_where_three_expenses_required(self):

        # Arrange
        expense_report = ExpenseReader.get_expenses_from_file(PATH_TO_EXPENSES)
        expected = 241861950
        sut = ExpenseFixer(expense_report)

        # Act
        actual = sut.fix_report(3)

        # Assert
        assert actual == expected
