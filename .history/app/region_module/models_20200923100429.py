from app import db

class Region(db.Model):
    # __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(80), unique=True, nullable=False)
    districts_id = db.Column(db.String(120), unique=True, nullable=False)
    priority = db.Column(db.Integer,unique=False, nullable=False)


# from sqlalchemy.dialects.postgresql import UUID
# from flask_sqlalchemy import SQLAlchemy
# import uuid

# db = SQLAlchemy()

# class Foo(db.Model):
#     # id = db.Column(db.Integer, primary_key=True)
#     id = db.Column(UUID(as_uuid=True), primary_key=True, )
