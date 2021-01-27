from recommendation import Recommendation
from test.user_preference import prefer
from utils.knn import nearest
from utils.others import api, get_user_dim, user_model, preprocessing
from utils.parser import parser
from sklearn.model_selection import train_test_split
import random
import pandas as pd
from sklearn.metrics import classification_report

name = 't-shirt'
raw_data = api(name)


def train():

    data = parser(raw_data)
    user = get_user_dim()
    user = user_model(user, name)

    k = 130
    feat = nearest(data, user, k)
    likes = prefer(feat)
    processed_feat = preprocessing(feat)

    X_train, X_test, y_train, y_test = train_test_split(processed_feat, likes, test_size=0.2)

    rec = Recommendation(processed_feat.shape[1])
    rec.train(X_train, y_train, 60)

    print(classification_report(y_test, rec.model.predict_classes(X_test)))


def test():
    test_data = random.sample(raw_data, 20)
    csv = pd.DataFrame(test_data)
    csv.to_csv('test.csv')
    data = parser(test_data)
    user = get_user_dim()
    user = user_model(user, name)

    k = 20
    feat = nearest(data, user, k)
    # likes = prefer(feat)
    processed_feat = preprocessing(feat)
    rec = Recommendation(processed_feat.shape[1])

    best = feat[rec.get_best(processed_feat)]
    print("\n\n BEST of test.csv \n ")
    print(best)


if __name__ == '__main__':
    train()
    test()
