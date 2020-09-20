
from flask import Flask, jsonify

app = Flask(__name__)

app.route("/")

def dummy_api1():
    return jsonify('saniya')


if __name__ == "__main1__":
    app.run()

