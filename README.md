# Python Utils

## Description
A Flask app that runs a microservice on the local machine providing
access to python utilities via API endpoints.

## Requirements

- python 3.8 or higher (can be installed using `venv`)

see https://realpython.com/python-virtual-environments-a-primer/

## Install

To run this in a virtual environment (from `venv` folder):

- from project root:
- `pip install virtualenv`
- `virtualenv venv`
- `source venv/bin/activate`
- `python -m pip install <package>`
- e.g. `python -m pip install green`


## Run

- To run the service, `flask run` on the command line.
- To run with debugger and reloader active (recommended while developing), 
`export FLASK_ENV=development` beforehand

## Use

Running the app using flask will make it available on localhost.
`flask run` should output the protocol, URL, and port on which the microservice is available. By
default, this is `http://127.0.0.1:5000/`

See `/app.py` for details on routes, variables, and returns

[//]: # (TODO: generate or auto-generate API documentation. Apparently Swagger for python 
is a thing? https://swagger.io/blog/api-development/automatically-generating-swagger-specifications-wi/)

### Requests
In general, requests are made like this (_NOTE: no trailing slash before the variables_):
```html
http://<host>:<port>/<module>/<function>?<arg_1_name>=<arg_1_value>&<arg_2_name>=<arg_2_value>&...
```
e.g.
```html
http://127.0.0.1:5000/primes/nth_prime/?n=12
```
or, where an argument type is array/list (see /app.py for each route's syntax):
```html
http://127.0.0.1:5000/combinations/combinations?source_list=1|2|3
```

### Returns
In general, returns are a `dict` with the format:
```bash
{
    data_type: <function_return_data_type_name>,
    result: <function_return>,
}
```
e.g.
```bash
{
    data_type: "int",
    result: 37,
}
```

## Test

### Run unit tests directly

from app root:

`python -m unittest discover -s modules -p "*_test.py" --verbose`

### Run using `green` testing package

from app root:

#### run all unit tests
`green`

#### target specific module (in general, dotted names):
`green modules.combinations_test`

`green modules.permutations_test`

etc.

#### target specific test:
`green modules.combinations_test.CombinationsTest`

`green modules.combinations_test.NChooseRTest`

etc.
