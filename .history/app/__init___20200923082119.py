from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
# Importing Configurations from config.py
app.config.from_object('config')

db = SQLAlchemy(app)
jwt = JWTManager(app)
cors = CORS(app)
api = Api(app)

@app.route('/')
def hello_world():
   return 'Hello World'

from app.region_module.crud import Region

api.add_resource(mod_auth.Region, '/login')
