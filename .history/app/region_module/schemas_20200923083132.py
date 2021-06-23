from .models import *
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()

 region_name = db.Column(db.String(80), unique=True, nullable=False)
    districts_id = db.Column(db.String(120), unique=True, nullable=False)
    priority = db.Column(db.Integer,unique=False, nullable=False)

parser.add_argument('id', help = 'This field cannot be blank', required = False)
parser.add_argument('region_name', help = 'This field should be of valid type', required = True)
parser.add_argument('districts_id', help = 'This field should be of valid type', required = True)
parser.add_argument('priority', help = 'This field should be of valid type', required = True)

