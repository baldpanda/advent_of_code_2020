import math


class ForestNavigator:
    def __init__(self, forest):
        self.forest = forest
        self.forest_depth, self.forest_width = forest.shape
        self.starting_location = (0, 0)

    def does_crash_into_tree(self, row_index, column_index):
        return self.forest[row_index, column_index] == "#"

    def get_number_of_trees_will_crash_into(
        self, number_of_moves_down, number_of_moves_right
    ):
        number_of_trees = 0
        location = self.starting_location
        lowest_point_in_forest_given_moves_down = (
            math.ceil(self.forest_depth / number_of_moves_down) - 1
        )
        for i in range(0, lowest_point_in_forest_given_moves_down):
            location = (
                location[0] + number_of_moves_down,
                (location[1] + number_of_moves_right) % self.forest_width,
            )
            if self.does_crash_into_tree(location[0], location[1]):
                number_of_trees += 1
        return number_of_trees
