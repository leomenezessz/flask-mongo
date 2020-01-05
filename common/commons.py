from uuid import uuid4
from bson.json_util import dumps
from flask import Response, request


def generate_str_uuid4() -> str:
    return str(uuid4())


def make_resp(data, code, mimetype="application/json"):
    return Response(dumps(data), code, mimetype=mimetype)


def msg_payload(msg):
    return {"message": msg}


def is_valid_request_method(acceptable_methods):
    for method in acceptable_methods:
        if method != request.method:
            return False
    return True


def contains_valid_path(path):
    if path in request.url:
        return True
    return False


def is_valid_fields(req: request, fields):
    if req.json is None:
        return False

    for field in fields:
        if field not in req.json:
            return False
    return True
