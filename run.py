import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config
from controllers import users, books

# from config import config
app = Flask(__name__,static_folder='statics', static_url_path='/statics')
app.secret_key = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)

# url register into app
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(books, url_prefix='/books')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.SERVER_PORT, debug = config.DEBUG)