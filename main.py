from recommendation import Recommendation
from utils import api, parser, nearest, user_model, get_user_dim


if __name__ == '__main__':
    name = 't-shirt'

    raw_data = api(name)
    data = parser(raw_data)

    user = get_user_dim()
    user = user_model(user)

    feat = nearest(data, user)

    rec = Recommendation(len(feat))

    # ToDO: Add train, predict in loop.

