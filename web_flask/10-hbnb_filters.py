#!/usr/bin/python3
"""
Script that starts a Flask web application inside the commandline
"""


from models import storage
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    render states HTML template from the 7th task
    """
    states = list(storage.all("State").values())
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """
    close storage which is either db or the file
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
