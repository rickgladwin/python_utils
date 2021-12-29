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


class IsStringObjectTest(unittest.TestCase):
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


class IsStringJsonObjectTest(unittest.TestCase):
    def test_determines_that_a_json_string_with_string_values_is_a_json_object(self):
        source_string: str = '{ "key1": "value 1", "key2": "value 2" }'
        expected_result: bool = True

        result: bool = a.is_string_json_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_a_spaceless_json_string_with_string_values_is_a_json_object(self):
        source_string: str = '{"key1":"value 1","key2":"value 2"}'
        expected_result: bool = True

        result: bool = a.is_string_json_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_a_json_string_with_int_values_is_a_json_object(self):
        source_string: str = '{ "key1": 123, "key2": 234 }'
        expected_result: bool = True

        result: bool = a.is_string_json_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_an_object_string_with_unquoted_keys_is_not_a_json_object(self):
        source_string: str = '{ key1: 123, key2: 234 }'
        expected_result: bool = False

        result: bool = a.is_string_json_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_a_json_string_with_reversed_quotation_marks_is_not_a_json_object(self):
        source_string: str = "{'key1':'value 1','key2':'value 2'}"
        expected_result: bool = False

        result: bool = a.is_string_json_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_an_int_string_is_not_a_json_object(self):
        source_string: str = "12345"
        expected_result: bool = False

        result: bool = a.is_string_object(source_string)

        self.assertEqual(expected_result, result)

    def test_determines_that_a_char_string_is_not_a_json_object(self):
        source_string: str = "hello there"
        expected_result: bool = False

        result: bool = a.is_string_object(source_string)

        self.assertEqual(expected_result, result)


class StringJsonObjectToDictTest(unittest.TestCase):
    def test_converts_a_json_string_with_string_values_to_a_dict(self):
        source_string: str = '{ "key1": "value 1", "key2": "value 2" }'
        expected_result: dict = {'key1':'value 1', 'key2':'value 2'}

        result: dict = a.string_json_object_to_dict(source_string)

        self.assertEqual(expected_result, result)

    def test_converts_a_spaceless_json_string_with_string_values_to_a_dict(self):
        source_string: str = '{"key1":"value 1","key2":"value 2"}'
        expected_result: dict = {'key1':'value 1', 'key2':'value 2'}

        result: dict = a.string_json_object_to_dict(source_string)

        self.assertEqual(expected_result, result)

    def test_throws_an_error_if_given_a_non_json_object_string(self):
        source_string: str = "{key1:1,key2:2}"
        try:
            a.string_json_object_to_dict(source_string)
        except ValueError:
            self.assertTrue(1, 1)
            return
        self.fail('no exception raised')

    def test_throws_an_error_if_given_an_int_string(self):
        source_string: str = "12345"
        try:
            a.string_json_object_to_dict(source_string)
        except ValueError:
            self.assertTrue(1, 1)
            return
        self.fail('no exception raised')

    def returns_a_char_string_unchanged(self):
        source_string: str = "hello there"
        try:
            a.string_json_object_to_dict(source_string)
        except ValueError:
            self.assertTrue(1, 1)
            return
        self.fail('no exception raised')
