from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

## CONFIGURING DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


## CREATING TABLE SCHEMA
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route("/")
def home():
    return render_template("index.html", books=db.session.query(Book).all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["title"],
                        author=request.form["author"],
                        rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit_rating", methods=["GET", "POST"])
def edit_rating():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    # id parameter passed by get request by anchor in index.html template
    book_id = request.args.get("id")
    book_selected = Book.query.get(book_id)
    # passing book_selected to edit_rating template
    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
