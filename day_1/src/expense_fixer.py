import numpy as np

class ExpenseFixer:
    def __init__(self, expenses):
        self.expenses = expenses

    def _get_expenses_adding_up_to_target(self, target, expenses):
        for expense in expenses:
            required_expense = target - expense
            if required_expense in self.expenses:
                return [expense, required_expense]

    def fix_report(self, number_of_expenses):
        if number_of_expenses == 2:
            expenses_to_fix = self._get_expenses_adding_up_to_target(2020, expenses=self.expenses)
            return np.prod(expenses_to_fix)
        if number_of_expenses == 3:
            for expense in self.expenses:
                target = 2020 - expense
                expense_report_copy = self.expenses.copy()
                expense_report_copy.remove(expense)
                required_expenses = self._get_expenses_adding_up_to_target(target, expenses=expense_report_copy)
                if required_expenses is not None:
                    required_expenses.append(expense)
                    return np.prod(required_expenses)