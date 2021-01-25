"""
    Add API, Parser and Nearest Neighbour here
"""

import requests
import json


def api(name):
    url = 'https://squas-store.herokuapp.com/amazon/'
    req = requests.get(url, params={'name': name})
    data = req.json()
    return data


def parser(raw_data):
    pass


def nearest(prod_attr, user_attr):
    k = 5
    pass


def user_model(user):
    with open('db/users.json') as f:
        model = json.load(f)
        return {k: model[k] for k in user if k in model}


def get_user_dim():
    with open('db/users.json') as f:
        user = json.load(f)
        return user
