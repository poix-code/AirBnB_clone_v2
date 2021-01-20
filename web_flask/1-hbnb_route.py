#!/usr/bin/python3
"""The script starts a Flask web application
The application runs on port 5000."""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Route and displays 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route and displays 'HBNB'"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
