import unittest
from . import combinations as c


# to run:
# from project root:
# python -m unittest discover -s modules -p "*_test.py" --verbose

# to run using green:
# from project root:
# green
# target specific test (in general, dotted names):
# green modules.combinations_test.CombinationsTest
# green modules.combinations_test.NChooseRTest

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
    def test_throws_value_error_for_n_or_r_less_than_zero(self):
        try:
            c.n_choose_r(n=-1, r=5)
        except ValueError:
            self.assertTrue(1, 1)
            return
        self.fail('no exception raised')

    def test_returns_an_empty_list_for_an_empty_input_list(self):
        input_list: list = list()
        combinations_result: list = c.list_combinations(input_list)
        expected_combinations: list = list([])
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_list_of_length_one_for_input_of_length_one(self):
        input_list: list = ['hello']
        combinations_result: list = c.list_combinations(input_list)
        expected_combinations: list = [[], ['hello']]
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_list_of_combinations_for_positive_unequal_n_and_r(self):
        input_list: list = ['a', 'b', 'c']
        combinations_result: list = c.list_combinations(source=input_list)
        expected_combinations: list = [
            [[]],  # r = 0
            [['a'], ['b'], ['c']],  # r = 1
            [['a', 'b'], ['a', 'c'], ['b', 'c']],  # r = 2
            [['a', 'b', 'c']]  # r = 3
        ]
        print(f'expected_combinations:             {expected_combinations}')
        self.assertEqual(combinations_result, expected_combinations)


class CombinationsRTest(unittest.TestCase):
    def test_throws_value_error_for_n_less_than_zero(self):
        try:
            c.n_choose_r(n=-1, r=5)
        except ValueError:
            self.assertTrue(1, 1)
            return
        self.fail('no exception raised for n less than 0')

    def test_throws_value_error_for_r_less_than_zero(self):
        try:
            c.n_choose_r(n=10, r=-5)
        except ValueError:
            self.assertTrue(1, 1)
            return
        self.fail('no exception raised for r less than 0')

    def test_throws_value_error_for_n_less_than_r(self):
        try:
            c.n_choose_r(n=10, r=11)
        except ValueError:
            self.assertTrue(1, 1)
            return
        self.fail('no exception raised for n less than r')

    def test_returns_an_empty_list_for_r_and_n_equal_0(self):
        input_list: list = list()
        r: int = 0
        combinations_r_result: list = c.combinations_r(input_list, r)
        print(f'combinations_r_result: {combinations_r_result}')
        expected_result: list = list([])
        self.assertEqual(combinations_r_result, expected_result)

    def test_returns_an_empty_list_for_r_equals_0(self):
        input_list: list = ['a', 'b', 'c']
        r: int = 0
        combinations_r_result: list = c.combinations_r(input_list, r)
        print(f'combinations_r_result: {combinations_r_result}')
        expected_result: list = list([])
        self.assertEqual(combinations_r_result, expected_result)

    def test_returns_a_list_of_length_1_combinations(self):
        input_list: list = ['a', 'b', 'c']
        r: int = 1
        combinations_r_result: list = c.combinations_r(input_list, r)
        print(f'combinations_r_result: {combinations_r_result}')
        expected_result: list = [['a'], ['b'], ['c']]
        self.assertEqual(combinations_r_result, expected_result)

    def test_returns_a_list_of_length_2_combinations(self):
        input_list: list = ['a', 'b', 'c', 'd']
        r: int = 2
        combinations_r_result: list = c.combinations_r(input_list, r)
        print(f'combinations_r_result: {combinations_r_result}')
        expected_result: list = [['a', 'b'], ['b', 'c'], ['a', 'c'], ['c', 'd'], ['b', 'd'], ['a', 'd']]
        self.assertEqual(combinations_r_result, expected_result)


if __name__ == '__main__':
    unittest.main()
