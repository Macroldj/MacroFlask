from . import db


class Book(db.Model):
    bookId = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80), unique=True, nullable=False)
    bookName = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.bookName
