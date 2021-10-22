from flask import Blueprint, jsonify


books_bp = Blueprint('books',__name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():

    pass 

# getting book by id
@books_bp.route("/<book_id>", methods=["GET"])
def get_book_by_id(book_id):
    pass 
