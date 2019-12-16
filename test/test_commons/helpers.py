from collections import namedtuple


def dict_to_namedtuple(name, dict):
    return namedtuple(name, dict.keys())(*dict.values())
