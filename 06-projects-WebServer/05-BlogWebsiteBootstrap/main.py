from flask import Flask, render_template, request
from post import Post
import requests

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
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
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
