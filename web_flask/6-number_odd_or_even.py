#!/usr/bin/python3
"""
Script that starts a Flask web application in the command line
"""


from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    display "Hello HBNB! in ther homepage"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display “HBNB” in the about page
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    display “Python ”, followed by the value of the text variable provided
    (replace underscore symbols with a space )
    """
    text = text.replace("_", " ")
    return "Python %s" % escape(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    display “n is a number” when integer
    """
    return "%d is a number" % n


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    display a HTML page that gives odd or even
    """
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
