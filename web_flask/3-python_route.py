#!/usr/bin/python3
"""Starts a Flask web application, running on port 5000"""


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


@app.route("/c/<txt>", strict_slashes=False)
def c(txt):
    """Displays 'C' and the content of 'text'"""
    return "C {}".format(txt.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is_cool"):
    """Displays Python + the value of 'text'"""
    return "Python {}".format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host="0.0.0.0")
