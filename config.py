class Config(object):
    DEBUG = False


class Development(Config):
    DEBUG = True
    DB_URI = "mongodb://localhost:27017"
    COLL_NAME = "digimons"
    DB_NAME = "dev"


class Production(Config):
    DB_URI = "mongodb://flask-user:A5k9Nce9PVJi@ds211268.mlab.com:11268/heroku_qt82bw6b?retryWrites=false"
    COLL_NAME = "digimons"
    DB_NAME = "heroku_qt82bw6b"


