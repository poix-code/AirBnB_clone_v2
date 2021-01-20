#!/usr/bin/python3
"""Runs a Flask application on port 5000"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' and the value of 'text', underscores
    must be replaced by spaces (_)"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0")