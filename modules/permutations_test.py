import unittest
from . import permutations as p

# to run:
# python -m unittest discover -s modules -p "*_test.py" --verbose

# nPr == "n permute r" == number of arrangements of r items from n objects


class NPermuteRTest(unittest.TestCase):
    def test_returns_permutations_count_for_positive_unequal_integers(self):
        permutations_count: int = p.n_permute_r(n=3, r=2)
        expected_permutations_count: int = 6
        self.assertEqual(permutations_count, expected_permutations_count)

    def test_returns_permutations_count_for_equal_integers(self):
        permutations_count: int = p.n_permute_r(n=10,  r=10)
        expected_permutations_count: int = 1
        self.assertEqual(permutations_count, expected_permutations_count)

    def test_throws_error_for_invalid_arguments(self):
        try:
            p.n_permute_r(n=3, r=5)
        except ValueError:
            self.assertTrue(1, 1)
            return
        self.fail('no exception raised')


class PermutationsTest(unittest.TestCase):
    def test_returns_an_empty_set_for_an_empty_input_set(self):
        input_set: set = set()
        combinations_result: set = p.permutations_set(input_set)
        expected_combinations: set = set()
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_set_of_length_one_for_input_of_length_one(self):
        input_set: set = set('hello')
        combinations_result: set = p.permutations_set(input_set)
        expected_combinations: set = set('hello')
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_set_of_permutations_for_positive_unequal_integers(self):
        input_items: set = {'a', 'b', 'c'}
        permutations_result: set = p.permutations_set(source_set=input_items)
        expected_permutations: set = {
            {{'a'}, {'b'}, {'c'}},
            {{'a', 'b'}, {'a', 'c'}, {'b', 'c'}, {'b', 'a'}, {'c', 'a'}, {'c', 'b'}},
            {{'a', 'b', 'c'}},
        }
        # TODO: how to compare sets?
        self.assertItemsEqual(permutations_result, expected_permutations)


if __name__ == '__main__':
    unittest.main()
