from forest_parser import ForestParser
from forest_navigator import ForestNavigator

forest_parser = ForestParser()
forest = forest_parser.read_forest_from_file("day_3/solution/forest.txt")
forest_navigator = ForestNavigator(forest)
number_of_trees_1_3 = forest_navigator.get_number_of_trees_will_crash_into(1, 3)
number_of_trees_1_1 = forest_navigator.get_number_of_trees_will_crash_into(1, 1)
number_of_trees_5_1 = forest_navigator.get_number_of_trees_will_crash_into(1, 5)
number_of_trees_1_7 = forest_navigator.get_number_of_trees_will_crash_into(1, 7)
number_of_trees_2_1 = forest_navigator.get_number_of_trees_will_crash_into(2, 1)

print(f"Number of trees: {number_of_trees_1_3}")

print(number_of_trees_1_3 * number_of_trees_1_1 * number_of_trees_5_1* number_of_trees_1_7* number_of_trees_2_1)