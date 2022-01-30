from flask import Flask, jsonify, make_response

from utils.utils import get_latest_articles

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    resp = make_response(jsonify(get_latest_articles()))
    resp.headers['Content-Type'] = 'application/json; charset=UTF-8'
    return resp


if __name__ == '__main__':
    app.run(debug=True)
