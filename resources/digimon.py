from flask import Response
from flask_restful import Resource, request
from mongo import Mongo
from bson.json_util import dumps
from common.commons import generate_str_uuid4, msg


class Digimon(Resource):

    def __init__(self):
        self.db = Mongo("localhost", 27017)
        self.coll = "digimons"
        self.db_name = "dev"

    def post(self):
        request.json["id"] = generate_str_uuid4()
        if self.db.insert_doc(self.db_name, self.coll, request.json).inserted_id:
            return msg("Your digimon has been inserted!"), 201

    def put(self):
        if self.db.update_doc(self.db_name, self.coll, request.json).modified_count:
            return msg("Your digimon has been updated!"), 200
        return msg("No found digimon to update..."), 404

    def delete(self):
        if self.db.delete_doc(self.db_name, self.coll, request.json).deleted_count:
            return msg("Your digimon has been deleted!"), 200
        return msg("No found digimon to delete..."), 404

    def get(self):
        result = self.db.find_doc(self.db_name, self.coll, request.args.to_dict())
        if result is not None:
            return Response(dumps(result), 200, mimetype='application/json')
        return msg("No one digimon can be find..."), 404


class DigimonsList(Digimon):
    def get(self):
        results = self.db.find_docs(self.db_name, self.coll, request.args.to_dict())
        return Response(dumps(results), 200, mimetype='application/json')
