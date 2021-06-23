from .models import *
from .schemas import *
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
import uuid

class RegionList(Resource):
    # @jwt_required
    def get(self):
        region = Regions.query.all()
        return RegionsSchema(many=True).dump(region)

    def post(self):
        data = add_parser.parse_args()
        new_region = Regions(
            region_name=data['region_name'],
            districts_id=data['districts_id'],
            priority = data['priority']
        )
        
        try:
            db.session.add(new_region)
            db.session.commit()
            return 'success',200
        except:
            return 'some error occured',500

class Region(Resource):
    # @jwt_required
    def get(self,id):
        if not id:
            return 'failed! check id type or id not present',500
        region = Regions.query.filter_by(id = id).first()
        return RegionsSchema().dump(region)

    def delete(self,id):
        data = IDparser.parse_args()
        if not id:
            return 'failed! check id type or id not present',500
        region = Region.query.filter_by(id = id).first()
        db.session.delete(region)
        db.session.commit()
        return 'success',200

    def put(self,id):
        data = update_parser.parse_args()
        if not id:
            return 'failed! check id type or id not present',500
        region = Region.query.filter_by(id = id).update(data)
        db.session.commit()
        return 'success',200

