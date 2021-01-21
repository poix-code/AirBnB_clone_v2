#!/usr/bin/python3
"""starts a Flask web application on port 5000"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page"""
    state = storage.all("State")
    amenity = storage.all("Amenity")
    return render_template('10-hbnb_filters.html',
                           states=state, amenities=amenity)


@app.teardown_appcontext
def use_teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
