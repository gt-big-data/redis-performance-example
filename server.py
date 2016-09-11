from flask import Flask, jsonify
from redis import Redis
from rq import Queue

import work

app = Flask(__name__)
q = Queue(connection=Redis())

@app.route('/')
def main():
    # Flask default folder for static files is "/static"
    return app.send_static_file('index.html')

@app.route('/do_now')
def do_now():
    work.do_work()
    return jsonify({'status': 'done'})

@app.route('/do_later')
def do_later():
    q.enqueue(work.do_work)
    return jsonify({'status': 'queued'})



if __name__ == "__main__":
    app.run(host='0.0.0.0')
