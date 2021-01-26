import numpy as np


def prefer(items):
    res = []
    for item in items:
        if item['colour'] == 'blue':
            res.append(1)
        else:
            res.append(0)

    return np.append(res)

