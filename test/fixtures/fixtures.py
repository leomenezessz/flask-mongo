import pytest
from mongo import Mongo
from test.test_commons.helpers import dict_to_namedtuple


@pytest.fixture
def doc():
    return {
        "id": "b4b00c86-04dd-4868-94da-71867d77c37c",
        "name": "Guilmon",
        "type": "Vaccine",
        "stage": "Rookie",
        "picture": None,
    }


@pytest.fixture
def docs():
    _digimon_list = [
        {
            "id": "b4b00c86-04dd-4868-94da-71867d77c37c",
            "name": "Datamon",
            "type": "Data",
            "stage": "Rookie",
            "picture": None,
        },
        {
            "id": "afc1d39c-ac67-4503-932a-0a690a22666b",
            "name": "Gabumon",
            "type": "Data",
            "stage": "Rookie",
            "picture": None,
        },
        {
            "id": "a3eb6779-f051-47aa-a8d0-ec267c660506",
            "name": "Growlmon",
            "type": "Virus",
            "stage": "Champion",
            "picture": None,
        },
    ]

    return _digimon_list


@pytest.fixture
def db(request):
    _db = {"con": Mongo("localhost", 27017), "collection": "digimons", "name": "test"}

    def drop_collection():
        _db["con"].drop_col("test", "digimons")

    request.addfinalizer(drop_collection)

    return dict_to_namedtuple("DB", _db)
