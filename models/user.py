from run import db


class User(db.Model):
    __bind_key__ = 'bookId'
    __tablename__ = 'user'
    userId = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(5), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username