import numpy as np
import pytest
from forest_parser import ForestParser
from forest_navigator import ForestNavigator


def test_forest_reads_in_without_exception():
    forest_parser = ForestParser()

    forest = forest_parser.read_forest_from_file(
        "./day_3/tests/test_data/test_forest.txt"
    )

    assert forest.shape == (11, 11)


def test_tree_found_in_slice():
    slice_of_forest = np.array(
        [
            [".", ".", "#", "#", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
    forest_navigator = ForestNavigator(slice_of_forest)

    square = forest_navigator.does_crash_into_tree(row_index=0, column_index=0)

    assert square == False


def test_tree_found_in_slice():
    slice_of_forest = np.array(
        [
            [".", ".", "#", "#", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
    forest_navigator = ForestNavigator(slice_of_forest)

    square = forest_navigator.does_crash_into_tree(row_index=0, column_index=0)

    assert square == False


@pytest.mark.parametrize("number_of_moves_right, number_of_moves_down, expected_number_of_trees", [(3,1,7), (1,1,2), (5,1,3), (7,1,4), (1,2,2)])
def test_navigating_through_example_forest(number_of_moves_down, number_of_moves_right,expected_number_of_trees ):
    forest_parser = ForestParser()
    forest = forest_parser.read_forest_from_file(
        "./day_3/tests/test_data/test_forest.txt"
    )
    forest_navigator = ForestNavigator(forest)
    number_of_trees = forest_navigator.get_number_of_trees_will_crash_into(
        number_of_moves_down=number_of_moves_down,
        number_of_moves_right=number_of_moves_right,
    )
    assert number_of_trees == expected_number_of_trees
