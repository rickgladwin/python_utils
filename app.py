# A Flask app that runs a microservice on the local machine providing
# access to python utilities via API endpoints.
#
# To run the service, `flask run` on the command line.
# To run with debugger and reloader active, `export FLASK_ENV=development` beforehand

from modules.sayhello_test_module import hi_message
from modules.partitional import Partitional
from modules.sayhello_test_module import add_two_numbers
from modules.primes import Primes
from modules.combinations import n_choose_r

from flask import Flask, request, Response

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
    m:int = int(request.args.get('m'))
    n:int = int(request.args.get('n'))

    result: int = add_two_numbers(m,n)

    return build_data_object(result)


@app.route('/primes/nth_prime', methods=['GET'])
def primes__nth_prime():
    primes = Primes()
    n:int = int(request.args.get('n'))

    nth_prime:int = primes.nth_prime_number(n)

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
    n: int = int(request.args.get('n'))
    r: int = int(request.args.get('r'))

    result: int = n_choose_r(n, r)

    return build_data_object(result)


@app.route('/combinations/combinations_r', methods=['GET'])
def combinations__combinations_r():
    n: int = int(request.args.get('n'))
    r: int = int(request.args.get('r'))

    result: int = n_choose_r(n, r)

    return build_data_object(result)