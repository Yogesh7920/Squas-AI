import requests
import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def api(**kwargs):
    url = 'https://squas-store.herokuapp.com/amazon/'
    req = requests.get(url, params=kwargs)
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
    feat['size_avg'] = np.mean(dimensions)
    return feat


def preprocessing(feats):
    feats = list(map(sizeRemove, feats))
    data = pd.DataFrame(feats)
    data.drop(['id'], axis=1)
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    return data
