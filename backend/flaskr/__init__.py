
import sys
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import abort
from model import set_up, Book

BOOK_PER_SHELF = 8
def pagination(request, selection):
    page = request.args.get(page, 1, type = int)
    start = (page - 1) * BOOK_PER_SHELF
    end = start + BOOK_PER_SHELF

    books = [book.format() for book in selection]
    current_book = books[start:end]

    return current_book

# TODO: Define the create_app method and complete initial set up of the application
def create_app():
    app = Flask(__name__)
    set_up(app)
    CORS(app)

    # TODO: Enable CORS and set response headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type, Authorization, true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS'
        )
        return response
    
    # TODO: Define an app route to retrieve all books

    @app.route('/books')
    def retrieve_books():
        selection = Book.query.order_by(Book.id).all()
        current_books  = pagination(request, selection)

        if len(current_books) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'books': current_books,
            'total books': len(Book.query.all())
        })
