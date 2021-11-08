from flask import make_response
from werkzeug.wrappers import ResponseStream
from app import db 
import json
from app.models.book import Book
from app.models.author import Author
from flask import Blueprint, jsonify, request, make_response, abort


# the request object represents the current HTTP request

books_bp = Blueprint('books',__name__, url_prefix="/books")
authors_bp = Blueprint('author',__name__, url_prefix="/authors")
genres_bp = Blueprint('genres', __name__, url_prefix="/genres")

''' BOOKS BP'''

@books_bp.route("", methods=["POST"])
def handle_books():
    request_body = request.get_json() # Convert the json data into a dictionary
    
    if "title" not in request_body or  "description" not in request_body:
        response_body = {"details":'Invalid Data'}
        return make_response(response_body,400)
    
    new_book = Book(title=request_body['title'], description=request_body['description'])
    
    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} created", 201 )
    #! make_response DOES'T handle list
    
# getting book by id
@books_bp.route("", methods=["GET"])
def get_all_books():
    books = Book.query.all()
    # all() -> returns a list of instances of Book
    # !We can limit the number of results in our queries by using limit(). 
    # !Consider this example that gets the first 100 Book records.
    # !Book.query.limit(100).all()
    response = []
    try:
        for book in books:
            response.append({
                        "success":True,
                        "title": book.title,
                        "description": book.description,
            })
        return jsonify(response),200
        # with no specified status code resturns
    except Exception:
        abort(400)
    
    #todo except Exception: in Python, it will capture all otherwise unhandled errors, including all HTTP status codes

@books_bp.route("<book_id>", methods=['GET'])
def get_one_book(book_id):
    try:
        book = Book.query.get(id=book_id).first()
        
        return {"id": book.id,
                "title": book.title,
                "description": book.description
        }, 200

    except Exception:
        abort(404)
        # ! abort() Raises an HTTPException for the given status code 


@books_bp.route("<book_id>", methods=['PATCH'])
def update_one_book(book_id):
    try:
        book = Book.query.get(book_id)
        form_request = request.get_json()

        book.title = form_request['title']
        book.description = form_request['description']
        
        db.session.commit()
    
        return make_response(f"Book #{book_id} successfully updated")

    except Exception:
        abort(404)
        # ! abort() Raises an HTTPException for the given status code 


@books_bp.route("<book_id>", methods=['DELETE'])
def delete_one_book(book_id):
    try:
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
    
        return make_response(f"Book #{book_id} successfully deleted")

    except Exception:
        abort(404)


''' AUTHOR BLUEPRINT'''

@authors_bp.route("", methods=["GET"])
def get_all_authors():
    authors = Author.query.all()
    # all() -> returns a list of instances of Book
    response = []
    try:
        for author in authors:
            response.append({
                        "success":True,
                        "name": author.name,
            })
        return jsonify(response),200
        # with no specified status code resturns
    except Exception:
        abort(400)
    
    #todo except Exception: in Python, it will capture all otherwise unhandled errors, including all HTTP status codes

@authors_bp.route("", methods=["POST"])
def add_author():
    request_body = request.get_json() # Convert the json data into a dictionary
    new_author = Author(name=request_body['name'])
    
    db.session.add(new_author)
    db.session.commit()

    return make_response(f"Author {new_author.name} was added to the authors list", 201 )
    #! make_response DOES'T handle list
    

''' RELATIONSHIP authors/books'''


@authors_bp.route("/<authors_id>/books", methods =['GET', 'POST'])
def read_author_books(author_id):
    auth_id = int(author_id)
    author = Author.query.get(id=auth_id)
    if author is None:
        return make_response("Author not found", 404)

    if request.method == "POST":
        request_body = request.get_json()
        new_book = Book(
            title=request_body["title"],
            description=request_body["description"],
            author=author
            )
        db.session.add(new_book)
        db.session.commit()
        return make_response(f"Book {new_book.title} by {new_book.author.name} successfully created", 201)
    
    elif request.method == "GET":
        books_response = []
        for book in author.books:
            books_response.append(
                {
                "id": book.id,
                "title": book.title,
                "description": book.description
                }
            )
        return jsonify(books_response)