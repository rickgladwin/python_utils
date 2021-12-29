import unittest
import app_helpers as a

# to run:
# from project root:
# python -m unittest discover -s modules -p "*_test.py" --verbose

# to run using green:
# from project root:
# green
# target specific test (in general, dotted names):
# green modules.combinations_test.CombinationsTest
# green modules.combinations_test.NChooseRTest


class StringObjectToDictTest(unittest.TestCase):
    def test_determines_that_a_non_json_string_with_string_values_is_an_object(self):
        source_string: str = "{ key1: 'value 1', key2: 'value 2' }"
        expected_result: bool = True

        result: bool = a.is_string_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_a_json_string_with_string_values_is_an_object(self):
        source_string: str = "{ 'key1': 'value 1', 'key2': 'value 2' }"
        expected_result: bool = True

        result: bool = a.is_string_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_a_non_json_string_with_int_values_is_an_object(self):
        source_string: str = "{ key1: 1, key2: 2 }"
        expected_result: bool = True

        result: bool = a.is_string_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_a_spaceless_non_json_string_with_string_values_is_an_object(self):
        source_string: str = "{key1:'value 1',key2:'value 2'}"
        expected_result: bool = True

        result: bool = a.is_string_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_a_spaceless_json_string_with_string_values_is_an_object(self):
        source_string: str = "{'key1':'value 1','key2':'value 2'}"
        expected_result: bool = True

        result: bool = a.is_string_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_a_spaceless_non_json_string_with_int_values_is_an_object(self):
        source_string: str = "{key1:1,key2:2}"
        expected_result: bool = True

        result: bool = a.is_string_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_an_int_string_is_not_an_object(self):
        source_string: str = "12345"
        expected_result: bool = False

        result: bool = a.is_string_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_a_char_string_is_not_an_object(self):
        source_string: str = "hello there"
        expected_result: bool = False

        result: bool = a.is_string_object(source_string)

        self.assertEqual(expected_result, result)
