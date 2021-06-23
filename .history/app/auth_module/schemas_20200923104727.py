from .models import *
from flask_restful import Resource, reqparse
from app import ma

class UsersSchema(ma.Schema):
    class Meta:
        fields = ("id","username")


add_parser = reqparse.RequestParser()
delete_get_parser = reqparse.RequestParser()
update_parser = reqparse.RequestParser()

delete_get_parser.add_argument('id', help = 'This field cannot be blank', required = True)

add_parser.add_argument('username', help = 'This field should be of valid type', required = True)
add_parser.add_argument('password', help = 'This field should be of valid type', required = True)

update_parser.add_argument('username', help = 'This field should be of valid type', required = False)
update_parser.add_argument('password', help = 'This field should be of valid type', required = False)

