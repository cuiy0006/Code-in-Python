import time
from flask import Flask, request


app = Flask(__name__)


@app.route('/<int:x>')
def index(x):
    time.sleep(x)
    return "{} is done".format(x)


@app.route('/error')
def error():
    time.sleep(3)
    return 'error'


if __name__ == '__main__':
    app.run(threaded=True, port=5011)
