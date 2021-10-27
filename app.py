# A Flask app that runs a microservice on the local machine providing
# access to python utilities via API endpoints.
#
# To run the service, `flask run` on the command line.
# To run with debugger and reloader active, `export FLASK_ENV=development` beforehand

from modules.sayhello_test_module import hi_message
from modules.partitional import Partitional
from modules.sayhello_test_module import add_two_numbers
from modules.primes import Primes

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world_from_app():
    return '<h1>hello world</h1>'


@app.route('/hello')
def default_fn():
    return hi_message()


@app.route('/add', methods=['GET'])
def add():
    m:int = int(request.args.get('m'))
    n:int = int(request.args.get('n'))
    sum:str = str(add_two_numbers(m,n))
    return sum


@app.route('/primes/nth_prime', methods=['GET'])
def primes_nth_prime():
    primes = Primes()
    n:int = int(request.args.get('n'))
    nth_prime:int = primes.nth_prime_number(n)
    return str(nth_prime)


@app.route('/partitional/partition_set', methods=['GET'])
def partitional_partition_set():
    # e.g. http://127.0.0.1:5000/partitional/partition_set?source_list=hello|there|world&partitions_count=2
    # with json objects: http://127.0.0.1:5000/partitional/partition_set?source_list={%22id%22:1,%22body%22:%22hello%22}|{%22id%22:2,%22body%22:%22there%22}|{%22id%22:3,%22body%22:%22world%22}&partitions_count=2
    source_list:list = request.args.get('source_list').split('|')
    partitions_count:int = int(request.args.get('partitions_count'))
    partitional = Partitional(source_list)
    partition_set:list = partitional.partition_set(len(source_list), partitions_count)

    return f'partition set:<br>{partition_set}<br>number of sets of length {partitions_count}: {len(partition_set)}'

