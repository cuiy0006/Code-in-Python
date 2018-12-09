from time import sleep
from flask import Flask, Response


app = Flask(__name__)

message = 'Hello Bloomberg 2017! \n' * 10
CHUNK_LEN = 10
N_CHUNKS = len(message) / CHUNK_LEN


@app.route('/foo')
@app.route('/bar')
def hello():
    def generate():
        i = 0
        while True:
            chunk = message[i:i+CHUNK_LEN]
            if chunk:
                yield chunk
                sleep(0.85 / N_CHUNKS)
                i += CHUNK_LEN
            else:
                break

    return Response(generate())


if __name__ == '__main__':
    app.run(threaded=True, port=5011)
