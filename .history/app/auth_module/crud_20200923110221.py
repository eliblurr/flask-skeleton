from .models import *
from .schemas import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
import uuid

class UsersList(Resource):
    # @jwt_required
    def get(self):
        try:
            users = Users.query.all()
            return UsersSchema(many=True).dump(region)
        except:
            return 'some error occured',500

    # create  user
    def post(self):
        data = add_parser.parse_args()
        new_user = Users(
            username=data['username'],
            password=Users.generate_hash(data['password']),
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return 'success',200
        except:
            return 'some error occured',500

class Region(Resource):
    # @jwt_required
    def get(self,id):
        if not id:
            return 'failed! check id type or id not present',500
        user = Users.query.filter_by(id = id).first()
        return UsersSchema().dump(region)

    # @jwt_required
    def delete(self,id):
        if not id:
            return 'failed! check id type or id not present',500
        user = Users.query.filter_by(id = id).first()
        db.session.delete(user)
        db.session.commit()
        return 'success',200

class Authenticate(Resource):
    def authenticate(self):
        data = add_parser.parse_args()


