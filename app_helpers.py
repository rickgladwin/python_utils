import json
import re


# helpers for interpreting/handling routes and request data

def string_object_to_dict(string_object: str) -> dict:
    # TODO: convert to dict
    if not is_string_object(string_object):
        raise ValueError('string_object_to_dict requires a string object')

    return json.loads(string_object)


def string_json_object_to_dict(string_object: str) -> dict:
    if not is_string_json_object(string_object):
        raise ValueError('string_object_to_dict requires a string object')

    return json.loads(string_object)


def is_string_object(source_string: str) -> bool:
    # TODO: extend to nested objects (Note: you did this in node for CIV Team)
    optional_json_object_regex: str = '^{( ?[\'\"]?.+[\'\"]? ?: ?[\'\"]?.+[\'\"]?,? ?)+}$'
    result = re.search(optional_json_object_regex, source_string)
    return result is not None


def is_string_json_object(source_string: str) -> bool:
    json_object_regex: str = '^{( ?\".+\" ?: ?[\'\"]?.+[\'\"]?,? ?)+}$'
    result = re.search(json_object_regex, source_string)
    return result is not None
