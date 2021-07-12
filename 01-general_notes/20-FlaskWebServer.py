# Flask is a framework for web app backends
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# Another option is django, but flask is enough for small projects

# What is a Framework?
# https://en.wikipedia.org/wiki/Software_framework

# Framework x Library:
# Frameworks and libraries are both code written by someone else
# that helps you perform some common tasks in a less verbose way.
# A framework inverts the control of the program.
# It tells the developer what they need. A library doesn't.

from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        prefix = "<b>"
        text = function()
        suffix = "</b>"
        return prefix+text+suffix
    return wrapper()


# decorator function serves to add the functionality
# it calls the bellow function only if that route is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/greet/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello {name}, your luck number is {number}</p>"


@app.route("/bye")
@make_bold
def bye():
    return "Bye!!"


# https://docs.python.org/3/library/__main__.html
# run app if this script is being executed in top level scope (not imported)
if __name__ == "__main__":
    app.run(debug=True)

# after that, it will be running on: http://127.0.0.1:5000/ (or localhost:5000)

# --- TIPS --- #

# Browser Cache when testing:
# when testing, sometimes the browser caches static files
# to overcome this, press SHIFT and click on RELOAD icon

# for HTML5 templates:
# You can use: https://html5up.net/
# or: https://www.squarespace.com/

# Edit Template HTML on Browser:
# type on browser console: > document.body.contentEditable=true
# now you can change the website
# to delete elements, go to elements on developer's tools and hit backspace
# remember to save the .html file and move to your server folder