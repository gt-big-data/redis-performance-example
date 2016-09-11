import os

from flask import Flask, jsonify
from redis import Redis
from rq import Queue

import work

USE_REDIS = os.getenv('USE_REDIS')
if USE_REDIS:
    print('Queuing work with Redis')
else:
    print('Doing work immediately.')


app = Flask(__name__)
q = Queue(connection=Redis())

@app.route('/')
def main():
    # Flask default folder for static files is "/static"
    return app.send_static_file('index.html')

@app.route('/ping')
def ping():
    if USE_REDIS:
        q.enqueue(work.do_work)
        return jsonify({'status': 'queued'})
    else:
        work.do_work()
        return jsonify({'status': 'done'})


if __name__ == "__main__":
    app.run()
