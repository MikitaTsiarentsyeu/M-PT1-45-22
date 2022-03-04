import json


filename = "data_base.json"
with open(filename) as f:
    data_base = json.load(f)

basket = {}


def get_all():
    return data_base


def get_category(category):
    data_category = {}
    for k, v in data_base.items():
        if v[0] == category:
            data_category[k] = v
    return data_category


def get_basket():
    return basket
