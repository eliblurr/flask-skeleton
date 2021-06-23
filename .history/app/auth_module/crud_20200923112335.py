from .models import *
from .schemas import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity
import uuid
from flask import jsonify
# from flask_jwt_extended import (
#     JWTManager, jwt_required, create_access_token,
#     get_jwt_identity
# )


class UsersList(Resource):
    # @jwt_required
    def get(self):
        try:
            users = Users.query.all()
            return UsersSchema(many=True).dump(users)
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

class User(Resource):
    # @jwt_required
    def get(self,id):
        if not id:
            return 'failed! check id type or id not present',500
        user = Users.query.filter_by(id = id).first()
        return UsersSchema().dump(user)

    # @jwt_required
    def delete(self,id):
        if not id:
            return 'failed! check id type or id not present',500
        user = Users.query.filter_by(id = id).first()
        db.session.delete(user)
        db.session.commit()
        return 'success',200

class Authenticate(Resource):
    def get(self):
        data = add_parser.parse_args()
        user = Users.query.filter_by(username = data['username']).first()
        if not user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}

        if Users.verify_hash(data['password'], user.password):
            # return '0ss'
            access_token = create_access_token(identity = data['username'])
            return {'access_token': access_token}
        
        return 'some error occured',500

    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200

class CurrentUser(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
# @jwt_required
# def protected():
#     # Access the identity of the current user with get_jwt_identity
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200




