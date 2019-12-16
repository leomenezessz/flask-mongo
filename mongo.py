from pymongo import MongoClient

retrieve_id = {'_id': False}


class Mongo:
    def __init__(self, uri):
        self.connection = MongoClient(uri)

    def insert_doc(self, db_name, col, doc):
        return self.connection[db_name][col].insert_one(doc)

    def insert_docs(self, db_name, col, docs):
        return self.connection[db_name][col].insert_many(docs)

    def find_docs(self, db_name, col, query):
        return self.connection[db_name][col].find(query, retrieve_id)

    def find_doc(self, db_name, col, doc):
        return self.connection[db_name][col].find_one(doc, retrieve_id)

    def update_doc(self, db_name, col, doc):
        return self.connection[db_name][col].update_one(
            {"id": doc["id"]}, {"$set": doc}
        )

    def delete_doc(self, db_name, col, doc):
        return self.connection[db_name][col].delete_one({"id": doc["id"]})

    def drop_col(self, db_name, col):
        return self.connection[db_name][col].drop()
