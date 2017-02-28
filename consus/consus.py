from flask import Flask
from flask_restful import Api

from consus.fileobj import FileObj, FileObjs
from consus.location import Location, Locations
from consus.database import Database

app = Flask(__name__)
api = Api(app)

api.add_resource(Location, '/location/<int:id>')
api.add_resource(Locations, '/locations')
api.add_resource(FileObj, '/file/<int:id>')
api.add_resource(FileObjs, '/files')

app.db = Database()