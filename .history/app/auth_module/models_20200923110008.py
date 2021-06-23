from app import db
from passlib.hash import pbkdf2_sha256 as sha256

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    @staticmethod
   def generate_hash(password):
        return sha256.hash(password)
    
   @staticmethod
   def verify_hash(password, hash):
        return sha256.verify(password, hash)


class AccessTokens(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.String, primary_key=True)
