from flask import Flask, jsonify

import work

app = Flask(__name__)

@app.route('/')
def main():
    # Flask default folder for static files is "/static"
    return app.send_static_file('index.html')

@app.route('/ping')
def ping():
    work.do_work()
    return jsonify({'status': 'done'})

if __name__ == "__main__":
    app.run()
