import numpy as np


def prefer1(items):
    res = []
    for item in items:
        if item['B'] == 1:
            if item['price'] < 800:
                res.append(1)
                continue

        res.append(0)

    return np.array(res)


def prefer2(items):
    res = []
    for item in items:
        like = 0
        if item['B'] == 1 and item['R'] == 0:
            like += 1

        if item['price'] < 800:
            like += 1

        if item['price'] < 600:
            like += 1

        if item['brand'] == 0:
            like += 3

        if item['discount'] > 10:
            like += 1

        if item['discount'] > 45:
            like += 2

        if item['rating'] > 4:
            like += 2

        if item['num_of_reviews'] > 1000:
            like += 1

        res.append(like)

    return np.array(res) / np.max(res)

