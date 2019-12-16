class Config(object):
    DEBUG = False


class Development(Config):
    DEBUG = True
    DB_URI = "mongodb://localhost:27017"
    COLL_NAME = "digimons"
    DB_NAME = "dev"


class Production(Config):
    DB_URI = "mongodb+srv://flask-rest:BMK0FM7fql0AHcQx@flask-mongo1-ecty1.mongodb.net/"
    COLL_NAME = "digimons"
    DB_NAME = "prod"


