from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

# creating a new class for login form
class LoginForm(FlaskForm):
    email = EmailField(label="email: ")
    password = PasswordField(label="password: ")
    submit = SubmitField(label="LOGIN")

app = Flask(__name__)
app.secret_key = "secretsecret"

@app.route("/login", methods=["GET"])
def login_route():
    # creating a login form object to pass through rendering
    login_form = LoginForm()
    return render_template("login.html", login_form=login_form)


@app.route("/login", methods=["POST"])
def send_login():       
    data = request.form
    print(data["email"])
    print(data["password"])
    return "<h1>Successful submitted</h1>"



if __name__ == "__main__":
    app.run(debug=True)
