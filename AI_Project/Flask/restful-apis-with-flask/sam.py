from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Book

# Connect to Database and create database session
engine = create_engine('sqlite:///books-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_books():
    books = session.query(Book).all()
    return jsonify(books=[b.serialize for b in books])


def get_book(book_id):
    books = session.query(Book).filter_by(id=book_id).one()
    return jsonify(books=books.serialize)


def makeANewBook(title, author, genre):
    addedbook = Book(title=title, author=author, genre=genre)
    session.add(addedbook)
    session.commit()
    return jsonify(Book=addedbook.serialize)


def updateBook(id, title, author, genre):
    updatedBook = session.query(Book).filter_by(id=id).one()
    if not title:
        updatedBook.title = title
    if not author:
        updatedBook.author = author
    if not genre:
        updatedBook.genre = genre
    session.add(updatedBook)
    session.commit()
    return 'Updated a Book with id %s' % id


def deleteABook(id):
    bookToDelete = session.query(Book).filter_by(id=id).one()
    session.delete(bookToDelete)
    session.commit()
    return 'Removed Book with id %s' % id


@app.route('/')
@app.route('/booksApi', methods=['GET', 'POST'])
def booksFunction():
    if request.method == 'GET':
        return get_books()
    elif request.method == 'POST':
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        genre = request.args.get('genre', '')
        return makeANewBook(title, author, genre)


@app.route('/booksApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def bookFunctionId(id):
    if request.method == 'GET':
        return get_book(id)

    elif request.method == 'PUT':
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        genre = request.args.get('genre', '')
        return updateBook(id, title, author, genre)

    elif request.method == 'DELETE':
        return deleteABook(id)


@app.route("/sameer", methods=["GET"])
def kingkhan():

    mydict = {"Sam":1 , "khan": 2, "sameer":{"kingkhan":3}, 
            "list": [1,2,3]}
    return jsonify(mydict)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8001)
