#!/usr/bin/python3
"""starts a Flask web application on port 5000"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id=None):
    """Display HTML page"""
    states = storage.all("State")
    if id:
        id = "State." + id
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def use_teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
