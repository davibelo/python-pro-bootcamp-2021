from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create Table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    review = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return '<Book %r>' % self.title


db.create_all()

# Creating first record
book_1 = Book(id=1, title="Harry Potter", author="J. K. Rowling", review=9.3)
db.session.add(book_1)
db.session.commit()