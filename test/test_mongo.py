from assertpy import assert_that
from test.fixtures.mongo_fixtures import *


class TestMongo:
    def test_should_be_insert_document(self, doc, db):
        result = db.con.insert_doc(db.name, db.collection, doc)
        assert_that(result.inserted_id).is_not_none()

    def test_should_be_insert_documents(self, docs, db):
        result = db.con.insert_docs(db.name, db.collection, docs)
        assert_that(result.inserted_ids).is_length(3)

    @pytest.mark.parametrize("query", [{"type": "Data"}, {"stage": "Rookie"}])
    def test_should_be_find_documents(self, db, docs, query):
        db.con.insert_docs(db.name, db.collection, docs)
        cursor = db.con.find_docs(db.name, db.collection, query)
        assert_that(cursor).extracting("name").is_equal_to(["Datamon", "Gabumon"])

    @pytest.mark.parametrize("query", [{"type": "Data"}, {"stage": "Rookie"}])
    def test_sould_be_find_document(self, db, docs, query):
        db.con.insert_docs(db.name, db.collection, docs)
        doc = db.con.find_doc(db.name, db.collection, query)
        assert_that(doc).contains_value("Rookie", "Datamon")

    def test_should_be_update_document(self, db, doc, docs):
        db.con.insert_docs(db.name, db.collection, docs)
        result = db.con.update_doc(db.name, db.collection, doc)
        assert_that(result.modified_count).is_equal_to(1)

    def test_should_delete_document(self, db, docs):
        db.con.insert_docs(db.name, db.collection, docs)
        result = db.con.delete_doc(db.name, db.collection, docs[1])
        assert_that(result.deleted_count).is_equal_to(1)
