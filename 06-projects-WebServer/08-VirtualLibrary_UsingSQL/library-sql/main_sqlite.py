import sqlite3

REL_PATH = "06-projects-WebServer/08-VirtualLibrary_UsingSQL/library-sql"


# Connecting to sql
db = sqlite3.connect(f"{REL_PATH}/books-colletion.db")
cursor = db.cursor()

# Creating database
cursor.execute(
    "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
)

# Adding first entry
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

