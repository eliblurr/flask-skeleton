from .models import *
from flask_restful import Resource, reqparse
from app import ma

class RegionsSchema(ma.Schema):
    class Meta:
        fields = ("id","region_name","districts_id","priority")


add_parser = reqparse.RequestParser()
delete_get_parser = reqparse.RequestParser()
update_parser = reqparse.RequestParser()

delete_get_parser.add_argument('id', help = 'This field cannot be blank', required = True)

add_parser.add_argument('region_name', help = 'This field should be of valid type', required = True)
add_parser.add_argument('districts_id', help = 'This field should be of valid type', required = True)
add_parser.add_argument('priority', help = 'This field should be of valid type', required = True)

update_parser.add_argument('region_name', help = 'This field should be of valid type', required = False)
update_parser.add_argument('districts_id', help = 'This field should be of valid type', required = False)
update_parser.add_argument('priority', help = 'This field should be of valid type', required = False)

