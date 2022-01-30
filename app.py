from flask import Flask, jsonify

from utils.utils import get_latest_articles

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    resp = get_latest_articles()
    return jsonify(resp), 200, {'Content-type': 'application/json; charset=UTF-8'}


if __name__ == '__main__':
    app.run(debug=True)
