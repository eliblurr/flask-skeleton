DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'test.db')
# SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,DB_SERVER,DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False 