from collections import Counter
import math


def euclidean_distance(a, b):
    # a and b are supposed to be vectors of same dimension
    sum_squared_distance = 0
    for i in range(len(a)):
        sum_squared_distance += math.pow(a[i] - b[i], 2)
    return math.sqrt(sum_squared_distance)


def k_nearest_indices(product_vectors, user_vector, k):

    # product vectors are say [[xx, xx,.., xx, xx], [xx, xx,.., xx, xx], ....., [xx, xx,.., xx, xx]]
    # user vector is say [xx, xx,.., xx, xx]
    # our target is to find top k the nearest vector to user_vector
    # and return them
    dist_and_indices = []
    for index, vector in enumerate(product_vectors):
        distance = euclidean_distance(vector, user_vector)
        dist_and_indices.append((distance, index))
    dist_and_indices.sort()
    return [i[1] for i in dist_and_indices[:k]]


