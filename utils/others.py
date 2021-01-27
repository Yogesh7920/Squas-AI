import requests
import json
import pandas as pd


def api(name):
    url = 'https://squas-store.herokuapp.com/amazon/'
    req = requests.get(url, params={'name': name})
    data = req.json()
    return data


def user_model(user, item):
    with open('db/user_model.json') as f:
        model = json.load(f)
        return {k: user[k] for k in model[item]}


def get_user_dim():
    with open('db/user.json') as f:
        user = json.load(f)
        return user


def preprocessing(feat):
    dimensions = feat.pop('size')
    feat['shoulder'] = dimensions[0]
    feat['chest'] = dimensions[1]
    feat['torso'] = dimensions[2]
    data = pd.DataFrame(feat)
    data.drop(['id', 'name'], axis=1)
    return data.to_numpy()
