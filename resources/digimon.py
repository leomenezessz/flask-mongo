from flask_restful import Resource, request
from mongo import Mongo
from common.commons import generate_str_uuid4, make_resp, msg_payload, is_valid_fields
from flask import current_app as app

_ALL_VALID_FIELDS = ["id", "name", "type", "stage", "picture"]
_INSERT_FIELDS = ["name", "type", "stage", "picture"]
_VALID_DELETE_FIELDS = ["id"]


class Digimon(Resource):

    def __init__(self):
        self.db = Mongo(app.config["DB_URI"])
        self.coll = app.config["COLL_NAME"]
        self.db_name = app.config["DB_NAME"]

    def post(self):

        if not is_valid_fields(request, _INSERT_FIELDS):
            return make_resp(msg_payload("Invalid body request!"), 422)

        request.json["id"] = generate_str_uuid4()
        if self.db.insert_doc(self.db_name, self.coll, request.json).inserted_id:
            return make_resp(msg_payload("Your digimon has been inserted!"), 201)

    def put(self):

        if not is_valid_fields(request, _ALL_VALID_FIELDS):
            return make_resp(msg_payload("Invalid body request!"), 422)

        if self.db.update_doc(self.db_name, self.coll, request.json).modified_count:
            return make_resp(msg_payload("Your digimon has been updated!"), 200)
        return make_resp(msg_payload("No found digimon to update..."), 404)

    def delete(self):

        if not is_valid_fields(request, _VALID_DELETE_FIELDS):
            return make_resp(msg_payload("Invalid body request!"), 422)

        if self.db.delete_doc(self.db_name, self.coll, request.json).deleted_count:
            return make_resp(msg_payload("Your digimon has been deleted!"), 200)
        return make_resp(msg_payload("No found digimon to delete..."), 404)

    def get(self):
        result = self.db.find_doc(self.db_name, self.coll, request.args.to_dict())
        if result is not None:
            return make_resp(result, 200)
        return make_resp(msg_payload("No one digimon can be find..."), 404)


class DigimonsList(Digimon):
    def get(self):
        results = self.db.find_docs(self.db_name, self.coll, request.args.to_dict())
        return make_resp(results, 200)
