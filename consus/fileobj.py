from flask import jsonify
from flask_restful import Resource
import consus.models as models
import consus.database as database
from flask import current_app as app

class FileObj(Resource):
    pass

class FileObjs(Resource):
    def get(self):
        db = app.db.Session()
        files = db.query(models.FileObj).all()
        return jsonify(files)