from .models import *
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()

parser.add_argument('id', help = 'This field cannot be blank', required = False)
parser.add_argument('region_name', help = 'This field should be of valid type', required = True)
parser.add_argument('districts_id', help = 'This field should be of valid type', required = True)
parser.add_argument('priority', help = 'This field should be of valid type', required = True)

