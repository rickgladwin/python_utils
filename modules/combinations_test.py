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
    def test_returns_an_empty_list_for_an_empty_input_list(self):
        input_list: list = list()
        combinations_result: list = c.combinations(input_list)
        expected_combinations: list = list([])
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_list_of_length_one_for_input_of_length_one(self):
        input_list: list = ['hello']
        combinations_result: list = c.combinations(input_list)
        expected_combinations: list = [[['hello']]]
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_list_of_string_combinations(self):
        input_list: list = ['a', 'b', 'c']
        combinations_result: list = c.combinations(source=input_list)
        expected_combinations: list = [
            [['a'], ['b'], ['c']],  # r = 1
            [['a', 'b'], ['a', 'c'], ['b', 'c']],  # r = 2
            [['a', 'b', 'c']]  # r = 3
        ]
        print(f'combinations_result:               {combinations_result}')
        print(f'expected_combinations:             {expected_combinations}')
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_list_of_integer_combinations(self):
        input_list: list = [i for i in range(0, 3)]
        combinations_result: list = c.combinations(source=input_list)
        expected_combinations: list = [
            [[0], [1], [2]],  # r = 1
            [[0, 1], [0, 2], [1, 2]],  # r = 2
            [[0, 1, 2]]  # r = 3
        ]
        print(f'combinations_result:               {combinations_result}')
        print(f'expected_combinations:             {expected_combinations}')
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_list_of_dictionary_combinations(self):
        input_list: list = [
            {'key_1':'value_1'},
            {'key_2':'value_2'},
            {'key_3':'value_3'},
        ]
        combinations_result: list = c.combinations(source=input_list)
        expected_combinations: list = [
            [[{'key_1':'value_1'}], [{'key_2':'value_2'}], [{'key_3':'value_3'}]],  # r = 1
            [[{'key_1':'value_1'}, {'key_2':'value_2'}], [{'key_1':'value_1'}, {'key_3':'value_3'}],
             [{'key_2':'value_2'}, {'key_3':'value_3'}]],  # r = 2
            [[{'key_1':'value_1'}, {'key_2':'value_2'}, {'key_3':'value_3'}]]  # r = 3
        ]
        print(f'combinations_result:               {combinations_result}')
        print(f'expected_combinations:             {expected_combinations}')
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_a_large_list_of_integer_combinations_for_positive_unequal_n_and_r(self):
        input_list: list = [i for i in range(0, 11)]
        combinations_result: list = c.combinations(source=input_list)
        expected_combinations: list = n_equals_10_combinations
        self.assertEqual(combinations_result, expected_combinations)

    def test_returns_without_error_for_an_input_list_with_10_elements_of_1_character(self):
        print(f'testing input list with 10 elements of 1 character...')
        input_list: list = ['a' for i in range(0, 10)]
        combinations_result: list = c.combinations(source=input_list)
        print(f'completed with 10 elements of 1 character')
        self.assertTrue(1, 1)

    def test_returns_without_error_for_an_input_list_with_10_elements_of_2_characters(self):
        print(f'testing input list with 10 elements of 2 characters...')
        input_list: list = ['aa' for i in range(0, 10)]
        combinations_result: list = c.combinations(source=input_list)
        print(f'completed with 10 elements of 2 characters')
        self.assertTrue(1, 1)

    def test_returns_without_error_for_an_input_list_with_10_elements_of_3_characters(self):
        print(f'testing input list with 10 elements of 3 characters...')
        input_list: list = ['aaa' for i in range(0, 10)]
        combinations_result: list = c.combinations(source=input_list)
        print(f'completed with 10 elements of 3 characters')
        self.assertTrue(1, 1)

    def test_returns_without_error_for_an_input_list_with_10_elements_of_10_characters(self):
        print(f'testing input list with 10 elements of 10 characters...')
        input_list: list = ['aaaaaaaaaa' for i in range(0, 10)]
        combinations_result: list = c.combinations(source=input_list)
        print(f'completed with 10 elements of 10 characters')
        self.assertTrue(1, 1)

    def test_returns_without_error_for_an_input_list_with_10_elements_of_50_characters(self):
        print(f'testing input list with 10 elements of 50 characters...')
        input_list: list = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' for i in range(0, 10)]
        combinations_result: list = c.combinations(source=input_list)
        print(f'completed with 10 elements of 50 characters')
        self.assertTrue(1, 1)

    def test_returns_without_error_for_an_input_list_with_20_elements_of_1_character(self):
        print(f'testing input list with 20 elements of 1 character...')
        input_list: list = ['a' for i in range(0, 20)]
        combinations_result: list = c.combinations(source=input_list)
        print(f'completed with 20 elements of 1 character')
        self.assertTrue(1, 1)

    def test_returns_without_error_for_an_input_list_with_20_elements_of_2_characters(self):
        print(f'testing input list with 20 elements of 2 characters...')
        input_list: list = ['aa' for i in range(0, 20)]
        combinations_result: list = c.combinations(source=input_list)
        print(f'completed with 20 elements of 2 characters')
        self.assertTrue(1, 1)

    def test_returns_without_error_for_an_input_list_with_20_elements_of_3_characters(self):
        print(f'testing input list with 20 elements of 3 characters...')
        input_list: list = ['aaa' for i in range(0, 20)]
        combinations_result: list = c.combinations(source=input_list)
        print(f'completed with 20 elements of 3 characters')
        self.assertTrue(1, 1)

    def test_returns_without_error_for_an_input_list_with_20_elements_of_10_characters(self):
        print(f'testing input list with 20 elements of 10 characters...')
        input_list: list = ['aaaaaaaaaa' for i in range(0, 20)]
        combinations_result: list = c.combinations(source=input_list)
        print(f'completed with 20 elements of 10 characters')
        self.assertTrue(1, 1)

    def test_returns_without_error_for_an_input_list_with_21_elements_of_1_character(self):
        print(f'testing input list with 21 elements of 1 character...')
        input_list: list = ['a' for i in range(0, 21)]
        combinations_result: list = c.combinations(source=input_list)
        print(f'completed with 21 elements of 1 character')
        self.assertTrue(1, 1)

    # def test_returns_without_error_for_an_input_list_with_22_elements_of_1_character(self):
    #     print(f'testing input list with 22 elements of 1 character...')
    #     input_list: list = ['a' for i in range(0, 22)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 22 elements of 1 character')
    #     self.assertTrue(1, 1)
    #
    # def test_returns_without_error_for_an_input_list_with_23_elements_of_1_character(self):
    #     print(f'testing input list with 23 elements of 1 character...')
    #     input_list: list = ['a' for i in range(0, 23)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 23 elements of 1 character')
    #     self.assertTrue(1, 1)

    # NOTE: higher than 23 takes a long time

    # def test_returns_without_error_for_an_input_list_with_24_elements_of_1_character(self):
    #     print(f'testing input list with 24 elements of 1 character...')
    #     input_list: list = ['a' for i in range(0, 24)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 24 elements of 1 character')
    #     self.assertTrue(1, 1)

    # def test_returns_without_error_for_an_input_list_with_30_elements_of_1_character(self):
    #     print(f'testing input list with 30 elements of 1 character...')
    #     input_list: list = ['a' for i in range(0, 30)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 30 elements of 1 character')
    #     self.assertTrue(1, 1)

    # def test_returns_without_error_for_an_input_list_with_30_elements_of_2_characters(self):
    #     print(f'testing input list with 30 elements of 2 characters...')
    #     input_list: list = ['aa' for i in range(0, 30)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 30 elements of 2 characters')
    #     self.assertTrue(1, 1)

    # def test_returns_without_error_for_an_input_list_with_30_elements_of_3_characters(self):
    #     print(f'testing input list with 30 elements of 3 characters...')
    #     input_list: list = ['aaa' for i in range(0, 30)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 30 elements of 3 characters')
    #     self.assertTrue(1, 1)

    # def test_returns_without_error_for_an_input_list_with_10_elements(self):
    #     print(f'testing input list with 10 elements...')
    #     input_list: list = [i for i in range(0, 10)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 10 elements')
    #     self.assertTrue(1, 1)
    #
    # def test_throws_an_error_at_some_element_limit_before_100(self):
    #     test_list_length: int = 1
    #     try:
    #         while test_list_length < 100:
    #             input_list: list = ['a' for i in range(0, test_list_length)]
    #             combinations_result: list = c.combinations(source=input_list)
    #             print(f'completed test with {test_list_length} elements')
    #             test_list_length += 1
    #     except:
    #         self.assertTrue(1, 1)
    #         return
    #     self.fail('no exception raised for source list length < 100')
    #
    # def test_returns_without_error_for_an_input_list_with_10_chars(self):
    #     print(f'testing input list with 10 chars...')
    #     input_list: list = [i for i in range(0, 10)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 10 chars')
    #     self.assertTrue(1, 1)
    #
    # def test_returns_without_error_for_an_input_list_with_20_elements(self):
    #     print(f'testing input list with 20 elements...')
    #     input_list: list = [i for i in range(0, 20)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 20 elements')
    #     self.assertTrue(1, 1)

    # def test_returns_without_error_for_an_input_list_with_20_chars(self):
    #     print(f'testing input list with 20 chars...')
    #     input_list: list = [i for i in range(10, 21)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 20 chars')
    #     self.assertTrue(1, 1)
    #
    # def test_returns_without_error_for_an_input_list_with_25_elements(self):
    #     print(f'testing input list with 25 elements...')
    #     input_list: list = ['a' for i in range(0, 25)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 25 elements')
    #     self.assertTrue(1, 1)
    #
    # def test_returns_without_error_for_an_input_list_with_30_elements(self):
    #     print(f'testing input list with 30 elements...')
    #     input_list: list = ['a' for i in range(0, 30)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 30 elements')
    #     self.assertTrue(1, 1)
    #
    # def test_returns_without_error_for_an_input_list_with_30_chars(self):
    #     print(f'testing input list with 30 chars...')
    #     input_list: list = [i for i in range(100, 111)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 30 chars')
    #     self.assertTrue(1, 1)

    # def test_returns_without_error_for_an_input_list_with_30_chars(self):
    #     print(f'testing input list with 30 chars...')
    #     input_list: list = [i for i in range(0, 30)]
    #     combinations_result: list = c.combinations(source=input_list)
    #     print(f'completed with 30 chars')
    #     self.assertTrue(1, 1)


class CombinationsRTest(unittest.TestCase):
    def test_throws_value_error_for_r_less_than_zero(self):
        input_list: list = ['a', 'b', 'c']
        try:
            c.combinations_r(source=input_list, r=-5)
        except ValueError:
            self.assertTrue(1, 1)
            return
        self.fail('no exception raised for r less than 0')

    def test_throws_value_error_for_n_less_than_r(self):
        input_list: list = ['a', 'b', 'c', 'd']
        try:
            c.combinations_r(source=input_list, r=6)
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
        # expected_result: list = [['a', 'b'], ['b', 'c'], ['a', 'c'], ['c', 'd'], ['b', 'd'], ['a', 'd']]
        # TODO: compare two lists and ignore element order
        expected_result: list = [['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'd'], ['b', 'd'], ['c', 'd']]
        self.assertEqual(combinations_r_result, expected_result)

    def test_returns_a_list_of_length_3_combinations(self):
        input_list: list = ['a', 'b', 'c', 'd']
        r: int = 3
        combinations_r_result: list = c.combinations_r(input_list, r)
        print(f'combinations_r_result: {combinations_r_result}')
        expected_result: list = [['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'c', 'd'], ['b', 'c', 'd']]
        print(f'expected_result: {expected_result}')
        self.assertEqual(combinations_r_result, expected_result)

    def test_returns_a_list_of_length_4_combinations(self):
        input_list: list = ['a', 'b', 'c', 'd', 'e', 'f']
        r: int = 4
        combinations_r_result: list = c.combinations_r(input_list, r)
        print(f'combinations_r_result: {combinations_r_result}')
        expected_result: list = [
            ['a', 'b', 'c', 'd'],
            ['a', 'b', 'c', 'e'],
            ['a', 'b', 'd', 'e'],
            ['a', 'c', 'd', 'e'],
            ['b', 'c', 'd', 'e'],
            ['a', 'b', 'c', 'f'],
            ['a', 'b', 'd', 'f'],
            ['a', 'c', 'd', 'f'],
            ['b', 'c', 'd', 'f'],
            ['a', 'b', 'e', 'f'],
            ['a', 'c', 'e', 'f'],
            ['b', 'c', 'e', 'f'],
            ['a', 'd', 'e', 'f'],
            ['b', 'd', 'e', 'f'],
            ['c', 'd', 'e', 'f'],
        ]
        print(f'expected_result: {expected_result}')
        self.assertEqual(combinations_r_result, expected_result)


n_equals_10_combinations: list = [
    [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]],
    [[0, 1], [0, 2], [1, 2], [0, 3], [1, 3], [2, 3], [0, 4], [1, 4], [2, 4], [3, 4], [0, 5], [1, 5], [2, 5], [3, 5],
     [4, 5], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7],
     [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [0, 9], [1, 9], [2, 9], [3, 9], [4, 9], [5, 9],
     [6, 9], [7, 9], [8, 9], [0, 10], [1, 10], [2, 10], [3, 10], [4, 10], [5, 10], [6, 10], [7, 10], [8, 10], [9, 10]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3], [0, 1, 4], [0, 2, 4], [1, 2, 4], [0, 3, 4], [1, 3, 4], [2, 3, 4],
     [0, 1, 5], [0, 2, 5], [1, 2, 5], [0, 3, 5], [1, 3, 5], [2, 3, 5], [0, 4, 5], [1, 4, 5], [2, 4, 5], [3, 4, 5],
     [0, 1, 6], [0, 2, 6], [1, 2, 6], [0, 3, 6], [1, 3, 6], [2, 3, 6], [0, 4, 6], [1, 4, 6], [2, 4, 6], [3, 4, 6],
     [0, 5, 6], [1, 5, 6], [2, 5, 6], [3, 5, 6], [4, 5, 6], [0, 1, 7], [0, 2, 7], [1, 2, 7], [0, 3, 7], [1, 3, 7],
     [2, 3, 7], [0, 4, 7], [1, 4, 7], [2, 4, 7], [3, 4, 7], [0, 5, 7], [1, 5, 7], [2, 5, 7], [3, 5, 7], [4, 5, 7],
     [0, 6, 7], [1, 6, 7], [2, 6, 7], [3, 6, 7], [4, 6, 7], [5, 6, 7], [0, 1, 8], [0, 2, 8], [1, 2, 8], [0, 3, 8],
     [1, 3, 8], [2, 3, 8], [0, 4, 8], [1, 4, 8], [2, 4, 8], [3, 4, 8], [0, 5, 8], [1, 5, 8], [2, 5, 8], [3, 5, 8],
     [4, 5, 8], [0, 6, 8], [1, 6, 8], [2, 6, 8], [3, 6, 8], [4, 6, 8], [5, 6, 8], [0, 7, 8], [1, 7, 8], [2, 7, 8],
     [3, 7, 8], [4, 7, 8], [5, 7, 8], [6, 7, 8], [0, 1, 9], [0, 2, 9], [1, 2, 9], [0, 3, 9], [1, 3, 9], [2, 3, 9],
     [0, 4, 9], [1, 4, 9], [2, 4, 9], [3, 4, 9], [0, 5, 9], [1, 5, 9], [2, 5, 9], [3, 5, 9], [4, 5, 9], [0, 6, 9],
     [1, 6, 9], [2, 6, 9], [3, 6, 9], [4, 6, 9], [5, 6, 9], [0, 7, 9], [1, 7, 9], [2, 7, 9], [3, 7, 9], [4, 7, 9],
     [5, 7, 9], [6, 7, 9], [0, 8, 9], [1, 8, 9], [2, 8, 9], [3, 8, 9], [4, 8, 9], [5, 8, 9], [6, 8, 9], [7, 8, 9],
     [0, 1, 10], [0, 2, 10], [1, 2, 10], [0, 3, 10], [1, 3, 10], [2, 3, 10], [0, 4, 10], [1, 4, 10], [2, 4, 10],
     [3, 4, 10], [0, 5, 10], [1, 5, 10], [2, 5, 10], [3, 5, 10], [4, 5, 10], [0, 6, 10], [1, 6, 10], [2, 6, 10],
     [3, 6, 10], [4, 6, 10], [5, 6, 10], [0, 7, 10], [1, 7, 10], [2, 7, 10], [3, 7, 10], [4, 7, 10], [5, 7, 10],
     [6, 7, 10], [0, 8, 10], [1, 8, 10], [2, 8, 10], [3, 8, 10], [4, 8, 10], [5, 8, 10], [6, 8, 10], [7, 8, 10],
     [0, 9, 10], [1, 9, 10], [2, 9, 10], [3, 9, 10], [4, 9, 10], [5, 9, 10], [6, 9, 10], [7, 9, 10], [8, 9, 10]],
    [[0, 1, 2, 3], [0, 1, 2, 4], [0, 1, 3, 4], [0, 2, 3, 4], [1, 2, 3, 4], [0, 1, 2, 5], [0, 1, 3, 5], [0, 2, 3, 5],
     [1, 2, 3, 5], [0, 1, 4, 5], [0, 2, 4, 5], [1, 2, 4, 5], [0, 3, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5], [0, 1, 2, 6],
     [0, 1, 3, 6], [0, 2, 3, 6], [1, 2, 3, 6], [0, 1, 4, 6], [0, 2, 4, 6], [1, 2, 4, 6], [0, 3, 4, 6], [1, 3, 4, 6],
     [2, 3, 4, 6], [0, 1, 5, 6], [0, 2, 5, 6], [1, 2, 5, 6], [0, 3, 5, 6], [1, 3, 5, 6], [2, 3, 5, 6], [0, 4, 5, 6],
     [1, 4, 5, 6], [2, 4, 5, 6], [3, 4, 5, 6], [0, 1, 2, 7], [0, 1, 3, 7], [0, 2, 3, 7], [1, 2, 3, 7], [0, 1, 4, 7],
     [0, 2, 4, 7], [1, 2, 4, 7], [0, 3, 4, 7], [1, 3, 4, 7], [2, 3, 4, 7], [0, 1, 5, 7], [0, 2, 5, 7], [1, 2, 5, 7],
     [0, 3, 5, 7], [1, 3, 5, 7], [2, 3, 5, 7], [0, 4, 5, 7], [1, 4, 5, 7], [2, 4, 5, 7], [3, 4, 5, 7], [0, 1, 6, 7],
     [0, 2, 6, 7], [1, 2, 6, 7], [0, 3, 6, 7], [1, 3, 6, 7], [2, 3, 6, 7], [0, 4, 6, 7], [1, 4, 6, 7], [2, 4, 6, 7],
     [3, 4, 6, 7], [0, 5, 6, 7], [1, 5, 6, 7], [2, 5, 6, 7], [3, 5, 6, 7], [4, 5, 6, 7], [0, 1, 2, 8], [0, 1, 3, 8],
     [0, 2, 3, 8], [1, 2, 3, 8], [0, 1, 4, 8], [0, 2, 4, 8], [1, 2, 4, 8], [0, 3, 4, 8], [1, 3, 4, 8], [2, 3, 4, 8],
     [0, 1, 5, 8], [0, 2, 5, 8], [1, 2, 5, 8], [0, 3, 5, 8], [1, 3, 5, 8], [2, 3, 5, 8], [0, 4, 5, 8], [1, 4, 5, 8],
     [2, 4, 5, 8], [3, 4, 5, 8], [0, 1, 6, 8], [0, 2, 6, 8], [1, 2, 6, 8], [0, 3, 6, 8], [1, 3, 6, 8], [2, 3, 6, 8],
     [0, 4, 6, 8], [1, 4, 6, 8], [2, 4, 6, 8], [3, 4, 6, 8], [0, 5, 6, 8], [1, 5, 6, 8], [2, 5, 6, 8], [3, 5, 6, 8],
     [4, 5, 6, 8], [0, 1, 7, 8], [0, 2, 7, 8], [1, 2, 7, 8], [0, 3, 7, 8], [1, 3, 7, 8], [2, 3, 7, 8], [0, 4, 7, 8],
     [1, 4, 7, 8], [2, 4, 7, 8], [3, 4, 7, 8], [0, 5, 7, 8], [1, 5, 7, 8], [2, 5, 7, 8], [3, 5, 7, 8], [4, 5, 7, 8],
     [0, 6, 7, 8], [1, 6, 7, 8], [2, 6, 7, 8], [3, 6, 7, 8], [4, 6, 7, 8], [5, 6, 7, 8], [0, 1, 2, 9], [0, 1, 3, 9],
     [0, 2, 3, 9], [1, 2, 3, 9], [0, 1, 4, 9], [0, 2, 4, 9], [1, 2, 4, 9], [0, 3, 4, 9], [1, 3, 4, 9], [2, 3, 4, 9],
     [0, 1, 5, 9], [0, 2, 5, 9], [1, 2, 5, 9], [0, 3, 5, 9], [1, 3, 5, 9], [2, 3, 5, 9], [0, 4, 5, 9], [1, 4, 5, 9],
     [2, 4, 5, 9], [3, 4, 5, 9], [0, 1, 6, 9], [0, 2, 6, 9], [1, 2, 6, 9], [0, 3, 6, 9], [1, 3, 6, 9], [2, 3, 6, 9],
     [0, 4, 6, 9], [1, 4, 6, 9], [2, 4, 6, 9], [3, 4, 6, 9], [0, 5, 6, 9], [1, 5, 6, 9], [2, 5, 6, 9], [3, 5, 6, 9],
     [4, 5, 6, 9], [0, 1, 7, 9], [0, 2, 7, 9], [1, 2, 7, 9], [0, 3, 7, 9], [1, 3, 7, 9], [2, 3, 7, 9], [0, 4, 7, 9],
     [1, 4, 7, 9], [2, 4, 7, 9], [3, 4, 7, 9], [0, 5, 7, 9], [1, 5, 7, 9], [2, 5, 7, 9], [3, 5, 7, 9], [4, 5, 7, 9],
     [0, 6, 7, 9], [1, 6, 7, 9], [2, 6, 7, 9], [3, 6, 7, 9], [4, 6, 7, 9], [5, 6, 7, 9], [0, 1, 8, 9], [0, 2, 8, 9],
     [1, 2, 8, 9], [0, 3, 8, 9], [1, 3, 8, 9], [2, 3, 8, 9], [0, 4, 8, 9], [1, 4, 8, 9], [2, 4, 8, 9], [3, 4, 8, 9],
     [0, 5, 8, 9], [1, 5, 8, 9], [2, 5, 8, 9], [3, 5, 8, 9], [4, 5, 8, 9], [0, 6, 8, 9], [1, 6, 8, 9], [2, 6, 8, 9],
     [3, 6, 8, 9], [4, 6, 8, 9], [5, 6, 8, 9], [0, 7, 8, 9], [1, 7, 8, 9], [2, 7, 8, 9], [3, 7, 8, 9], [4, 7, 8, 9],
     [5, 7, 8, 9], [6, 7, 8, 9], [0, 1, 2, 10], [0, 1, 3, 10], [0, 2, 3, 10], [1, 2, 3, 10], [0, 1, 4, 10],
     [0, 2, 4, 10], [1, 2, 4, 10], [0, 3, 4, 10], [1, 3, 4, 10], [2, 3, 4, 10], [0, 1, 5, 10], [0, 2, 5, 10],
     [1, 2, 5, 10], [0, 3, 5, 10], [1, 3, 5, 10], [2, 3, 5, 10], [0, 4, 5, 10], [1, 4, 5, 10], [2, 4, 5, 10],
     [3, 4, 5, 10], [0, 1, 6, 10], [0, 2, 6, 10], [1, 2, 6, 10], [0, 3, 6, 10], [1, 3, 6, 10], [2, 3, 6, 10],
     [0, 4, 6, 10], [1, 4, 6, 10], [2, 4, 6, 10], [3, 4, 6, 10], [0, 5, 6, 10], [1, 5, 6, 10], [2, 5, 6, 10],
     [3, 5, 6, 10], [4, 5, 6, 10], [0, 1, 7, 10], [0, 2, 7, 10], [1, 2, 7, 10], [0, 3, 7, 10], [1, 3, 7, 10],
     [2, 3, 7, 10], [0, 4, 7, 10], [1, 4, 7, 10], [2, 4, 7, 10], [3, 4, 7, 10], [0, 5, 7, 10], [1, 5, 7, 10],
     [2, 5, 7, 10], [3, 5, 7, 10], [4, 5, 7, 10], [0, 6, 7, 10], [1, 6, 7, 10], [2, 6, 7, 10], [3, 6, 7, 10],
     [4, 6, 7, 10], [5, 6, 7, 10], [0, 1, 8, 10], [0, 2, 8, 10], [1, 2, 8, 10], [0, 3, 8, 10], [1, 3, 8, 10],
     [2, 3, 8, 10], [0, 4, 8, 10], [1, 4, 8, 10], [2, 4, 8, 10], [3, 4, 8, 10], [0, 5, 8, 10], [1, 5, 8, 10],
     [2, 5, 8, 10], [3, 5, 8, 10], [4, 5, 8, 10], [0, 6, 8, 10], [1, 6, 8, 10], [2, 6, 8, 10], [3, 6, 8, 10],
     [4, 6, 8, 10], [5, 6, 8, 10], [0, 7, 8, 10], [1, 7, 8, 10], [2, 7, 8, 10], [3, 7, 8, 10], [4, 7, 8, 10],
     [5, 7, 8, 10], [6, 7, 8, 10], [0, 1, 9, 10], [0, 2, 9, 10], [1, 2, 9, 10], [0, 3, 9, 10], [1, 3, 9, 10],
     [2, 3, 9, 10], [0, 4, 9, 10], [1, 4, 9, 10], [2, 4, 9, 10], [3, 4, 9, 10], [0, 5, 9, 10], [1, 5, 9, 10],
     [2, 5, 9, 10], [3, 5, 9, 10], [4, 5, 9, 10], [0, 6, 9, 10], [1, 6, 9, 10], [2, 6, 9, 10], [3, 6, 9, 10],
     [4, 6, 9, 10], [5, 6, 9, 10], [0, 7, 9, 10], [1, 7, 9, 10], [2, 7, 9, 10], [3, 7, 9, 10], [4, 7, 9, 10],
     [5, 7, 9, 10], [6, 7, 9, 10], [0, 8, 9, 10], [1, 8, 9, 10], [2, 8, 9, 10], [3, 8, 9, 10], [4, 8, 9, 10],
     [5, 8, 9, 10], [6, 8, 9, 10], [7, 8, 9, 10]],
    [[0, 1, 2, 3, 4], [0, 1, 2, 3, 5], [0, 1, 2, 4, 5], [0, 1, 3, 4, 5], [0, 2, 3, 4, 5], [1, 2, 3, 4, 5],
     [0, 1, 2, 3, 6], [0, 1, 2, 4, 6], [0, 1, 3, 4, 6], [0, 2, 3, 4, 6], [1, 2, 3, 4, 6], [0, 1, 2, 5, 6],
     [0, 1, 3, 5, 6], [0, 2, 3, 5, 6], [1, 2, 3, 5, 6], [0, 1, 4, 5, 6], [0, 2, 4, 5, 6], [1, 2, 4, 5, 6],
     [0, 3, 4, 5, 6], [1, 3, 4, 5, 6], [2, 3, 4, 5, 6], [0, 1, 2, 3, 7], [0, 1, 2, 4, 7], [0, 1, 3, 4, 7],
     [0, 2, 3, 4, 7], [1, 2, 3, 4, 7], [0, 1, 2, 5, 7], [0, 1, 3, 5, 7], [0, 2, 3, 5, 7], [1, 2, 3, 5, 7],
     [0, 1, 4, 5, 7], [0, 2, 4, 5, 7], [1, 2, 4, 5, 7], [0, 3, 4, 5, 7], [1, 3, 4, 5, 7], [2, 3, 4, 5, 7],
     [0, 1, 2, 6, 7], [0, 1, 3, 6, 7], [0, 2, 3, 6, 7], [1, 2, 3, 6, 7], [0, 1, 4, 6, 7], [0, 2, 4, 6, 7],
     [1, 2, 4, 6, 7], [0, 3, 4, 6, 7], [1, 3, 4, 6, 7], [2, 3, 4, 6, 7], [0, 1, 5, 6, 7], [0, 2, 5, 6, 7],
     [1, 2, 5, 6, 7], [0, 3, 5, 6, 7], [1, 3, 5, 6, 7], [2, 3, 5, 6, 7], [0, 4, 5, 6, 7], [1, 4, 5, 6, 7],
     [2, 4, 5, 6, 7], [3, 4, 5, 6, 7], [0, 1, 2, 3, 8], [0, 1, 2, 4, 8], [0, 1, 3, 4, 8], [0, 2, 3, 4, 8],
     [1, 2, 3, 4, 8], [0, 1, 2, 5, 8], [0, 1, 3, 5, 8], [0, 2, 3, 5, 8], [1, 2, 3, 5, 8], [0, 1, 4, 5, 8],
     [0, 2, 4, 5, 8], [1, 2, 4, 5, 8], [0, 3, 4, 5, 8], [1, 3, 4, 5, 8], [2, 3, 4, 5, 8], [0, 1, 2, 6, 8],
     [0, 1, 3, 6, 8], [0, 2, 3, 6, 8], [1, 2, 3, 6, 8], [0, 1, 4, 6, 8], [0, 2, 4, 6, 8], [1, 2, 4, 6, 8],
     [0, 3, 4, 6, 8], [1, 3, 4, 6, 8], [2, 3, 4, 6, 8], [0, 1, 5, 6, 8], [0, 2, 5, 6, 8], [1, 2, 5, 6, 8],
     [0, 3, 5, 6, 8], [1, 3, 5, 6, 8], [2, 3, 5, 6, 8], [0, 4, 5, 6, 8], [1, 4, 5, 6, 8], [2, 4, 5, 6, 8],
     [3, 4, 5, 6, 8], [0, 1, 2, 7, 8], [0, 1, 3, 7, 8], [0, 2, 3, 7, 8], [1, 2, 3, 7, 8], [0, 1, 4, 7, 8],
     [0, 2, 4, 7, 8], [1, 2, 4, 7, 8], [0, 3, 4, 7, 8], [1, 3, 4, 7, 8], [2, 3, 4, 7, 8], [0, 1, 5, 7, 8],
     [0, 2, 5, 7, 8], [1, 2, 5, 7, 8], [0, 3, 5, 7, 8], [1, 3, 5, 7, 8], [2, 3, 5, 7, 8], [0, 4, 5, 7, 8],
     [1, 4, 5, 7, 8], [2, 4, 5, 7, 8], [3, 4, 5, 7, 8], [0, 1, 6, 7, 8], [0, 2, 6, 7, 8], [1, 2, 6, 7, 8],
     [0, 3, 6, 7, 8], [1, 3, 6, 7, 8], [2, 3, 6, 7, 8], [0, 4, 6, 7, 8], [1, 4, 6, 7, 8], [2, 4, 6, 7, 8],
     [3, 4, 6, 7, 8], [0, 5, 6, 7, 8], [1, 5, 6, 7, 8], [2, 5, 6, 7, 8], [3, 5, 6, 7, 8], [4, 5, 6, 7, 8],
     [0, 1, 2, 3, 9], [0, 1, 2, 4, 9], [0, 1, 3, 4, 9], [0, 2, 3, 4, 9], [1, 2, 3, 4, 9], [0, 1, 2, 5, 9],
     [0, 1, 3, 5, 9], [0, 2, 3, 5, 9], [1, 2, 3, 5, 9], [0, 1, 4, 5, 9], [0, 2, 4, 5, 9], [1, 2, 4, 5, 9],
     [0, 3, 4, 5, 9], [1, 3, 4, 5, 9], [2, 3, 4, 5, 9], [0, 1, 2, 6, 9], [0, 1, 3, 6, 9], [0, 2, 3, 6, 9],
     [1, 2, 3, 6, 9], [0, 1, 4, 6, 9], [0, 2, 4, 6, 9], [1, 2, 4, 6, 9], [0, 3, 4, 6, 9], [1, 3, 4, 6, 9],
     [2, 3, 4, 6, 9], [0, 1, 5, 6, 9], [0, 2, 5, 6, 9], [1, 2, 5, 6, 9], [0, 3, 5, 6, 9], [1, 3, 5, 6, 9],
     [2, 3, 5, 6, 9], [0, 4, 5, 6, 9], [1, 4, 5, 6, 9], [2, 4, 5, 6, 9], [3, 4, 5, 6, 9], [0, 1, 2, 7, 9],
     [0, 1, 3, 7, 9], [0, 2, 3, 7, 9], [1, 2, 3, 7, 9], [0, 1, 4, 7, 9], [0, 2, 4, 7, 9], [1, 2, 4, 7, 9],
     [0, 3, 4, 7, 9], [1, 3, 4, 7, 9], [2, 3, 4, 7, 9], [0, 1, 5, 7, 9], [0, 2, 5, 7, 9], [1, 2, 5, 7, 9],
     [0, 3, 5, 7, 9], [1, 3, 5, 7, 9], [2, 3, 5, 7, 9], [0, 4, 5, 7, 9], [1, 4, 5, 7, 9], [2, 4, 5, 7, 9],
     [3, 4, 5, 7, 9], [0, 1, 6, 7, 9], [0, 2, 6, 7, 9], [1, 2, 6, 7, 9], [0, 3, 6, 7, 9], [1, 3, 6, 7, 9],
     [2, 3, 6, 7, 9], [0, 4, 6, 7, 9], [1, 4, 6, 7, 9], [2, 4, 6, 7, 9], [3, 4, 6, 7, 9], [0, 5, 6, 7, 9],
     [1, 5, 6, 7, 9], [2, 5, 6, 7, 9], [3, 5, 6, 7, 9], [4, 5, 6, 7, 9], [0, 1, 2, 8, 9], [0, 1, 3, 8, 9],
     [0, 2, 3, 8, 9], [1, 2, 3, 8, 9], [0, 1, 4, 8, 9], [0, 2, 4, 8, 9], [1, 2, 4, 8, 9], [0, 3, 4, 8, 9],
     [1, 3, 4, 8, 9], [2, 3, 4, 8, 9], [0, 1, 5, 8, 9], [0, 2, 5, 8, 9], [1, 2, 5, 8, 9], [0, 3, 5, 8, 9],
     [1, 3, 5, 8, 9], [2, 3, 5, 8, 9], [0, 4, 5, 8, 9], [1, 4, 5, 8, 9], [2, 4, 5, 8, 9], [3, 4, 5, 8, 9],
     [0, 1, 6, 8, 9], [0, 2, 6, 8, 9], [1, 2, 6, 8, 9], [0, 3, 6, 8, 9], [1, 3, 6, 8, 9], [2, 3, 6, 8, 9],
     [0, 4, 6, 8, 9], [1, 4, 6, 8, 9], [2, 4, 6, 8, 9], [3, 4, 6, 8, 9], [0, 5, 6, 8, 9], [1, 5, 6, 8, 9],
     [2, 5, 6, 8, 9], [3, 5, 6, 8, 9], [4, 5, 6, 8, 9], [0, 1, 7, 8, 9], [0, 2, 7, 8, 9], [1, 2, 7, 8, 9],
     [0, 3, 7, 8, 9], [1, 3, 7, 8, 9], [2, 3, 7, 8, 9], [0, 4, 7, 8, 9], [1, 4, 7, 8, 9], [2, 4, 7, 8, 9],
     [3, 4, 7, 8, 9], [0, 5, 7, 8, 9], [1, 5, 7, 8, 9], [2, 5, 7, 8, 9], [3, 5, 7, 8, 9], [4, 5, 7, 8, 9],
     [0, 6, 7, 8, 9], [1, 6, 7, 8, 9], [2, 6, 7, 8, 9], [3, 6, 7, 8, 9], [4, 6, 7, 8, 9], [5, 6, 7, 8, 9],
     [0, 1, 2, 3, 10], [0, 1, 2, 4, 10], [0, 1, 3, 4, 10], [0, 2, 3, 4, 10], [1, 2, 3, 4, 10], [0, 1, 2, 5, 10],
     [0, 1, 3, 5, 10], [0, 2, 3, 5, 10], [1, 2, 3, 5, 10], [0, 1, 4, 5, 10], [0, 2, 4, 5, 10], [1, 2, 4, 5, 10],
     [0, 3, 4, 5, 10], [1, 3, 4, 5, 10], [2, 3, 4, 5, 10], [0, 1, 2, 6, 10], [0, 1, 3, 6, 10], [0, 2, 3, 6, 10],
     [1, 2, 3, 6, 10], [0, 1, 4, 6, 10], [0, 2, 4, 6, 10], [1, 2, 4, 6, 10], [0, 3, 4, 6, 10], [1, 3, 4, 6, 10],
     [2, 3, 4, 6, 10], [0, 1, 5, 6, 10], [0, 2, 5, 6, 10], [1, 2, 5, 6, 10], [0, 3, 5, 6, 10], [1, 3, 5, 6, 10],
     [2, 3, 5, 6, 10], [0, 4, 5, 6, 10], [1, 4, 5, 6, 10], [2, 4, 5, 6, 10], [3, 4, 5, 6, 10], [0, 1, 2, 7, 10],
     [0, 1, 3, 7, 10], [0, 2, 3, 7, 10], [1, 2, 3, 7, 10], [0, 1, 4, 7, 10], [0, 2, 4, 7, 10], [1, 2, 4, 7, 10],
     [0, 3, 4, 7, 10], [1, 3, 4, 7, 10], [2, 3, 4, 7, 10], [0, 1, 5, 7, 10], [0, 2, 5, 7, 10], [1, 2, 5, 7, 10],
     [0, 3, 5, 7, 10], [1, 3, 5, 7, 10], [2, 3, 5, 7, 10], [0, 4, 5, 7, 10], [1, 4, 5, 7, 10], [2, 4, 5, 7, 10],
     [3, 4, 5, 7, 10], [0, 1, 6, 7, 10], [0, 2, 6, 7, 10], [1, 2, 6, 7, 10], [0, 3, 6, 7, 10], [1, 3, 6, 7, 10],
     [2, 3, 6, 7, 10], [0, 4, 6, 7, 10], [1, 4, 6, 7, 10], [2, 4, 6, 7, 10], [3, 4, 6, 7, 10], [0, 5, 6, 7, 10],
     [1, 5, 6, 7, 10], [2, 5, 6, 7, 10], [3, 5, 6, 7, 10], [4, 5, 6, 7, 10], [0, 1, 2, 8, 10], [0, 1, 3, 8, 10],
     [0, 2, 3, 8, 10], [1, 2, 3, 8, 10], [0, 1, 4, 8, 10], [0, 2, 4, 8, 10], [1, 2, 4, 8, 10], [0, 3, 4, 8, 10],
     [1, 3, 4, 8, 10], [2, 3, 4, 8, 10], [0, 1, 5, 8, 10], [0, 2, 5, 8, 10], [1, 2, 5, 8, 10], [0, 3, 5, 8, 10],
     [1, 3, 5, 8, 10], [2, 3, 5, 8, 10], [0, 4, 5, 8, 10], [1, 4, 5, 8, 10], [2, 4, 5, 8, 10], [3, 4, 5, 8, 10],
     [0, 1, 6, 8, 10], [0, 2, 6, 8, 10], [1, 2, 6, 8, 10], [0, 3, 6, 8, 10], [1, 3, 6, 8, 10], [2, 3, 6, 8, 10],
     [0, 4, 6, 8, 10], [1, 4, 6, 8, 10], [2, 4, 6, 8, 10], [3, 4, 6, 8, 10], [0, 5, 6, 8, 10], [1, 5, 6, 8, 10],
     [2, 5, 6, 8, 10], [3, 5, 6, 8, 10], [4, 5, 6, 8, 10], [0, 1, 7, 8, 10], [0, 2, 7, 8, 10], [1, 2, 7, 8, 10],
     [0, 3, 7, 8, 10], [1, 3, 7, 8, 10], [2, 3, 7, 8, 10], [0, 4, 7, 8, 10], [1, 4, 7, 8, 10], [2, 4, 7, 8, 10],
     [3, 4, 7, 8, 10], [0, 5, 7, 8, 10], [1, 5, 7, 8, 10], [2, 5, 7, 8, 10], [3, 5, 7, 8, 10], [4, 5, 7, 8, 10],
     [0, 6, 7, 8, 10], [1, 6, 7, 8, 10], [2, 6, 7, 8, 10], [3, 6, 7, 8, 10], [4, 6, 7, 8, 10], [5, 6, 7, 8, 10],
     [0, 1, 2, 9, 10], [0, 1, 3, 9, 10], [0, 2, 3, 9, 10], [1, 2, 3, 9, 10], [0, 1, 4, 9, 10], [0, 2, 4, 9, 10],
     [1, 2, 4, 9, 10], [0, 3, 4, 9, 10], [1, 3, 4, 9, 10], [2, 3, 4, 9, 10], [0, 1, 5, 9, 10], [0, 2, 5, 9, 10],
     [1, 2, 5, 9, 10], [0, 3, 5, 9, 10], [1, 3, 5, 9, 10], [2, 3, 5, 9, 10], [0, 4, 5, 9, 10], [1, 4, 5, 9, 10],
     [2, 4, 5, 9, 10], [3, 4, 5, 9, 10], [0, 1, 6, 9, 10], [0, 2, 6, 9, 10], [1, 2, 6, 9, 10], [0, 3, 6, 9, 10],
     [1, 3, 6, 9, 10], [2, 3, 6, 9, 10], [0, 4, 6, 9, 10], [1, 4, 6, 9, 10], [2, 4, 6, 9, 10], [3, 4, 6, 9, 10],
     [0, 5, 6, 9, 10], [1, 5, 6, 9, 10], [2, 5, 6, 9, 10], [3, 5, 6, 9, 10], [4, 5, 6, 9, 10], [0, 1, 7, 9, 10],
     [0, 2, 7, 9, 10], [1, 2, 7, 9, 10], [0, 3, 7, 9, 10], [1, 3, 7, 9, 10], [2, 3, 7, 9, 10], [0, 4, 7, 9, 10],
     [1, 4, 7, 9, 10], [2, 4, 7, 9, 10], [3, 4, 7, 9, 10], [0, 5, 7, 9, 10], [1, 5, 7, 9, 10], [2, 5, 7, 9, 10],
     [3, 5, 7, 9, 10], [4, 5, 7, 9, 10], [0, 6, 7, 9, 10], [1, 6, 7, 9, 10], [2, 6, 7, 9, 10], [3, 6, 7, 9, 10],
     [4, 6, 7, 9, 10], [5, 6, 7, 9, 10], [0, 1, 8, 9, 10], [0, 2, 8, 9, 10], [1, 2, 8, 9, 10], [0, 3, 8, 9, 10],
     [1, 3, 8, 9, 10], [2, 3, 8, 9, 10], [0, 4, 8, 9, 10], [1, 4, 8, 9, 10], [2, 4, 8, 9, 10], [3, 4, 8, 9, 10],
     [0, 5, 8, 9, 10], [1, 5, 8, 9, 10], [2, 5, 8, 9, 10], [3, 5, 8, 9, 10], [4, 5, 8, 9, 10], [0, 6, 8, 9, 10],
     [1, 6, 8, 9, 10], [2, 6, 8, 9, 10], [3, 6, 8, 9, 10], [4, 6, 8, 9, 10], [5, 6, 8, 9, 10], [0, 7, 8, 9, 10],
     [1, 7, 8, 9, 10], [2, 7, 8, 9, 10], [3, 7, 8, 9, 10], [4, 7, 8, 9, 10], [5, 7, 8, 9, 10], [6, 7, 8, 9, 10]],
    [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 6], [0, 1, 2, 3, 5, 6], [0, 1, 2, 4, 5, 6], [0, 1, 3, 4, 5, 6],
     [0, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 7], [0, 1, 2, 3, 5, 7], [0, 1, 2, 4, 5, 7],
     [0, 1, 3, 4, 5, 7], [0, 2, 3, 4, 5, 7], [1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 6, 7], [0, 1, 2, 4, 6, 7],
     [0, 1, 3, 4, 6, 7], [0, 2, 3, 4, 6, 7], [1, 2, 3, 4, 6, 7], [0, 1, 2, 5, 6, 7], [0, 1, 3, 5, 6, 7],
     [0, 2, 3, 5, 6, 7], [1, 2, 3, 5, 6, 7], [0, 1, 4, 5, 6, 7], [0, 2, 4, 5, 6, 7], [1, 2, 4, 5, 6, 7],
     [0, 3, 4, 5, 6, 7], [1, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 8], [0, 1, 2, 3, 5, 8],
     [0, 1, 2, 4, 5, 8], [0, 1, 3, 4, 5, 8], [0, 2, 3, 4, 5, 8], [1, 2, 3, 4, 5, 8], [0, 1, 2, 3, 6, 8],
     [0, 1, 2, 4, 6, 8], [0, 1, 3, 4, 6, 8], [0, 2, 3, 4, 6, 8], [1, 2, 3, 4, 6, 8], [0, 1, 2, 5, 6, 8],
     [0, 1, 3, 5, 6, 8], [0, 2, 3, 5, 6, 8], [1, 2, 3, 5, 6, 8], [0, 1, 4, 5, 6, 8], [0, 2, 4, 5, 6, 8],
     [1, 2, 4, 5, 6, 8], [0, 3, 4, 5, 6, 8], [1, 3, 4, 5, 6, 8], [2, 3, 4, 5, 6, 8], [0, 1, 2, 3, 7, 8],
     [0, 1, 2, 4, 7, 8], [0, 1, 3, 4, 7, 8], [0, 2, 3, 4, 7, 8], [1, 2, 3, 4, 7, 8], [0, 1, 2, 5, 7, 8],
     [0, 1, 3, 5, 7, 8], [0, 2, 3, 5, 7, 8], [1, 2, 3, 5, 7, 8], [0, 1, 4, 5, 7, 8], [0, 2, 4, 5, 7, 8],
     [1, 2, 4, 5, 7, 8], [0, 3, 4, 5, 7, 8], [1, 3, 4, 5, 7, 8], [2, 3, 4, 5, 7, 8], [0, 1, 2, 6, 7, 8],
     [0, 1, 3, 6, 7, 8], [0, 2, 3, 6, 7, 8], [1, 2, 3, 6, 7, 8], [0, 1, 4, 6, 7, 8], [0, 2, 4, 6, 7, 8],
     [1, 2, 4, 6, 7, 8], [0, 3, 4, 6, 7, 8], [1, 3, 4, 6, 7, 8], [2, 3, 4, 6, 7, 8], [0, 1, 5, 6, 7, 8],
     [0, 2, 5, 6, 7, 8], [1, 2, 5, 6, 7, 8], [0, 3, 5, 6, 7, 8], [1, 3, 5, 6, 7, 8], [2, 3, 5, 6, 7, 8],
     [0, 4, 5, 6, 7, 8], [1, 4, 5, 6, 7, 8], [2, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 9],
     [0, 1, 2, 3, 5, 9], [0, 1, 2, 4, 5, 9], [0, 1, 3, 4, 5, 9], [0, 2, 3, 4, 5, 9], [1, 2, 3, 4, 5, 9],
     [0, 1, 2, 3, 6, 9], [0, 1, 2, 4, 6, 9], [0, 1, 3, 4, 6, 9], [0, 2, 3, 4, 6, 9], [1, 2, 3, 4, 6, 9],
     [0, 1, 2, 5, 6, 9], [0, 1, 3, 5, 6, 9], [0, 2, 3, 5, 6, 9], [1, 2, 3, 5, 6, 9], [0, 1, 4, 5, 6, 9],
     [0, 2, 4, 5, 6, 9], [1, 2, 4, 5, 6, 9], [0, 3, 4, 5, 6, 9], [1, 3, 4, 5, 6, 9], [2, 3, 4, 5, 6, 9],
     [0, 1, 2, 3, 7, 9], [0, 1, 2, 4, 7, 9], [0, 1, 3, 4, 7, 9], [0, 2, 3, 4, 7, 9], [1, 2, 3, 4, 7, 9],
     [0, 1, 2, 5, 7, 9], [0, 1, 3, 5, 7, 9], [0, 2, 3, 5, 7, 9], [1, 2, 3, 5, 7, 9], [0, 1, 4, 5, 7, 9],
     [0, 2, 4, 5, 7, 9], [1, 2, 4, 5, 7, 9], [0, 3, 4, 5, 7, 9], [1, 3, 4, 5, 7, 9], [2, 3, 4, 5, 7, 9],
     [0, 1, 2, 6, 7, 9], [0, 1, 3, 6, 7, 9], [0, 2, 3, 6, 7, 9], [1, 2, 3, 6, 7, 9], [0, 1, 4, 6, 7, 9],
     [0, 2, 4, 6, 7, 9], [1, 2, 4, 6, 7, 9], [0, 3, 4, 6, 7, 9], [1, 3, 4, 6, 7, 9], [2, 3, 4, 6, 7, 9],
     [0, 1, 5, 6, 7, 9], [0, 2, 5, 6, 7, 9], [1, 2, 5, 6, 7, 9], [0, 3, 5, 6, 7, 9], [1, 3, 5, 6, 7, 9],
     [2, 3, 5, 6, 7, 9], [0, 4, 5, 6, 7, 9], [1, 4, 5, 6, 7, 9], [2, 4, 5, 6, 7, 9], [3, 4, 5, 6, 7, 9],
     [0, 1, 2, 3, 8, 9], [0, 1, 2, 4, 8, 9], [0, 1, 3, 4, 8, 9], [0, 2, 3, 4, 8, 9], [1, 2, 3, 4, 8, 9],
     [0, 1, 2, 5, 8, 9], [0, 1, 3, 5, 8, 9], [0, 2, 3, 5, 8, 9], [1, 2, 3, 5, 8, 9], [0, 1, 4, 5, 8, 9],
     [0, 2, 4, 5, 8, 9], [1, 2, 4, 5, 8, 9], [0, 3, 4, 5, 8, 9], [1, 3, 4, 5, 8, 9], [2, 3, 4, 5, 8, 9],
     [0, 1, 2, 6, 8, 9], [0, 1, 3, 6, 8, 9], [0, 2, 3, 6, 8, 9], [1, 2, 3, 6, 8, 9], [0, 1, 4, 6, 8, 9],
     [0, 2, 4, 6, 8, 9], [1, 2, 4, 6, 8, 9], [0, 3, 4, 6, 8, 9], [1, 3, 4, 6, 8, 9], [2, 3, 4, 6, 8, 9],
     [0, 1, 5, 6, 8, 9], [0, 2, 5, 6, 8, 9], [1, 2, 5, 6, 8, 9], [0, 3, 5, 6, 8, 9], [1, 3, 5, 6, 8, 9],
     [2, 3, 5, 6, 8, 9], [0, 4, 5, 6, 8, 9], [1, 4, 5, 6, 8, 9], [2, 4, 5, 6, 8, 9], [3, 4, 5, 6, 8, 9],
     [0, 1, 2, 7, 8, 9], [0, 1, 3, 7, 8, 9], [0, 2, 3, 7, 8, 9], [1, 2, 3, 7, 8, 9], [0, 1, 4, 7, 8, 9],
     [0, 2, 4, 7, 8, 9], [1, 2, 4, 7, 8, 9], [0, 3, 4, 7, 8, 9], [1, 3, 4, 7, 8, 9], [2, 3, 4, 7, 8, 9],
     [0, 1, 5, 7, 8, 9], [0, 2, 5, 7, 8, 9], [1, 2, 5, 7, 8, 9], [0, 3, 5, 7, 8, 9], [1, 3, 5, 7, 8, 9],
     [2, 3, 5, 7, 8, 9], [0, 4, 5, 7, 8, 9], [1, 4, 5, 7, 8, 9], [2, 4, 5, 7, 8, 9], [3, 4, 5, 7, 8, 9],
     [0, 1, 6, 7, 8, 9], [0, 2, 6, 7, 8, 9], [1, 2, 6, 7, 8, 9], [0, 3, 6, 7, 8, 9], [1, 3, 6, 7, 8, 9],
     [2, 3, 6, 7, 8, 9], [0, 4, 6, 7, 8, 9], [1, 4, 6, 7, 8, 9], [2, 4, 6, 7, 8, 9], [3, 4, 6, 7, 8, 9],
     [0, 5, 6, 7, 8, 9], [1, 5, 6, 7, 8, 9], [2, 5, 6, 7, 8, 9], [3, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 10], [0, 1, 2, 3, 5, 10], [0, 1, 2, 4, 5, 10], [0, 1, 3, 4, 5, 10], [0, 2, 3, 4, 5, 10],
     [1, 2, 3, 4, 5, 10], [0, 1, 2, 3, 6, 10], [0, 1, 2, 4, 6, 10], [0, 1, 3, 4, 6, 10], [0, 2, 3, 4, 6, 10],
     [1, 2, 3, 4, 6, 10], [0, 1, 2, 5, 6, 10], [0, 1, 3, 5, 6, 10], [0, 2, 3, 5, 6, 10], [1, 2, 3, 5, 6, 10],
     [0, 1, 4, 5, 6, 10], [0, 2, 4, 5, 6, 10], [1, 2, 4, 5, 6, 10], [0, 3, 4, 5, 6, 10], [1, 3, 4, 5, 6, 10],
     [2, 3, 4, 5, 6, 10], [0, 1, 2, 3, 7, 10], [0, 1, 2, 4, 7, 10], [0, 1, 3, 4, 7, 10], [0, 2, 3, 4, 7, 10],
     [1, 2, 3, 4, 7, 10], [0, 1, 2, 5, 7, 10], [0, 1, 3, 5, 7, 10], [0, 2, 3, 5, 7, 10], [1, 2, 3, 5, 7, 10],
     [0, 1, 4, 5, 7, 10], [0, 2, 4, 5, 7, 10], [1, 2, 4, 5, 7, 10], [0, 3, 4, 5, 7, 10], [1, 3, 4, 5, 7, 10],
     [2, 3, 4, 5, 7, 10], [0, 1, 2, 6, 7, 10], [0, 1, 3, 6, 7, 10], [0, 2, 3, 6, 7, 10], [1, 2, 3, 6, 7, 10],
     [0, 1, 4, 6, 7, 10], [0, 2, 4, 6, 7, 10], [1, 2, 4, 6, 7, 10], [0, 3, 4, 6, 7, 10], [1, 3, 4, 6, 7, 10],
     [2, 3, 4, 6, 7, 10], [0, 1, 5, 6, 7, 10], [0, 2, 5, 6, 7, 10], [1, 2, 5, 6, 7, 10], [0, 3, 5, 6, 7, 10],
     [1, 3, 5, 6, 7, 10], [2, 3, 5, 6, 7, 10], [0, 4, 5, 6, 7, 10], [1, 4, 5, 6, 7, 10], [2, 4, 5, 6, 7, 10],
     [3, 4, 5, 6, 7, 10], [0, 1, 2, 3, 8, 10], [0, 1, 2, 4, 8, 10], [0, 1, 3, 4, 8, 10], [0, 2, 3, 4, 8, 10],
     [1, 2, 3, 4, 8, 10], [0, 1, 2, 5, 8, 10], [0, 1, 3, 5, 8, 10], [0, 2, 3, 5, 8, 10], [1, 2, 3, 5, 8, 10],
     [0, 1, 4, 5, 8, 10], [0, 2, 4, 5, 8, 10], [1, 2, 4, 5, 8, 10], [0, 3, 4, 5, 8, 10], [1, 3, 4, 5, 8, 10],
     [2, 3, 4, 5, 8, 10], [0, 1, 2, 6, 8, 10], [0, 1, 3, 6, 8, 10], [0, 2, 3, 6, 8, 10], [1, 2, 3, 6, 8, 10],
     [0, 1, 4, 6, 8, 10], [0, 2, 4, 6, 8, 10], [1, 2, 4, 6, 8, 10], [0, 3, 4, 6, 8, 10], [1, 3, 4, 6, 8, 10],
     [2, 3, 4, 6, 8, 10], [0, 1, 5, 6, 8, 10], [0, 2, 5, 6, 8, 10], [1, 2, 5, 6, 8, 10], [0, 3, 5, 6, 8, 10],
     [1, 3, 5, 6, 8, 10], [2, 3, 5, 6, 8, 10], [0, 4, 5, 6, 8, 10], [1, 4, 5, 6, 8, 10], [2, 4, 5, 6, 8, 10],
     [3, 4, 5, 6, 8, 10], [0, 1, 2, 7, 8, 10], [0, 1, 3, 7, 8, 10], [0, 2, 3, 7, 8, 10], [1, 2, 3, 7, 8, 10],
     [0, 1, 4, 7, 8, 10], [0, 2, 4, 7, 8, 10], [1, 2, 4, 7, 8, 10], [0, 3, 4, 7, 8, 10], [1, 3, 4, 7, 8, 10],
     [2, 3, 4, 7, 8, 10], [0, 1, 5, 7, 8, 10], [0, 2, 5, 7, 8, 10], [1, 2, 5, 7, 8, 10], [0, 3, 5, 7, 8, 10],
     [1, 3, 5, 7, 8, 10], [2, 3, 5, 7, 8, 10], [0, 4, 5, 7, 8, 10], [1, 4, 5, 7, 8, 10], [2, 4, 5, 7, 8, 10],
     [3, 4, 5, 7, 8, 10], [0, 1, 6, 7, 8, 10], [0, 2, 6, 7, 8, 10], [1, 2, 6, 7, 8, 10], [0, 3, 6, 7, 8, 10],
     [1, 3, 6, 7, 8, 10], [2, 3, 6, 7, 8, 10], [0, 4, 6, 7, 8, 10], [1, 4, 6, 7, 8, 10], [2, 4, 6, 7, 8, 10],
     [3, 4, 6, 7, 8, 10], [0, 5, 6, 7, 8, 10], [1, 5, 6, 7, 8, 10], [2, 5, 6, 7, 8, 10], [3, 5, 6, 7, 8, 10],
     [4, 5, 6, 7, 8, 10], [0, 1, 2, 3, 9, 10], [0, 1, 2, 4, 9, 10], [0, 1, 3, 4, 9, 10], [0, 2, 3, 4, 9, 10],
     [1, 2, 3, 4, 9, 10], [0, 1, 2, 5, 9, 10], [0, 1, 3, 5, 9, 10], [0, 2, 3, 5, 9, 10], [1, 2, 3, 5, 9, 10],
     [0, 1, 4, 5, 9, 10], [0, 2, 4, 5, 9, 10], [1, 2, 4, 5, 9, 10], [0, 3, 4, 5, 9, 10], [1, 3, 4, 5, 9, 10],
     [2, 3, 4, 5, 9, 10], [0, 1, 2, 6, 9, 10], [0, 1, 3, 6, 9, 10], [0, 2, 3, 6, 9, 10], [1, 2, 3, 6, 9, 10],
     [0, 1, 4, 6, 9, 10], [0, 2, 4, 6, 9, 10], [1, 2, 4, 6, 9, 10], [0, 3, 4, 6, 9, 10], [1, 3, 4, 6, 9, 10],
     [2, 3, 4, 6, 9, 10], [0, 1, 5, 6, 9, 10], [0, 2, 5, 6, 9, 10], [1, 2, 5, 6, 9, 10], [0, 3, 5, 6, 9, 10],
     [1, 3, 5, 6, 9, 10], [2, 3, 5, 6, 9, 10], [0, 4, 5, 6, 9, 10], [1, 4, 5, 6, 9, 10], [2, 4, 5, 6, 9, 10],
     [3, 4, 5, 6, 9, 10], [0, 1, 2, 7, 9, 10], [0, 1, 3, 7, 9, 10], [0, 2, 3, 7, 9, 10], [1, 2, 3, 7, 9, 10],
     [0, 1, 4, 7, 9, 10], [0, 2, 4, 7, 9, 10], [1, 2, 4, 7, 9, 10], [0, 3, 4, 7, 9, 10], [1, 3, 4, 7, 9, 10],
     [2, 3, 4, 7, 9, 10], [0, 1, 5, 7, 9, 10], [0, 2, 5, 7, 9, 10], [1, 2, 5, 7, 9, 10], [0, 3, 5, 7, 9, 10],
     [1, 3, 5, 7, 9, 10], [2, 3, 5, 7, 9, 10], [0, 4, 5, 7, 9, 10], [1, 4, 5, 7, 9, 10], [2, 4, 5, 7, 9, 10],
     [3, 4, 5, 7, 9, 10], [0, 1, 6, 7, 9, 10], [0, 2, 6, 7, 9, 10], [1, 2, 6, 7, 9, 10], [0, 3, 6, 7, 9, 10],
     [1, 3, 6, 7, 9, 10], [2, 3, 6, 7, 9, 10], [0, 4, 6, 7, 9, 10], [1, 4, 6, 7, 9, 10], [2, 4, 6, 7, 9, 10],
     [3, 4, 6, 7, 9, 10], [0, 5, 6, 7, 9, 10], [1, 5, 6, 7, 9, 10], [2, 5, 6, 7, 9, 10], [3, 5, 6, 7, 9, 10],
     [4, 5, 6, 7, 9, 10], [0, 1, 2, 8, 9, 10], [0, 1, 3, 8, 9, 10], [0, 2, 3, 8, 9, 10], [1, 2, 3, 8, 9, 10],
     [0, 1, 4, 8, 9, 10], [0, 2, 4, 8, 9, 10], [1, 2, 4, 8, 9, 10], [0, 3, 4, 8, 9, 10], [1, 3, 4, 8, 9, 10],
     [2, 3, 4, 8, 9, 10], [0, 1, 5, 8, 9, 10], [0, 2, 5, 8, 9, 10], [1, 2, 5, 8, 9, 10], [0, 3, 5, 8, 9, 10],
     [1, 3, 5, 8, 9, 10], [2, 3, 5, 8, 9, 10], [0, 4, 5, 8, 9, 10], [1, 4, 5, 8, 9, 10], [2, 4, 5, 8, 9, 10],
     [3, 4, 5, 8, 9, 10], [0, 1, 6, 8, 9, 10], [0, 2, 6, 8, 9, 10], [1, 2, 6, 8, 9, 10], [0, 3, 6, 8, 9, 10],
     [1, 3, 6, 8, 9, 10], [2, 3, 6, 8, 9, 10], [0, 4, 6, 8, 9, 10], [1, 4, 6, 8, 9, 10], [2, 4, 6, 8, 9, 10],
     [3, 4, 6, 8, 9, 10], [0, 5, 6, 8, 9, 10], [1, 5, 6, 8, 9, 10], [2, 5, 6, 8, 9, 10], [3, 5, 6, 8, 9, 10],
     [4, 5, 6, 8, 9, 10], [0, 1, 7, 8, 9, 10], [0, 2, 7, 8, 9, 10], [1, 2, 7, 8, 9, 10], [0, 3, 7, 8, 9, 10],
     [1, 3, 7, 8, 9, 10], [2, 3, 7, 8, 9, 10], [0, 4, 7, 8, 9, 10], [1, 4, 7, 8, 9, 10], [2, 4, 7, 8, 9, 10],
     [3, 4, 7, 8, 9, 10], [0, 5, 7, 8, 9, 10], [1, 5, 7, 8, 9, 10], [2, 5, 7, 8, 9, 10], [3, 5, 7, 8, 9, 10],
     [4, 5, 7, 8, 9, 10], [0, 6, 7, 8, 9, 10], [1, 6, 7, 8, 9, 10], [2, 6, 7, 8, 9, 10], [3, 6, 7, 8, 9, 10],
     [4, 6, 7, 8, 9, 10], [5, 6, 7, 8, 9, 10]],
    [[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 6, 7], [0, 1, 2, 3, 5, 6, 7], [0, 1, 2, 4, 5, 6, 7],
     [0, 1, 3, 4, 5, 6, 7], [0, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 8], [0, 1, 2, 3, 4, 6, 8],
     [0, 1, 2, 3, 5, 6, 8], [0, 1, 2, 4, 5, 6, 8], [0, 1, 3, 4, 5, 6, 8], [0, 2, 3, 4, 5, 6, 8], [1, 2, 3, 4, 5, 6, 8],
     [0, 1, 2, 3, 4, 7, 8], [0, 1, 2, 3, 5, 7, 8], [0, 1, 2, 4, 5, 7, 8], [0, 1, 3, 4, 5, 7, 8], [0, 2, 3, 4, 5, 7, 8],
     [1, 2, 3, 4, 5, 7, 8], [0, 1, 2, 3, 6, 7, 8], [0, 1, 2, 4, 6, 7, 8], [0, 1, 3, 4, 6, 7, 8], [0, 2, 3, 4, 6, 7, 8],
     [1, 2, 3, 4, 6, 7, 8], [0, 1, 2, 5, 6, 7, 8], [0, 1, 3, 5, 6, 7, 8], [0, 2, 3, 5, 6, 7, 8], [1, 2, 3, 5, 6, 7, 8],
     [0, 1, 4, 5, 6, 7, 8], [0, 2, 4, 5, 6, 7, 8], [1, 2, 4, 5, 6, 7, 8], [0, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8],
     [2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 9], [0, 1, 2, 3, 4, 6, 9], [0, 1, 2, 3, 5, 6, 9], [0, 1, 2, 4, 5, 6, 9],
     [0, 1, 3, 4, 5, 6, 9], [0, 2, 3, 4, 5, 6, 9], [1, 2, 3, 4, 5, 6, 9], [0, 1, 2, 3, 4, 7, 9], [0, 1, 2, 3, 5, 7, 9],
     [0, 1, 2, 4, 5, 7, 9], [0, 1, 3, 4, 5, 7, 9], [0, 2, 3, 4, 5, 7, 9], [1, 2, 3, 4, 5, 7, 9], [0, 1, 2, 3, 6, 7, 9],
     [0, 1, 2, 4, 6, 7, 9], [0, 1, 3, 4, 6, 7, 9], [0, 2, 3, 4, 6, 7, 9], [1, 2, 3, 4, 6, 7, 9], [0, 1, 2, 5, 6, 7, 9],
     [0, 1, 3, 5, 6, 7, 9], [0, 2, 3, 5, 6, 7, 9], [1, 2, 3, 5, 6, 7, 9], [0, 1, 4, 5, 6, 7, 9], [0, 2, 4, 5, 6, 7, 9],
     [1, 2, 4, 5, 6, 7, 9], [0, 3, 4, 5, 6, 7, 9], [1, 3, 4, 5, 6, 7, 9], [2, 3, 4, 5, 6, 7, 9], [0, 1, 2, 3, 4, 8, 9],
     [0, 1, 2, 3, 5, 8, 9], [0, 1, 2, 4, 5, 8, 9], [0, 1, 3, 4, 5, 8, 9], [0, 2, 3, 4, 5, 8, 9], [1, 2, 3, 4, 5, 8, 9],
     [0, 1, 2, 3, 6, 8, 9], [0, 1, 2, 4, 6, 8, 9], [0, 1, 3, 4, 6, 8, 9], [0, 2, 3, 4, 6, 8, 9], [1, 2, 3, 4, 6, 8, 9],
     [0, 1, 2, 5, 6, 8, 9], [0, 1, 3, 5, 6, 8, 9], [0, 2, 3, 5, 6, 8, 9], [1, 2, 3, 5, 6, 8, 9], [0, 1, 4, 5, 6, 8, 9],
     [0, 2, 4, 5, 6, 8, 9], [1, 2, 4, 5, 6, 8, 9], [0, 3, 4, 5, 6, 8, 9], [1, 3, 4, 5, 6, 8, 9], [2, 3, 4, 5, 6, 8, 9],
     [0, 1, 2, 3, 7, 8, 9], [0, 1, 2, 4, 7, 8, 9], [0, 1, 3, 4, 7, 8, 9], [0, 2, 3, 4, 7, 8, 9], [1, 2, 3, 4, 7, 8, 9],
     [0, 1, 2, 5, 7, 8, 9], [0, 1, 3, 5, 7, 8, 9], [0, 2, 3, 5, 7, 8, 9], [1, 2, 3, 5, 7, 8, 9], [0, 1, 4, 5, 7, 8, 9],
     [0, 2, 4, 5, 7, 8, 9], [1, 2, 4, 5, 7, 8, 9], [0, 3, 4, 5, 7, 8, 9], [1, 3, 4, 5, 7, 8, 9], [2, 3, 4, 5, 7, 8, 9],
     [0, 1, 2, 6, 7, 8, 9], [0, 1, 3, 6, 7, 8, 9], [0, 2, 3, 6, 7, 8, 9], [1, 2, 3, 6, 7, 8, 9], [0, 1, 4, 6, 7, 8, 9],
     [0, 2, 4, 6, 7, 8, 9], [1, 2, 4, 6, 7, 8, 9], [0, 3, 4, 6, 7, 8, 9], [1, 3, 4, 6, 7, 8, 9], [2, 3, 4, 6, 7, 8, 9],
     [0, 1, 5, 6, 7, 8, 9], [0, 2, 5, 6, 7, 8, 9], [1, 2, 5, 6, 7, 8, 9], [0, 3, 5, 6, 7, 8, 9], [1, 3, 5, 6, 7, 8, 9],
     [2, 3, 5, 6, 7, 8, 9], [0, 4, 5, 6, 7, 8, 9], [1, 4, 5, 6, 7, 8, 9], [2, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 10], [0, 1, 2, 3, 4, 6, 10], [0, 1, 2, 3, 5, 6, 10], [0, 1, 2, 4, 5, 6, 10],
     [0, 1, 3, 4, 5, 6, 10], [0, 2, 3, 4, 5, 6, 10], [1, 2, 3, 4, 5, 6, 10], [0, 1, 2, 3, 4, 7, 10],
     [0, 1, 2, 3, 5, 7, 10], [0, 1, 2, 4, 5, 7, 10], [0, 1, 3, 4, 5, 7, 10], [0, 2, 3, 4, 5, 7, 10],
     [1, 2, 3, 4, 5, 7, 10], [0, 1, 2, 3, 6, 7, 10], [0, 1, 2, 4, 6, 7, 10], [0, 1, 3, 4, 6, 7, 10],
     [0, 2, 3, 4, 6, 7, 10], [1, 2, 3, 4, 6, 7, 10], [0, 1, 2, 5, 6, 7, 10], [0, 1, 3, 5, 6, 7, 10],
     [0, 2, 3, 5, 6, 7, 10], [1, 2, 3, 5, 6, 7, 10], [0, 1, 4, 5, 6, 7, 10], [0, 2, 4, 5, 6, 7, 10],
     [1, 2, 4, 5, 6, 7, 10], [0, 3, 4, 5, 6, 7, 10], [1, 3, 4, 5, 6, 7, 10], [2, 3, 4, 5, 6, 7, 10],
     [0, 1, 2, 3, 4, 8, 10], [0, 1, 2, 3, 5, 8, 10], [0, 1, 2, 4, 5, 8, 10], [0, 1, 3, 4, 5, 8, 10],
     [0, 2, 3, 4, 5, 8, 10], [1, 2, 3, 4, 5, 8, 10], [0, 1, 2, 3, 6, 8, 10], [0, 1, 2, 4, 6, 8, 10],
     [0, 1, 3, 4, 6, 8, 10], [0, 2, 3, 4, 6, 8, 10], [1, 2, 3, 4, 6, 8, 10], [0, 1, 2, 5, 6, 8, 10],
     [0, 1, 3, 5, 6, 8, 10], [0, 2, 3, 5, 6, 8, 10], [1, 2, 3, 5, 6, 8, 10], [0, 1, 4, 5, 6, 8, 10],
     [0, 2, 4, 5, 6, 8, 10], [1, 2, 4, 5, 6, 8, 10], [0, 3, 4, 5, 6, 8, 10], [1, 3, 4, 5, 6, 8, 10],
     [2, 3, 4, 5, 6, 8, 10], [0, 1, 2, 3, 7, 8, 10], [0, 1, 2, 4, 7, 8, 10], [0, 1, 3, 4, 7, 8, 10],
     [0, 2, 3, 4, 7, 8, 10], [1, 2, 3, 4, 7, 8, 10], [0, 1, 2, 5, 7, 8, 10], [0, 1, 3, 5, 7, 8, 10],
     [0, 2, 3, 5, 7, 8, 10], [1, 2, 3, 5, 7, 8, 10], [0, 1, 4, 5, 7, 8, 10], [0, 2, 4, 5, 7, 8, 10],
     [1, 2, 4, 5, 7, 8, 10], [0, 3, 4, 5, 7, 8, 10], [1, 3, 4, 5, 7, 8, 10], [2, 3, 4, 5, 7, 8, 10],
     [0, 1, 2, 6, 7, 8, 10], [0, 1, 3, 6, 7, 8, 10], [0, 2, 3, 6, 7, 8, 10], [1, 2, 3, 6, 7, 8, 10],
     [0, 1, 4, 6, 7, 8, 10], [0, 2, 4, 6, 7, 8, 10], [1, 2, 4, 6, 7, 8, 10], [0, 3, 4, 6, 7, 8, 10],
     [1, 3, 4, 6, 7, 8, 10], [2, 3, 4, 6, 7, 8, 10], [0, 1, 5, 6, 7, 8, 10], [0, 2, 5, 6, 7, 8, 10],
     [1, 2, 5, 6, 7, 8, 10], [0, 3, 5, 6, 7, 8, 10], [1, 3, 5, 6, 7, 8, 10], [2, 3, 5, 6, 7, 8, 10],
     [0, 4, 5, 6, 7, 8, 10], [1, 4, 5, 6, 7, 8, 10], [2, 4, 5, 6, 7, 8, 10], [3, 4, 5, 6, 7, 8, 10],
     [0, 1, 2, 3, 4, 9, 10], [0, 1, 2, 3, 5, 9, 10], [0, 1, 2, 4, 5, 9, 10], [0, 1, 3, 4, 5, 9, 10],
     [0, 2, 3, 4, 5, 9, 10], [1, 2, 3, 4, 5, 9, 10], [0, 1, 2, 3, 6, 9, 10], [0, 1, 2, 4, 6, 9, 10],
     [0, 1, 3, 4, 6, 9, 10], [0, 2, 3, 4, 6, 9, 10], [1, 2, 3, 4, 6, 9, 10], [0, 1, 2, 5, 6, 9, 10],
     [0, 1, 3, 5, 6, 9, 10], [0, 2, 3, 5, 6, 9, 10], [1, 2, 3, 5, 6, 9, 10], [0, 1, 4, 5, 6, 9, 10],
     [0, 2, 4, 5, 6, 9, 10], [1, 2, 4, 5, 6, 9, 10], [0, 3, 4, 5, 6, 9, 10], [1, 3, 4, 5, 6, 9, 10],
     [2, 3, 4, 5, 6, 9, 10], [0, 1, 2, 3, 7, 9, 10], [0, 1, 2, 4, 7, 9, 10], [0, 1, 3, 4, 7, 9, 10],
     [0, 2, 3, 4, 7, 9, 10], [1, 2, 3, 4, 7, 9, 10], [0, 1, 2, 5, 7, 9, 10], [0, 1, 3, 5, 7, 9, 10],
     [0, 2, 3, 5, 7, 9, 10], [1, 2, 3, 5, 7, 9, 10], [0, 1, 4, 5, 7, 9, 10], [0, 2, 4, 5, 7, 9, 10],
     [1, 2, 4, 5, 7, 9, 10], [0, 3, 4, 5, 7, 9, 10], [1, 3, 4, 5, 7, 9, 10], [2, 3, 4, 5, 7, 9, 10],
     [0, 1, 2, 6, 7, 9, 10], [0, 1, 3, 6, 7, 9, 10], [0, 2, 3, 6, 7, 9, 10], [1, 2, 3, 6, 7, 9, 10],
     [0, 1, 4, 6, 7, 9, 10], [0, 2, 4, 6, 7, 9, 10], [1, 2, 4, 6, 7, 9, 10], [0, 3, 4, 6, 7, 9, 10],
     [1, 3, 4, 6, 7, 9, 10], [2, 3, 4, 6, 7, 9, 10], [0, 1, 5, 6, 7, 9, 10], [0, 2, 5, 6, 7, 9, 10],
     [1, 2, 5, 6, 7, 9, 10], [0, 3, 5, 6, 7, 9, 10], [1, 3, 5, 6, 7, 9, 10], [2, 3, 5, 6, 7, 9, 10],
     [0, 4, 5, 6, 7, 9, 10], [1, 4, 5, 6, 7, 9, 10], [2, 4, 5, 6, 7, 9, 10], [3, 4, 5, 6, 7, 9, 10],
     [0, 1, 2, 3, 8, 9, 10], [0, 1, 2, 4, 8, 9, 10], [0, 1, 3, 4, 8, 9, 10], [0, 2, 3, 4, 8, 9, 10],
     [1, 2, 3, 4, 8, 9, 10], [0, 1, 2, 5, 8, 9, 10], [0, 1, 3, 5, 8, 9, 10], [0, 2, 3, 5, 8, 9, 10],
     [1, 2, 3, 5, 8, 9, 10], [0, 1, 4, 5, 8, 9, 10], [0, 2, 4, 5, 8, 9, 10], [1, 2, 4, 5, 8, 9, 10],
     [0, 3, 4, 5, 8, 9, 10], [1, 3, 4, 5, 8, 9, 10], [2, 3, 4, 5, 8, 9, 10], [0, 1, 2, 6, 8, 9, 10],
     [0, 1, 3, 6, 8, 9, 10], [0, 2, 3, 6, 8, 9, 10], [1, 2, 3, 6, 8, 9, 10], [0, 1, 4, 6, 8, 9, 10],
     [0, 2, 4, 6, 8, 9, 10], [1, 2, 4, 6, 8, 9, 10], [0, 3, 4, 6, 8, 9, 10], [1, 3, 4, 6, 8, 9, 10],
     [2, 3, 4, 6, 8, 9, 10], [0, 1, 5, 6, 8, 9, 10], [0, 2, 5, 6, 8, 9, 10], [1, 2, 5, 6, 8, 9, 10],
     [0, 3, 5, 6, 8, 9, 10], [1, 3, 5, 6, 8, 9, 10], [2, 3, 5, 6, 8, 9, 10], [0, 4, 5, 6, 8, 9, 10],
     [1, 4, 5, 6, 8, 9, 10], [2, 4, 5, 6, 8, 9, 10], [3, 4, 5, 6, 8, 9, 10], [0, 1, 2, 7, 8, 9, 10],
     [0, 1, 3, 7, 8, 9, 10], [0, 2, 3, 7, 8, 9, 10], [1, 2, 3, 7, 8, 9, 10], [0, 1, 4, 7, 8, 9, 10],
     [0, 2, 4, 7, 8, 9, 10], [1, 2, 4, 7, 8, 9, 10], [0, 3, 4, 7, 8, 9, 10], [1, 3, 4, 7, 8, 9, 10],
     [2, 3, 4, 7, 8, 9, 10], [0, 1, 5, 7, 8, 9, 10], [0, 2, 5, 7, 8, 9, 10], [1, 2, 5, 7, 8, 9, 10],
     [0, 3, 5, 7, 8, 9, 10], [1, 3, 5, 7, 8, 9, 10], [2, 3, 5, 7, 8, 9, 10], [0, 4, 5, 7, 8, 9, 10],
     [1, 4, 5, 7, 8, 9, 10], [2, 4, 5, 7, 8, 9, 10], [3, 4, 5, 7, 8, 9, 10], [0, 1, 6, 7, 8, 9, 10],
     [0, 2, 6, 7, 8, 9, 10], [1, 2, 6, 7, 8, 9, 10], [0, 3, 6, 7, 8, 9, 10], [1, 3, 6, 7, 8, 9, 10],
     [2, 3, 6, 7, 8, 9, 10], [0, 4, 6, 7, 8, 9, 10], [1, 4, 6, 7, 8, 9, 10], [2, 4, 6, 7, 8, 9, 10],
     [3, 4, 6, 7, 8, 9, 10], [0, 5, 6, 7, 8, 9, 10], [1, 5, 6, 7, 8, 9, 10], [2, 5, 6, 7, 8, 9, 10],
     [3, 5, 6, 7, 8, 9, 10], [4, 5, 6, 7, 8, 9, 10]],
    [[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 8], [0, 1, 2, 3, 4, 5, 7, 8], [0, 1, 2, 3, 4, 6, 7, 8],
     [0, 1, 2, 3, 5, 6, 7, 8], [0, 1, 2, 4, 5, 6, 7, 8], [0, 1, 3, 4, 5, 6, 7, 8], [0, 2, 3, 4, 5, 6, 7, 8],
     [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 9], [0, 1, 2, 3, 4, 5, 7, 9], [0, 1, 2, 3, 4, 6, 7, 9],
     [0, 1, 2, 3, 5, 6, 7, 9], [0, 1, 2, 4, 5, 6, 7, 9], [0, 1, 3, 4, 5, 6, 7, 9], [0, 2, 3, 4, 5, 6, 7, 9],
     [1, 2, 3, 4, 5, 6, 7, 9], [0, 1, 2, 3, 4, 5, 8, 9], [0, 1, 2, 3, 4, 6, 8, 9], [0, 1, 2, 3, 5, 6, 8, 9],
     [0, 1, 2, 4, 5, 6, 8, 9], [0, 1, 3, 4, 5, 6, 8, 9], [0, 2, 3, 4, 5, 6, 8, 9], [1, 2, 3, 4, 5, 6, 8, 9],
     [0, 1, 2, 3, 4, 7, 8, 9], [0, 1, 2, 3, 5, 7, 8, 9], [0, 1, 2, 4, 5, 7, 8, 9], [0, 1, 3, 4, 5, 7, 8, 9],
     [0, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [0, 1, 2, 3, 6, 7, 8, 9], [0, 1, 2, 4, 6, 7, 8, 9],
     [0, 1, 3, 4, 6, 7, 8, 9], [0, 2, 3, 4, 6, 7, 8, 9], [1, 2, 3, 4, 6, 7, 8, 9], [0, 1, 2, 5, 6, 7, 8, 9],
     [0, 1, 3, 5, 6, 7, 8, 9], [0, 2, 3, 5, 6, 7, 8, 9], [1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 4, 5, 6, 7, 8, 9],
     [0, 2, 4, 5, 6, 7, 8, 9], [1, 2, 4, 5, 6, 7, 8, 9], [0, 3, 4, 5, 6, 7, 8, 9], [1, 3, 4, 5, 6, 7, 8, 9],
     [2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 10], [0, 1, 2, 3, 4, 5, 7, 10], [0, 1, 2, 3, 4, 6, 7, 10],
     [0, 1, 2, 3, 5, 6, 7, 10], [0, 1, 2, 4, 5, 6, 7, 10], [0, 1, 3, 4, 5, 6, 7, 10], [0, 2, 3, 4, 5, 6, 7, 10],
     [1, 2, 3, 4, 5, 6, 7, 10], [0, 1, 2, 3, 4, 5, 8, 10], [0, 1, 2, 3, 4, 6, 8, 10], [0, 1, 2, 3, 5, 6, 8, 10],
     [0, 1, 2, 4, 5, 6, 8, 10], [0, 1, 3, 4, 5, 6, 8, 10], [0, 2, 3, 4, 5, 6, 8, 10], [1, 2, 3, 4, 5, 6, 8, 10],
     [0, 1, 2, 3, 4, 7, 8, 10], [0, 1, 2, 3, 5, 7, 8, 10], [0, 1, 2, 4, 5, 7, 8, 10], [0, 1, 3, 4, 5, 7, 8, 10],
     [0, 2, 3, 4, 5, 7, 8, 10], [1, 2, 3, 4, 5, 7, 8, 10], [0, 1, 2, 3, 6, 7, 8, 10], [0, 1, 2, 4, 6, 7, 8, 10],
     [0, 1, 3, 4, 6, 7, 8, 10], [0, 2, 3, 4, 6, 7, 8, 10], [1, 2, 3, 4, 6, 7, 8, 10], [0, 1, 2, 5, 6, 7, 8, 10],
     [0, 1, 3, 5, 6, 7, 8, 10], [0, 2, 3, 5, 6, 7, 8, 10], [1, 2, 3, 5, 6, 7, 8, 10], [0, 1, 4, 5, 6, 7, 8, 10],
     [0, 2, 4, 5, 6, 7, 8, 10], [1, 2, 4, 5, 6, 7, 8, 10], [0, 3, 4, 5, 6, 7, 8, 10], [1, 3, 4, 5, 6, 7, 8, 10],
     [2, 3, 4, 5, 6, 7, 8, 10], [0, 1, 2, 3, 4, 5, 9, 10], [0, 1, 2, 3, 4, 6, 9, 10], [0, 1, 2, 3, 5, 6, 9, 10],
     [0, 1, 2, 4, 5, 6, 9, 10], [0, 1, 3, 4, 5, 6, 9, 10], [0, 2, 3, 4, 5, 6, 9, 10], [1, 2, 3, 4, 5, 6, 9, 10],
     [0, 1, 2, 3, 4, 7, 9, 10], [0, 1, 2, 3, 5, 7, 9, 10], [0, 1, 2, 4, 5, 7, 9, 10], [0, 1, 3, 4, 5, 7, 9, 10],
     [0, 2, 3, 4, 5, 7, 9, 10], [1, 2, 3, 4, 5, 7, 9, 10], [0, 1, 2, 3, 6, 7, 9, 10], [0, 1, 2, 4, 6, 7, 9, 10],
     [0, 1, 3, 4, 6, 7, 9, 10], [0, 2, 3, 4, 6, 7, 9, 10], [1, 2, 3, 4, 6, 7, 9, 10], [0, 1, 2, 5, 6, 7, 9, 10],
     [0, 1, 3, 5, 6, 7, 9, 10], [0, 2, 3, 5, 6, 7, 9, 10], [1, 2, 3, 5, 6, 7, 9, 10], [0, 1, 4, 5, 6, 7, 9, 10],
     [0, 2, 4, 5, 6, 7, 9, 10], [1, 2, 4, 5, 6, 7, 9, 10], [0, 3, 4, 5, 6, 7, 9, 10], [1, 3, 4, 5, 6, 7, 9, 10],
     [2, 3, 4, 5, 6, 7, 9, 10], [0, 1, 2, 3, 4, 8, 9, 10], [0, 1, 2, 3, 5, 8, 9, 10], [0, 1, 2, 4, 5, 8, 9, 10],
     [0, 1, 3, 4, 5, 8, 9, 10], [0, 2, 3, 4, 5, 8, 9, 10], [1, 2, 3, 4, 5, 8, 9, 10], [0, 1, 2, 3, 6, 8, 9, 10],
     [0, 1, 2, 4, 6, 8, 9, 10], [0, 1, 3, 4, 6, 8, 9, 10], [0, 2, 3, 4, 6, 8, 9, 10], [1, 2, 3, 4, 6, 8, 9, 10],
     [0, 1, 2, 5, 6, 8, 9, 10], [0, 1, 3, 5, 6, 8, 9, 10], [0, 2, 3, 5, 6, 8, 9, 10], [1, 2, 3, 5, 6, 8, 9, 10],
     [0, 1, 4, 5, 6, 8, 9, 10], [0, 2, 4, 5, 6, 8, 9, 10], [1, 2, 4, 5, 6, 8, 9, 10], [0, 3, 4, 5, 6, 8, 9, 10],
     [1, 3, 4, 5, 6, 8, 9, 10], [2, 3, 4, 5, 6, 8, 9, 10], [0, 1, 2, 3, 7, 8, 9, 10], [0, 1, 2, 4, 7, 8, 9, 10],
     [0, 1, 3, 4, 7, 8, 9, 10], [0, 2, 3, 4, 7, 8, 9, 10], [1, 2, 3, 4, 7, 8, 9, 10], [0, 1, 2, 5, 7, 8, 9, 10],
     [0, 1, 3, 5, 7, 8, 9, 10], [0, 2, 3, 5, 7, 8, 9, 10], [1, 2, 3, 5, 7, 8, 9, 10], [0, 1, 4, 5, 7, 8, 9, 10],
     [0, 2, 4, 5, 7, 8, 9, 10], [1, 2, 4, 5, 7, 8, 9, 10], [0, 3, 4, 5, 7, 8, 9, 10], [1, 3, 4, 5, 7, 8, 9, 10],
     [2, 3, 4, 5, 7, 8, 9, 10], [0, 1, 2, 6, 7, 8, 9, 10], [0, 1, 3, 6, 7, 8, 9, 10], [0, 2, 3, 6, 7, 8, 9, 10],
     [1, 2, 3, 6, 7, 8, 9, 10], [0, 1, 4, 6, 7, 8, 9, 10], [0, 2, 4, 6, 7, 8, 9, 10], [1, 2, 4, 6, 7, 8, 9, 10],
     [0, 3, 4, 6, 7, 8, 9, 10], [1, 3, 4, 6, 7, 8, 9, 10], [2, 3, 4, 6, 7, 8, 9, 10], [0, 1, 5, 6, 7, 8, 9, 10],
     [0, 2, 5, 6, 7, 8, 9, 10], [1, 2, 5, 6, 7, 8, 9, 10], [0, 3, 5, 6, 7, 8, 9, 10], [1, 3, 5, 6, 7, 8, 9, 10],
     [2, 3, 5, 6, 7, 8, 9, 10], [0, 4, 5, 6, 7, 8, 9, 10], [1, 4, 5, 6, 7, 8, 9, 10], [2, 4, 5, 6, 7, 8, 9, 10],
     [3, 4, 5, 6, 7, 8, 9, 10]],
    [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 9], [0, 1, 2, 3, 4, 5, 6, 8, 9], [0, 1, 2, 3, 4, 5, 7, 8, 9],
     [0, 1, 2, 3, 4, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9],
     [0, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 10],
     [0, 1, 2, 3, 4, 5, 6, 8, 10], [0, 1, 2, 3, 4, 5, 7, 8, 10], [0, 1, 2, 3, 4, 6, 7, 8, 10],
     [0, 1, 2, 3, 5, 6, 7, 8, 10], [0, 1, 2, 4, 5, 6, 7, 8, 10], [0, 1, 3, 4, 5, 6, 7, 8, 10],
     [0, 2, 3, 4, 5, 6, 7, 8, 10], [1, 2, 3, 4, 5, 6, 7, 8, 10], [0, 1, 2, 3, 4, 5, 6, 9, 10],
     [0, 1, 2, 3, 4, 5, 7, 9, 10], [0, 1, 2, 3, 4, 6, 7, 9, 10], [0, 1, 2, 3, 5, 6, 7, 9, 10],
     [0, 1, 2, 4, 5, 6, 7, 9, 10], [0, 1, 3, 4, 5, 6, 7, 9, 10], [0, 2, 3, 4, 5, 6, 7, 9, 10],
     [1, 2, 3, 4, 5, 6, 7, 9, 10], [0, 1, 2, 3, 4, 5, 8, 9, 10], [0, 1, 2, 3, 4, 6, 8, 9, 10],
     [0, 1, 2, 3, 5, 6, 8, 9, 10], [0, 1, 2, 4, 5, 6, 8, 9, 10], [0, 1, 3, 4, 5, 6, 8, 9, 10],
     [0, 2, 3, 4, 5, 6, 8, 9, 10], [1, 2, 3, 4, 5, 6, 8, 9, 10], [0, 1, 2, 3, 4, 7, 8, 9, 10],
     [0, 1, 2, 3, 5, 7, 8, 9, 10], [0, 1, 2, 4, 5, 7, 8, 9, 10], [0, 1, 3, 4, 5, 7, 8, 9, 10],
     [0, 2, 3, 4, 5, 7, 8, 9, 10], [1, 2, 3, 4, 5, 7, 8, 9, 10], [0, 1, 2, 3, 6, 7, 8, 9, 10],
     [0, 1, 2, 4, 6, 7, 8, 9, 10], [0, 1, 3, 4, 6, 7, 8, 9, 10], [0, 2, 3, 4, 6, 7, 8, 9, 10],
     [1, 2, 3, 4, 6, 7, 8, 9, 10], [0, 1, 2, 5, 6, 7, 8, 9, 10], [0, 1, 3, 5, 6, 7, 8, 9, 10],
     [0, 2, 3, 5, 6, 7, 8, 9, 10], [1, 2, 3, 5, 6, 7, 8, 9, 10], [0, 1, 4, 5, 6, 7, 8, 9, 10],
     [0, 2, 4, 5, 6, 7, 8, 9, 10], [1, 2, 4, 5, 6, 7, 8, 9, 10], [0, 3, 4, 5, 6, 7, 8, 9, 10],
     [1, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10]],
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 10], [0, 1, 2, 3, 4, 5, 6, 7, 9, 10],
     [0, 1, 2, 3, 4, 5, 6, 8, 9, 10], [0, 1, 2, 3, 4, 5, 7, 8, 9, 10], [0, 1, 2, 3, 4, 6, 7, 8, 9, 10],
     [0, 1, 2, 3, 5, 6, 7, 8, 9, 10], [0, 1, 2, 4, 5, 6, 7, 8, 9, 10], [0, 1, 3, 4, 5, 6, 7, 8, 9, 10],
     [0, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
]

if __name__ == '__main__':
    unittest.main()
