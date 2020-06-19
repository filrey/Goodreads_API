import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db.query_property()


# class Book(db.model):
#     __tablename__ = 'books'
#     id = db.Column(db.Integer, primary_key=True)
#     isbn = db.Column(db.Integer, unique=True)
#     title = db.Column(db.String)
#     author = db.Column(db.String)
#     year = db.Column(db.Integer)

#     def __init__(self, isbn, title, author, year):
#         self.isbn = isbn
#         self.title = title
#         self.author = author
#         self.year = year


# class User(db.model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String)
#     password = db.Column(db.String)

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password


# ROUTES


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        return render_template('success.html')
