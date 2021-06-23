from app import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)


class AccessTokens(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.String, primary_key=True)
