from .models import *
from .schemas import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from flask_restful import fields, marshal_with #describe response structure

resource_fields = {
    # 'task':   fields.String,
    # 'uri':    fields.Url('todo_ep')
}

class Region(Resource):
    # @jwt_required
    # @marshal_with(resource_fields)
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
    
    def get(self,id):
        if id:
            return 'get by id'

        #                 crud = Crud.query.all()
        #         # print(crud)
        #         return CrudSchema(many=True).dump(crud)
        #         return {'hello': 'Read'},200
        return 'get'

    def delete(self,id):
        return 'delete'

    def put(self,id):
        return 'put'
