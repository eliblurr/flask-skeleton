from .models import *
from .schemas import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from flask_restful import fields, marshal_with #describe response structure

resource_fields = {
    # 'task':   fields.String,
    # 'uri':    fields.Url('todo_ep')
}

class RegionList(Resource):
    # @jwt_required
    # @marshal_with(resource_fields)
    def get(self):
        region = Region.query.all()
        return region
        # return 'g4et all'

    def post(self):
                #         args = parser.parse_args()
                # try:
                #         crud = Crud(title=args['title'])
                #         db.session.add(crud)
                #         db.session.commit()
                #         return 'success',200
                # except:
                #         return 'failed',400
        return 'post'

class Region(Resource):
    # @jwt_required
    # @marshal_with(resource_fields)
    def get(self,id):
        if not id:
            return 'failed! check id type or id not present',500
        region = Region.query.filter_by(id = id).first()
        return region

    def delete(self,id):
        data = IDparser.parse_args()
        if not id:
            return 'failed! check id type or id not present',500
        region = Region.query.filter_by(id = id).first()
        db.session.delete(region)
        db.session.commit()
        return 'success'

    def put(self,id):
        data = update_parser.parse_args()
        if not id:
            return 'failed! check id type or id not present',500
        region = Region.query.filter_by(id = id).update(data)
        db.session.commit()
        return True
        return 'put by id'
