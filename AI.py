from recommendation import Recommendation
from test.user_preference import prefer1, prefer2
from utils.knn import nearest
from utils.others import get_user_dim, user_model, preprocessing
from utils.parser import parser
from sklearn.model_selection import train_test_split
import random
import pandas as pd
from sklearn.metrics import classification_report, mean_squared_error
from pprint import pprint
import numpy as np


class AI:
    item = 't-shirt'

    def __init__(self, username, optimize='bin'):
        self.username = username
        self.optimize = optimize

    def switch_optimize(self):
        self.optimize = {
            'bin': 'rec',
            'rec': 'bin'
        }.get(self.optimize, 'bin')

    def preprocessing(self, data, k, dev=True):
        data = parser(data)
        user = get_user_dim()
        user = user_model(user, self.item)
        feat = nearest(data, user, k)
        if dev:
            if self.optimize == 'bin':
                likes = prefer1(feat)
            else:
                likes = prefer2(feat)

            p_feat = preprocessing(feat)
            return feat, p_feat, likes

        p_feat = preprocessing(feat)
        return feat, p_feat, []

    def train(self, raw_data):
        _, p_feat, likes = self.preprocessing(raw_data, 250)
        X_train, X_test, y_train, y_test = train_test_split(p_feat, likes, test_size=0.2)
        rec = Recommendation(p_feat.shape[1], self.username, self.optimize)
        rec.train(X_train, y_train, 80)

        if self.optimize == 'rec':
            print('MSE = ', mean_squared_error(y_test, rec.model.predict(X_test)))
        else:
            print(classification_report(y_test, rec.model.predict_classes(X_test)))

    def test(self, test_data):

        feat, p_feat, likes = self.preprocessing(test_data, 40)

        csv = pd.DataFrame(feat)
        csv['score'] = likes
        csv.to_csv('test.csv')

        rec = Recommendation(p_feat.shape[1], self.username, self.optimize)

        best = feat[rec.get_best(p_feat)]
        print("\n\nBEST of test.csv", end='\t')
        print('id = ', best['id'])
        pprint(best)

    def predict(self, raw_data):
        feat, p_feat, _ = self.preprocessing(raw_data, 250, False)
        rec = Recommendation(p_feat.shape[1], self.username, self.optimize)
        best = feat[rec.get_best(p_feat)]
        rec.save()
        best_prod = list(filter(lambda x: x['id'] == best['id'], raw_data))[0]
        return best_prod

    def feedback_train(self, data, username):
        _, p_feat, _ = self.preprocessing(data, 250, False)
        likes = np.array([0])
        rec = Recommendation(p_feat.shape[1], username, self.optimize)
        rec.model.fit(p_feat, likes, epochs=5, verbose=0)
        rec.save()
