from flask import Flask, request, Response
from bson.json_util import dumps
from app.digimon_store import DigimonServiceStore
from app.utils import msg

app = Flask(__name__)


@app.route("/insert", methods=["POST"])
def insert_digimon():
    result = DigimonServiceStore().insert(request.json)

    if result is not None:
        return Response(msg("Your digimon has been inserted!"), 201, mimetype='application/json')
    else:
        return Response(msg("Your digimon has not been inserted, please try again..."), 500, mimetype='application/json')


@app.route("/update", methods=["PUT"])
def update_digimon():
    result = DigimonServiceStore().update(request.json)
    print(result)

    if result == 0:
        return Response(msg("Your digimon has not been updated, please try again..."), 422, mimetype='application/json')

    return Response(msg("Your digimon has been updated!"), 200, mimetype='application/json')


@app.route("/digimons", methods=["GET"])
def find_digimons():
    result = DigimonServiceStore().finds(request.args.to_dict())
    return Response(dumps(result), 200, mimetype='application/json')


@app.route("/digimon/", methods=["GET"])
def find_digimon():
    result = DigimonServiceStore().find(request.args.to_dict())

    if result is None:
        return Response(msg("No one digimon can be find..."), 404, mimetype='application/json')
    return Response(dumps(result), 200, mimetype='application/json')


@app.route("/delete", methods=["DELETE"])
def delete_digimon():
    result = DigimonServiceStore().delete(request.json)

    if result == 0:
        return Response(msg("Your digimon has not been deleted :Z"), 404, mimetype='application/json')

    return Response(msg("Your digimon has been deleted!"), 200, mimetype='application/json')


if __name__ == "__main__":
    app.run(debug=True)
