from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)

app.config.from_object('config')

b = SQLAlchemy(app)
jwt = JWTManager(app)
cors = CORS(app)
api = Api(app)