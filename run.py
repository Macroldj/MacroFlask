import os

from flask import Flask

from config import config
from controllers import users, books
from models import db

# from config import config
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, static_folder='statics', static_url_path='/statics')
app.secret_key = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# router register into application
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(books, url_prefix='/books')
db.app = app
db.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.SERVER_PORT, debug=config.DEBUG)
