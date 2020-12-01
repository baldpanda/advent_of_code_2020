from expense_reader import ExpenseReader
from expense_fixer import ExpenseFixer

PATH_TO_EXPENSE_REPORT = "solution/expense_report.csv"
expenses = ExpenseReader.get_expenses_from_file(PATH_TO_EXPENSE_REPORT)

expense_fixer = ExpenseFixer(expenses)

print(f"Answer for two expenses: {expense_fixer.fix_report(2)}")
print(f"Answer for three expenses: {expense_fixer.fix_report(3)}")