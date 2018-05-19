from flask_restplus import Resource, Api, reqparse, fields
from flask import Blueprint
from app.models import Books


#  Blueprint that represents book.py module
books_api = Blueprint('resources.books', __name__)
api = Api(books_api)


# model for book when posting\ adding book
model_book = api.model('Book', {'book_id': fields.Integer,
                                'title': fields.String,
                                'author': fields.String,
                                'copies': fields.Integer})

# model for book when modifying book information
model_book_info = api.model('Book info', {"title": fields.String,
                                          "author": fields.String,
                                          "copies": fields.Integer})


class BooksLists(Resource):
    """Methods = [GET, POST]"""
    parser = reqparse.RequestParser()


    parser.add_argument('title', type=str, required=True,
                        help='book title is not provided', location=['json'])

    parser.add_argument('author', type=str, required=True,
                        help='book author is not provided', location=['json'])

    parser.add_argument('copies', type=int, required=True, help='book copies is not provided', location=['json'])

    @staticmethod
    def get():
        """get all books
        endpoint = /api/v1/books
        method == GET"""
        response = Books.get_all_books()
        return response


    @api.expect(model_book)
    def post(self):
        """ add a book
        endpoint = /api/v1/books
        method == POST"""
        args = self.parser.parse_args(strict=True)
        title = args['title']
        author = args['author']
        copies = args['copies']

        response = Books.add_book(book_title=title, book_author=author, book_copies=copies)
        return response

class Book(Resource):
    """methods = [GET, POST, PUT, DELETE]"""

    req_data = reqparse.RequestParser()
    req_data.add_argument('title', type=str, required=False, location=['json'], help='Field cannot be empty')

    req_data.add_argument('author', type=str, required=False, location=['json'])

    req_data.add_argument('copies', type=str, location=['json'])

    @staticmethod
    def get(book_id):
        """ get specific book using id
        endpoint = /api/v1/book/<int:book_id>
        method == GET"""
        response = Books.get_one(book_id)
        return response

    @api.expect(model_book_info)
    def put(self, book_id):
        """ modify book information
        endpoint = /api/v1/books/<int:book_id>
        method == PUT"""
        args = self.req_data.parse_args(strict=True)
        title = args['title']
        author = args['author']
        copies = args['copies']

        msg = {"msg": "Field cannot be empty"}

        if title == "" or author == "" or copies == "":
            return msg

        if title == None and author == None and copies == None:
            return {"Cannot be empty"}

        if title:
            response = Books.modify_book_title(book_id, title=title)
            return response

        if author:
            response = Books.modify_book_author(book_id, author=author)
            return response

        if copies:
            response = Books.modify_book_copies(book_id=book_id, copies=copies)
            return response

    @staticmethod
    def delete(book_id):
        """ Delete book
        endpoint = /api/v1/book/<int:book_id>
        method == DELETE"""
        response = Books.delete_book(book_id)
        return response


class BorrowBook(Resource):

    def get(self, book_id):
        pass


api.add_resource(BooksLists, '/books', endpoint='books')
api.add_resource(Book, '/books/<int:book_id>', endpoint='book')
api.add_resource(BorrowBook, '/users/books/<int:book_id>')