from recommendation import Recommendation
from test.user_preference import prefer
from utils.knn import nearest
from utils.others import api, get_user_dim, user_model
from utils.parser import parser

if __name__ == '__main__':
    name = 't-shirt'

    raw_data = api(name)
    likes = prefer(raw_data)

    data = parser(raw_data)
    user = get_user_dim()
    user = user_model(user)

    feat = nearest(data, user)
    rec = Recommendation(len(feat))
    rec.train(feat, likes, 30)
