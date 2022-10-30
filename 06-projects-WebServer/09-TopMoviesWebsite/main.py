from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

# Loading TMDB WEBSITE API KEY from .env file
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# The Movie Database API
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_DETAILS_URL = "https://api.themoviedb.org/3/movie/"
TMDB_IMAGE_URL = "http://image.tmdb.org/t/p/w185"

app = Flask(
    __name__,
    instance_path=
    "C:\\Users\\davib\\Desktop\\python-pro-bootcamp-2021\\06-projects-WebServer\\09-TopMoviesWebsite"
)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

## CONFIGURING DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app, session_options={"expire_on_commit": False})


## CREATING TABLE SCHEMA
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(300), nullable=True)
    img_url = db.Column(db.String(300), nullable=False)


with app.app_context():
    db.create_all()


# Edit rating form
class RateMovieForm(FlaskForm):
    rating = DecimalField(label="Your Rating 0-10:",
                          places=1,
                          validators=[DataRequired()])
    review = StringField(label="Your review:", validators=[DataRequired()])
    submit = SubmitField(label="Submit Review")


# Add movie form
class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    all_movies.reverse()
    for movie in all_movies:
        movie.raking = all_movies.index(movie) + 1        
        db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():  # this method works only with POST request
        movie_title = form.title.data
        response = requests.get(TMDB_SEARCH_URL,
                                params={
                                    "api_key": TMDB_API_KEY,
                                    "query": movie_title
                                })
        response.raise_for_status()
        try:
            data = response.json()["results"]
            return render_template("select.html", movies=data)
        except:
            redirect(url_for("add"))
    return render_template("add.html", form=form)


@app.route("/details", methods=["GET", "POST"])
def details():
    movie_api_id = request.args.get("id")
    response = requests.get(f"{TMDB_DETAILS_URL}/{movie_api_id}",
                            params={"api_key": TMDB_API_KEY})
    data = response.json()
    new_movie = Movie(title=data["title"],
                      year=data["release_date"].split("-")[0],
                      description=data["overview"],
                      rating=0,
                      ranking=0,
                      review="",
                      img_url=f'{TMDB_IMAGE_URL}/{data["poster_path"]}')
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie_to_rate = Movie.query.get(movie_id)
    if form.validate_on_submit():  # this method works only with POST request
        movie_to_rate.rating = float(form.rating.data)
        movie_to_rate.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_to_rate, form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    movie_id = request.args.get("id")
    movie_to_del = Movie.query.get(movie_id)
    db.session.delete(movie_to_del)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
