import numpy as np


def prefer(items):
    res = []
    for item in items:
        if item['B'] == 1:
            if item['price'] < 800:
                res.append(1)
                continue

        res.append(0)

    return np.array(res)
