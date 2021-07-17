from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


# creating a new class for login form
class LoginForm(FlaskForm):
    email = StringField(label="email: ", validators=[DataRequired(), Email()])
    password = PasswordField(label="password: ", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="LOGIN")


app = Flask(__name__)
app.secret_key = "secretsecret"
TEST_EMAIL = "d@d.com"
TEST_PASS = "12345678"

@app.route("/login", methods=["GET", "POST"])
def login_route():
    # creating a login form object to pass through rendering
    login_form = LoginForm()    
    if login_form.validate_on_submit():
        if login_form.email.data == TEST_EMAIL and login_form.password.data == TEST_PASS:
            return render_template("success.html")
        else:
            return render_template("failure.html")
    return render_template("login.html", login_form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
