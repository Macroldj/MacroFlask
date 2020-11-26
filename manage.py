from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager

from run import app
from models.user import User
from models.book import Book
from models import db

manage = Manager(app)
migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manage.run()