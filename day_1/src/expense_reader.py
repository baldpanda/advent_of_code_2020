import pandas as pd

class ExpenseReader:
    @staticmethod
    def get_expenses_from_file(path_to_file):
        return pd.read_csv(path_to_file, header=None).iloc[:, 0].tolist()
