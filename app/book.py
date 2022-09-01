from flask import Blueprint, current_app, jsonify, request
from .model import Book
from .serealize import BookSchema
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import engine
from marshmallow import EXCLUDE

bp_book = Blueprint('books', __name__)



@bp_book.route('/book', methods=['GET'])
def show():
    bsh = BookSchema(many=True)
    books = Book.query.all()
    books_dump = bsh.dump(books)
    return jsonify(books_dump), 200

    
@bp_book.route('/book', methods=['POST'])
def create():
    bsh = BookSchema(unknown=EXCLUDE)
    data = request.get_json()
    sess = scoped_session(sessionmaker(bind=engine))
    book = bsh.load(data, session=sess)
    books = bsh.dump(book)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    return jsonify(books), 201
    
    
@bp_book.route('/book/<id>', methods=['PUT'])
def edit(id):
    bsh = BookSchema(unknown=EXCLUDE)
    query = Book.query.filter(Book.id_book == id)
    query.update(request.json)
    current_app.db.session.commit()
    autors = bsh.dump(query.first())
    return jsonify(autors), 200

@bp_book.route('/book/<id>', methods=['DELETE'])
def delete(id):
    Book.query.filter(Book.id_book == id).delete()
    current_app.db.session.commit()
    return jsonify('Deletado'), 200
