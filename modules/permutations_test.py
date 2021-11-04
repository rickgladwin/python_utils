import unittest
from . import permutations as p

# to run:
# python -m unittest discover -s modules -p "*_test.py" --verbose

# nPr == "n permute r" == number of arrangements of r items from n objects

class PermuteTest(unittest.TestCase):
    def test_returns_permutations_count_for_positive_unequal_integers(self):
        permutations_count: int = p.permute(n=3,r=2)
        expected_permutations_count: int = 6
        self.assertEqual(permutations_count, expected_permutations_count)

    def test_returns_permutations_count_for_equal_integers(self):
        permutations_count: int = p.permute(n=10, r=10)
        expected_permutations_count: int = 1
        self.assertEqual(permutations_count, expected_permutations_count)

    def test_throws_error_for_invalid_arguments(self):
        try:
            p.permute(n=3,r=5)
        except:
            self.assertTrue(1,1)
            return
        self.fail('no exception raised')

class PermutationsTest(unittest.TestCase):
    def test_returns_a_set_of_permutations_for_positive_unequal_integers(self):
        input_items: list = ['a', 'b', 'c']
        permutations: set = p.permutations(items=input_items, r=2)
        expected_permutations: set = {['a','b'], ['b', 'c'], ['c', 'd']}
        self.assertEqual(permutations, expected_permutations)


if __name__ == '__main__':
    unittest.main()
