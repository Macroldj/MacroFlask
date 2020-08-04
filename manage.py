from flask_sqlalchemy import SQLAlchemy

from utils.app import create_app
from utils.config import Config

app = create_app(Config)
manager = Manager(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


if __name__ == '__main__':
    manager.run()