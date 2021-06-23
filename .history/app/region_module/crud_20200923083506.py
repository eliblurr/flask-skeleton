from .models import *
from .schemas import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

class Region(Resource):
    # @jwt_required
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
        #                 crud = Crud.query.all()
        #         # print(crud)
        #         return CrudSchema(many=True).dump(crud)
        #         return {'hello': 'Read'},200
        # return 'get'

    def delete(self,id):
        return 'delete'

    def put(self,id):
        return 'put'
