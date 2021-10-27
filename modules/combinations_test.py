import unittest
from . import combinations as c

# to run:
# from project root:
# python -m unittest discover -s modules -p "*_test.py" --verbose

# to run using green:
# from project root:
# green

# nCr == "n choose r" == number of combinations of r items from n objects (order doesn't matter)

class ChooseTest(unittest.TestCase):
    def test_returns_combinations_count_for_positive_unequal_integers(self):
        combinations_count: int = c.choose(n=3,r=2)
        expected_combinations_count: int = 3
        self.assertEqual(combinations_count, expected_combinations_count)

    def test_returns_combinations_count_for_equal_integers(self):
        combinations_count: int = c.choose(n=10, r=10)
        expected_combinations_count: int = 1
        self.assertEqual(combinations_count, expected_combinations_count)

    def test_throws_error_for_invalid_arguments(self):
        try:
            c.choose(n=3,r=5)
        except:
            self.assertTrue(1,1)
            return
        self.fail('no exception raised')

class CombinationsTest(unittest.TestCase):
    def test_returns_a_set_of_combinations_for_positive_unequal_integers(self):
        input_items: list = ['a', 'b', 'c']
        combinations: set = c.combinations(items=input_items, r=2)
        expected_combinations: set = {['a','b'], ['b', 'c'], ['c', 'd']}
        self.assertEqual(combinations, expected_combinations)


if __name__ == '__main__':
    unittest.main()
