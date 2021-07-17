from flask import Flask, render_template, request
from post import Post
from dotenv import load_dotenv
import requests
import smtplib
import os

REL_PATH = f"{os.path.dirname(__file__)}"
load_dotenv(dotenv_path=f"{REL_PATH}/.env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
DEST_EMAIL = os.getenv("DEST_EMAIL")

# making post objects using imported Post class
posts_json = requests.get("https://api.npoint.io/ed99320662742443cc5b").json()
post_objects = []
for post in posts_json:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route("/")
def home_route():
    return render_template("index.html", all_posts=post_objects)


@app.route("/about")
def about_route():
    return render_template("about.html")


@app.route("/contact", methods=["GET"])
def contact_route():
    return render_template("contact.html")


@app.route("/contact", methods=["POST"])
def receive_contact_data():
    data = request.form
    name = data["name"]
    email = data["email"]
    phone = data["phone"]
    message = data["message"]

    print("sending email...")
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=DEST_EMAIL,
            msg=
            f"Subject:Contact from {name}\n\n{message}\n\n email: {email}\n phone: {phone}"
        )
    print(f"email sent to {DEST_EMAIL}!")

    return "<h1> Successful sent message </h1>"


@app.route("/post/<int:index>")
def post_route(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
