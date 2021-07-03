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

# decorator function serves to add the functionality 
# it calls the bellow function only if that route is accessed 
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye!!</p>"

# https://docs.python.org/3/library/__main__.html
# run app if this script is being executed in top level scope (not imported)
if __name__ == "__main__":
    app.run()

# after that, it will be running on: http://127.0.0.1:5000/ (or localhost:5000)
