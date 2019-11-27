from flask import Flask
from resources.digimon import Digimon, DigimonsList
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(Digimon, "/insert", "/get/", "/delete", "/update")
api.add_resource(DigimonsList, "/list/")


if __name__ == "__main__":
    app.run(debug=True)
