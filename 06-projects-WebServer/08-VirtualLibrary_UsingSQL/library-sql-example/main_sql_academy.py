from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sql_academy-books.db"
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

# # Creating database file
# db.create_all()

## CRUD examples ##

# Creating new record
book_1 = Book(id=1, title="Harry Potter", author="J. K. Rowling", review=9.3)
db.session.add(book_1)
db.session.commit()

# Read All Records
all_books = db.session.query(Book).all()
print(all_books)

# # Read A Particular Record By Query
# book = Book.query.filter_by(title="Harry Potter").first()
# print(book)
# print(type(book))

# # Update A Particular Record By Query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()
# all_books = db.session.query(Book).all()
# print(all_books)

# # Update A Record By PRIMARY KEY
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()
# all_books = db.session.query(Book).all()
# print(all_books)

# # Delete A Particular Record By PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
# all_books = db.session.query(Book).all()
# print(all_books)