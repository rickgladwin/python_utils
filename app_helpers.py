import re


# helpers for interpreting/handling routes and request data

def string_object_to_object(string_object: str) -> dict:
    # TODO: if is string object, convert to dict
    return {"key1":"value 1"}


def is_string_object(source_string: str) -> bool:
    # TODO: use a regex to determine object/POJO/JSON format
    # non_json_object_regex: str = '{( ?.+: ?[\'\"]?.+[\'\"]?,?)+}'
    optional_json_object_regex: str = '{( ?[\'\"]?.+[\'\"]? ?: ?[\'\"]?.+[\'\"]?,? ?)+}'
    result = re.search(optional_json_object_regex, source_string)
    return result is not None
    # return len(result.group(0)) > 0
