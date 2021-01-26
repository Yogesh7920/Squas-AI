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

def sizechart(size):
    # From Levi's shirt sizechart measurements
    # return format [chest, shoulder width, Front length] in cms
    return {
        'S'  : [100.3, 43.2, 72.4],
        'M'  : [108, 45.7, 74.9],
        'L'  : [115.6, 48.3, 77.5],
        'XL' : [123.2, 49.5, 80],
        'XXL': [130.8, 52.1, 81.3],
    }.get(size, -1)

def colourencoding(colour):
    return {
        'red': 0,
        'blue': 1,
        'green': 2,
        'white': 3,
        'black': 4,
    }.get(colour, -1)

def brandencoding(brand):
    return {
        'adidas': 0,
        'levis' : 1,
        'arrow' : 2,
        'hm'    : 3,
        'nike'  : 4,
    }.get(brand, -1)

def categoryencoding(category):
    return{
        't-shirt' : 0,
        'shirt'   : 1,
    }.get(category, -1)

def encode(key, val):
    return {
        'name' : categoryencoding(val),
        'size' : sizechart(val),
        'brand': brandencoding(val),
        'colour': colourencoding(val),
    }.get(key, val)

def parser(raw_data):
    prod_attr = []
    for data in raw_data:
        dict = {}
        for key, val in data.items():
            dict[key] = encode(key,val)
        prod_attr.append(dict)
    return prod_attr

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
