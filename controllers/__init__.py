from flask import Blueprint, Flask

users = Blueprint('users',__name__)
books = Blueprint('books',__name__)

from .user import *
from .book import *
