from .models import *
from .schemas import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
import uuid

class UsersList(Resource):
    def get(self):
        try:
            users = Users.query.all()
            return UsersSchema(many=True).dump(region)
        except:
            return 'some error occured',500

    def post(self):
        data = add_parser.parse_args()
        new_user = Users(
            username=data['username'],
            password=data['password'],
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return 'success',200
        except:
            return 'some error occured',500

class Region(Resource):
    def get(self,id):
        if not id:
            return 'failed! check id type or id not present',500
        user = Users.query.filter_by(id = id).first()
        return UsersSchema().dump(region)

    def delete(self,id):
        if not id:
            return 'failed! check id type or id not present',500
        user = Users.query.filter_by(id = id).first()
        db.session.delete(user)
        db.session.commit()
        return 'success',200


