from app.mongo_db import Mongo
from app.utils import generate_str_uuid4, dict_have_key


class DigimonServiceStore:

    def __init__(self):
        self.db = Mongo("localhost", 27017)
        self.coll = "digimons"
        self.db_name = "dev"

    def insert(self, digimon):
        digimon["id"] = generate_str_uuid4()
        return self.db.insert_doc(self.db_name, self.coll, digimon).inserted_id

    def update(self, digimon):
        if dict_have_key(digimon, "id"):
            return self.db.update_doc(self.db_name, self.coll, digimon).modified_count

    def delete(self, digimon):
        if dict_have_key(digimon, "id"):
            return self.db.delete_doc(self.db_name, self.coll, digimon).deleted_count

    def find(self, digimon):
        return self.db.find_doc(self.db_name, self.coll, digimon)

    def finds(self, query):
        return self.db.find_docs(self.db_name, self.coll, query)
