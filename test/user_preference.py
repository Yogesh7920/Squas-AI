import numpy as np


def prefer(items):
    res = []
    for item in items:
        if item['B'] == 1.0 and item['R'] == 0 and item['G'] == 0:
            res.append(1)
        else:
            res.append(0)

    return np.array(res)
