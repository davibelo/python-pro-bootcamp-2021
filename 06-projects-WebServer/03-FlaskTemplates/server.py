from flask import Flask, render_template
import requests
import random
import datetime

AGE_GUESS_BASE_URL="https://api.agify.io/?name="
GENDER_GUESS_BASE_URL = "https://api.genderize.io?name="
BLOG_DATA_URL = "https://api.npoint.io/ed99320662742443cc5b"
# https://www.npoint.io/docs/ed99320662742443cc5b

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.datetime.now()
    year = now.year
    random_number = random.randint(1, 10)

    # sending variables to html template
    return render_template("index.html",
                           year=year,
                           random_number=random_number)

@app.route("/guess/<name>")
def guess(name):
    response = requests.get(url=f"{AGE_GUESS_BASE_URL}{name}")
    age = response.json()["age"]
    response = requests.get(url=f"{GENDER_GUESS_BASE_URL}{name}")
    gender = response.json()["gender"]
    return render_template("guess.html", name=name.capitalize(), age=age, gender=gender)

@app.route("/blog")
def blog():
    response = requests.get(url=BLOG_DATA_URL)
    articles = response.json()    
    return render_template("blog.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)