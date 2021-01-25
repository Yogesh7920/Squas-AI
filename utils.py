"""
    Add API, Parser and Nearest Neighbour here
"""

import requests
import json
from knn import k_nearest_indices

def api(name):
    url = 'https://squas-store.herokuapp.com/amazon/'
    req = requests.get(url, params={'name': name})
    data = req.json()
    return data


def parser(raw_data):
    pass


def nearest(prod_attr, user_attr):
    k = 5
    # prod_vector and user_vector are to be made 
    # based on prod_attr and user_attr charcteristics
    prod_vector = []
    user_vector = []
    k_indices = k_nearest_indices(prod_vector, user_vector, k)
    nearest_products = []
    for index in k_indices:
        nearest_products.append(prod_attr[index])
    return nearest_products


def user_model(user):
    with open('db/users.json') as f:
        model = json.load(f)
        return {k: model[k] for k in user if k in model}


def get_user_dim():
    with open('db/users.json') as f:
        user = json.load(f)
        return user
