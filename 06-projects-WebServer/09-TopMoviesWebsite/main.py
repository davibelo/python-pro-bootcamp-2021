from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

## CONFIGURING DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## CREATING TABLE SCHEMA
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(300), nullable=False)
    img_url = db.Column(db.String(300), nullable=False)


db.create_all()


# creating a edit form based on FlaskForm
class MovieForm(FlaskForm):
    rating = DecimalField(label="Your Rating 0-10:", places=1, validators=[DataRequired()])
    review = StringField(label="Your review:", validators=[DataRequired()])
    submit = SubmitField(label="Submit Review")

@app.route("/")
def home():
    return render_template("index.html", movies=db.session.query(Movie).all())


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = MovieForm()
    if form.validate_on_submit(): # this method works only with POST request
        print(form.rating.data)
        print(form.review.data)
    movie_id = request.args.get("id")
    movie_to_edit = Movie.query.get(movie_id)
    return render_template("edit.html", movie=movie_to_edit, form=form)


@app.route("/delete")
def delete():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
