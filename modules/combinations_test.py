import unittest
from . import combinations as c

# to run:
# from project root:
# python -m unittest discover -s modules -p "*_test.py" --verbose

# to run using green:
# from project root:
# green

# nCr == "n choose r" == number of combinations of r items from n objects (order doesn't matter)


class NChooseRTest(unittest.TestCase):
    def test_returns_combinations_count_for_positive_unequal_integers(self):
        combinations_count: int = c.n_choose_r(n=3, r=2)
        expected_combinations_count: int = 3
        self.assertEqual(combinations_count, expected_combinations_count)

    def test_returns_combinations_count_for_equal_integers(self):
        combinations_count: int = c.n_choose_r(n=10, r=10)
        expected_combinations_count: int = 1
        self.assertEqual(combinations_count, expected_combinations_count)

    def test_throws_value_error_for_invalid_arguments(self):
        try:
            c.n_choose_r(n=3, r=5)
        except ValueError:
            self.assertTrue(1, 1)
            return
        self.fail('no exception raised')


class CombinationsTest(unittest.TestCase):
    def test_returns_an_empty_list_for_an_empty_input_list(self):
        input_set: list = list()
        combinations_result: list = c.list_combinations(input_set)
        expected_combinations: list = list([])
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_list_of_length_one_for_input_of_length_one(self):
        input_set: list = ['hello']
        combinations_result: list = c.list_combinations(input_set)
        expected_combinations: list = [[], ['hello']]
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_list_of_combinations_for_positive_unequal_n_and_r(self):
        input_list: list = ['a', 'b', 'c']
        combinations_result: list = c.list_combinations(source=input_list)
        expected_combinations: list = [
            [[]],                                   # r = 0
            [['a'], ['b'], ['c']],                  # r = 1
            [['a', 'b'], ['a', 'c'], ['b', 'c']],   # r = 2
            [['a', 'b', 'c']]                       # r = 3
        ]
        print(f'expected_combinations:             {expected_combinations}')
        self.assertEqual(combinations_result, expected_combinations)


if __name__ == '__main__':
    unittest.main()
