#!/usr/bin/python3
"""
Script that starts a Flask web application in the commandline
"""


from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    display "Hello HBNB! as the homepage"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display “HBNB as the about page”
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    display “C ” followed by the value of the text variable provided
    (replace underscore symbols with a space )
    """
    text = text.replace("_", " ")
    return "C %s" % escape(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
