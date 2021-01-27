import requests
import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


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


def sizeRemove(feat):
    dimensions = feat.pop('size')
    feat['shoulder'] = dimensions[0]
    feat['chest'] = dimensions[1]
    feat['torso'] = dimensions[2]
    feat['size_avg'] = np.mean(dimensions)
    return feat


def preprocessing(feats):
    feats = list(map(sizeRemove, feats))
    data = pd.DataFrame(feats)
    data.drop(['id', 'name'], axis=1)
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    return data
