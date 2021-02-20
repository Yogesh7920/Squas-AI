from recommendation import Recommendation
from test.user_preference import prefer1, prefer2
from utils.knn import nearest
from utils.others import api, get_user_dim, user_model, preprocessing
from utils.parser import parser
from sklearn.model_selection import train_test_split
import random
import pandas as pd
from sklearn.metrics import classification_report
from pprint import pprint

item = 't-shirt'
raw_data = api(item=item)


def train():

    data = parser(raw_data)
    user = get_user_dim()
    user = user_model(user, item)

    k = 250
    feat = nearest(data, user, k)
    likes = prefer1(feat)
    processed_feat = preprocessing(feat)

    X_train, X_test, y_train, y_test = train_test_split(processed_feat, likes, test_size=0.2)

    rec = Recommendation(processed_feat.shape[1])
    rec.train(X_train, y_train, 80)

    print(classification_report(y_test, rec.model.predict_classes(X_test)))


def test():
    test_data = random.sample(raw_data, 50)
    data = parser(test_data)
    user = get_user_dim()
    user = user_model(user, item)

    k = 40
    feat = nearest(data, user, k)

    csv = pd.DataFrame(feat)
    likes = prefer1(feat)
    csv['score'] = likes
    csv.to_csv('test.csv')

    processed_feat = preprocessing(feat)
    rec = Recommendation(processed_feat.shape[1])

    best = feat[rec.get_best(processed_feat)]
    print("\n\nBEST of test.csv", end='\t')
    print('id = ', best['id'])
    print('\n')
    pprint(best)


if __name__ == '__main__':
    train()
    test()
