from uuid import uuid4


def generate_str_uuid4() -> str:
    return str(uuid4())


def dict_have_key(dict: dict, key):
    if key in dict:
        return True
    return False


def msg(msg_param):
    return {"message": msg_param}
