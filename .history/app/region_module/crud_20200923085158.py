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
        return 'g4et all'

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
            return 'failed! check id type or id not present',400
        region = Region.query.filter_by(id = id).first()
        return region


        #                 crud = Crud.query.all()
        #         # print(crud)
        #         return CrudSchema(many=True).dump(crud)
        #         return {'hello': 'Read'},200
        return 'get by id'

    def delete(self,id):
        if not id:
            return 'failed! check id type or id not present',400
        return 'delete by id'
        #     def post(self):
        # data = IDparser.parse_args()
        # asset = Assets.query.filter_by(id = data['assetID']).first()
        # db.session.delete(asset)
        # db.session.commit()

    def put(self,id):
        if not id:
            return 'failed! check id type or id not present',400
        return 'put by id'
