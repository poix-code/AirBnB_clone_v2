#!/usr/bin/python3
"""Runs a Flask web application on port 5000"""


from flask import Flask, render_template

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
    """Displays C + <text> without '_'"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<txt>", strict_slashes=False)
def python(txt="is_cool"):
    """Displays Python + <txt>"""
    return "Python {}".format(txt.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Checks for 'n' as int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Dispays HTML page only if n is type int"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
