from .models import *
from .schemas import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

class Region(Resource):
    # @jwt_required
    def post(self):
        return 'post'
    
    def get(self):
        return 'get'

    def delete(self,id):
        return 'delete'

    def put(self,id):
        return 'put'
