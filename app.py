# A Flask app that runs a microservice on the local machine providing
# access to python utilities via API endpoints.
#
# To run the service, `flask run` on the command line.
# To run with debugger and reloader active, `export FLASK_ENV=development` beforehand
import flask

from app_helpers import is_string_json_object, is_string_object, string_json_object_to_dict
from modules.sayhello_test_module import hi_message
from modules.partitional import Partitional
from modules.sayhello_test_module import add_two_numbers
from modules.primes import Primes
from modules.combinations import n_choose_r, combinations, combinations_r

from flask import Flask, request, Response, make_response

# change this line if you want to use a different file as the root file for the Flask app
app = Flask(__name__)


def build_data_object(result):
    data_object: dict = {
        'data_type': type(result).__name__,
        'result': result,
    }
    return data_object


@app.route('/')
def hello_world_from_app():
    return '<h1>Python Utilities are available via Flask!</h1>'


@app.route('/hello')
def default_fn():
    return hi_message()


@app.route('/add', methods=['GET'])
# e.g. /add?m=2&n=3 -> 5
def add():
    m: int = int(request.args.get('m'))
    n: int = int(request.args.get('n'))

    result: int = add_two_numbers(m, n)

    return build_data_object(result)


@app.route('/primes/nth_prime', methods=['GET'])
def primes__nth_prime():
    primes = Primes()
    n: int = int(request.args.get('n'))

    nth_prime: int = primes.nth_prime_number(n)

    return build_data_object(nth_prime)


@app.route('/partitional/partition_set', methods=['GET'])
def partitional__partition_set():
    # e.g. http://127.0.0.1:5000/partitional/partition_set?source_list=hello|there|world&partitions_count=2
    # with json objects: http://127.0.0.1:5000/partitional/partition_set?source_list={%22id%22:1,%22body%22:%22hello%22}|{%22id%22:2,%22body%22:%22there%22}|{%22id%22:3,%22body%22:%22world%22}&partitions_count=2
    source_list: list = request.args.get('source_list').split('|')
    partitions_count: int = int(request.args.get('partitions_count'))
    partitional = Partitional(source_list)
    partition_set: list = partitional.partition_set(len(source_list), partitions_count)

    return f'partition set:<br>{partition_set}<br>number of sets of length {partitions_count}: {len(partition_set)}'


@app.route('/combinations/n_choose_r', methods=['GET'])
def combinations__n_choose_r():
    """e.g. http://127.0.0.1:5000/combinations/n_choose_r?n=3&r=2"""
    n: int = int(request.args.get('n'))
    r: int = int(request.args.get('r'))

    result: int = n_choose_r(n, r)

    return build_data_object(result)


@app.route('/combinations/combinations_r', methods=['GET'])
def combinations__combinations_r():
    """e.g. http://127.0.0.1:5000/combinations/combinations_r?source_list=a|b|c&r=2"""
    source_list: list = request.args.get('source_list').split('|')
    r: int = int(request.args.get('r'))

    result: list = combinations_r(source_list, r)

    return build_data_object(result)


@app.route('/combinations/combinations', methods=['GET'])
def combinations__combinations():
    """e.g. http://127.0.0.1:5000/combinations/combinations_r?source_list=a|b|c"""
    source_list: list = request.args.get('source_list').split('|')

    # TODO: if the source_list elements are json strings representing objects, convert them to dicts

    # If the source_list elements are objects, they need to be JSON in order for the
    #  system to handle them successfully
    source_list_elements_are_json_objects: bool = True
    source_list_has_non_json_objects: bool = False
    for i in range(0, len(source_list)):
        if not is_string_json_object(source_list[i]):
            source_list_elements_are_json_objects = False
            if is_string_object(source_list[i]):
                source_list_has_non_json_objects = True
                break

    if source_list_elements_are_json_objects:
        for i in range(0, len(source_list)):
            source_list[i] = string_json_object_to_dict(source_list[i])

    if source_list_has_non_json_objects:
        error_response = make_response('objects in the source list must be JSON formatted', 400)
        return error_response

    result: list = combinations(source_list)

    return build_data_object(result)
