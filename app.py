# A Flask app that runs a microservice on the local machine providing
# access to python utilities via API endpoints.
#
# To run the service, `flask run` on the command line.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>hello world</h1>"
