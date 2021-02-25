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


def train(raw_data, username):
    data = parser(raw_data)
    user = get_user_dim()
    user = user_model(user, item)

    k = 250
    feat = nearest(data, user, k)
    likes = prefer1(feat)
    processed_feat = preprocessing(feat)

    X_train, X_test, y_train, y_test = train_test_split(processed_feat, likes, test_size=0.2)

    rec = Recommendation(processed_feat.shape[1], username)
    rec.train(X_train, y_train, 150)

    print(classification_report(y_test, rec.model.predict_classes(X_test)))


def test(raw_data, username):
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
    rec = Recommendation(processed_feat.shape[1], username)

    best = feat[rec.get_best(processed_feat)]
    print("\n\nBEST of test.csv", end='\t')
    print('id = ', best['id'])
    pprint(best)


def predict(raw_data, username):
    data = parser(raw_data)
    user = get_user_dim()
    user = user_model(user, item)

    k = 250
    feat = nearest(data, user, k)
    processed_feat = preprocessing(feat)
    rec = Recommendation(processed_feat.shape[1], username)
    best = feat[rec.get_best(processed_feat)]
    # print("\n\nBEST of test.csv", end='\t')
    # print('id = ', best['id'])
    # pprint(best)
    return best['id']


if __name__ == '__main__':
    mode = 'development'
    # mode = 'production'
    username = 'Yogesh'
    raw_data = api(item=item)
    if mode == 'development':
        train(raw_data, username)
        test(raw_data, username)
    else:
        best_id = predict(raw_data, username)
        best_prod = filter(lambda x: x['id'] == best_id, raw_data)
        print(best_prod)

        correct = int(input("Is this prediction correct (1/0)"))

        if not correct:
            train([best_prod], username)
