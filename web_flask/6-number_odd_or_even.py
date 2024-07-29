#!/usr/bin/python3

"""
Pyhton script that starts a Flask web application:

- listening on 0.0.0.0, port 5000
- Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
               (replace underscore _ symbols with a space)
    /python/<text>: display “Python ”, followed by the value of the text
                    variable (replace underscore _ symbols with a space )
                    - The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
                          H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
                          H1 tag: “Number: n is even|odd” inside the tag BODY
- uses the option strict_slashes=False definition
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    outcome = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, outcome=outcome)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
