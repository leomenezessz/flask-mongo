class Config(object):
    DEBUG = False


class Development(Config):
    DEBUG = True
    DB_URI = "localhost"
    DB_PORT = 27017
    COLL_NAME = "digimons"
    DB_NAME = "dev"


class Production(Config):
    """"TODO: Implement production configs"""
