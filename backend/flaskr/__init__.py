import json
import sys
from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from model import set_up, Book

BOOKS_PER_SHELF = 8
# def paginate_books(request, selection):
#     page = request.args.get('page', 1, type = int)
#     start = (page - 1) * BOOK_PER_SHELF
#     end = start + BOOK_PER_SHELF

#     books = [book.format() for book in selection]
#     current_book = books[start:end]

#     return current_book
def paginate_books(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * BOOKS_PER_SHELF
    end = start + BOOKS_PER_SHELF

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
    # def retrieve_books():
    #     selection = Book.query.order_by(Book.id).all()
    #     print([select.format() for select in selection])
    #     # return 'result'
    #     current_books  = pagination(request, selection)
    #     return ('result')

    #     # if len(current_books) == 0:
    #     #     abort(404)
    #     # return jsonify({
    #     #     'success': True,
    #     #     'books': current_books,
    #     #     'total_books': len(Book.query.all())
    #     # })
    def retrieve_books():
        selection = Book.query.order_by(Book.id).all()
        current_books = paginate_books(request, selection)

        if len(current_books) == 0:
            abort(404)

        return jsonify(
            {
                "success": True,
                "books": current_books,
                "total_books": len(Book.query.all()),
            }
        )

    return app