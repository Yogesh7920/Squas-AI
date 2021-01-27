import numpy as np


def prefer(items):
    res = []
    for item in items:
        if item['B'] == 1 and item['R'] == 1 and item['G'] == 1:
            res.append(1)
        else:
            res.append(0)

    return np.array(res)
