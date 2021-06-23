from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# Importing Configurations from config.py
app.config.from_object('config')

db = SQLAlchemy(app)
jwt = JWTManager(app)
cors = CORS(app)
api = Api(app)
ma = Marshmallow(app)

@app.route('/')
def hello_world():
   return 'Hello World! Welcom to Flask Skeleton'

from app.region_module.crud import Region,RegionList

api.add_resource(RegionList, '/region')
api.add_resource(Region, '/region/<int:id>')

db.create_all()
