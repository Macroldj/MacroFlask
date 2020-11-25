from flask import Flask

from models import user,db,book


if __name__ == '__main__':
    app = Flask(__name__)
    