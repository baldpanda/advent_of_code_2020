import numpy as np

class ForestParser:

    def read_forest_from_file(self, path):
        with open(path) as f:
            data = f.readlines()
        list_of_rows = [[i for i in x.strip()] for x in data] 
        return np.array(list_of_rows)

