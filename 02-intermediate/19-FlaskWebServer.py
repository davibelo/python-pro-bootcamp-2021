# Flask is a framework for web app backends
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


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# to run the server, it is necessary to create a enviroment variable
# and use a command to start flash server

# example on bash:
# $ export FLASK_APP=02-intermediate/19-FlaskWebServer.py
# $ flask run
# after that, it will be running on: http://127.0.0.1:5000/ (or localhost:5000)

