from collections import Counter
import math
import numpy as np

def euclidean_distance(a, b):
    # a and b are supposed to be vectors of same dimension
    return np.linalg.norm(np.array(a) - np.array(b))


def is_underfit(vector, user_vector):
    for i in range(len(vector)):
        if(vector[i] < user_vector[i]):
            return True
    return False

def k_nearest_indices(product_vectors, user_vector, k):

    # product vectors are say [[xx, xx,.., xx, xx], [xx, xx,.., xx, xx], ....., [xx, xx,.., xx, xx]]
    # user vector is say [xx, xx,.., xx, xx]
    # our target is to find top k the nearest vector to user_vector
    # and return them
    dist_and_indices = []
    for index, vector in enumerate(product_vectors):
        if(is_underfit(vector, user_vector)):
            continue
        distance = euclidean_distance(vector, user_vector)
        dist_and_indices.append((distance, index))
    dist_and_indices.sort()
    return [i[1] for i in dist_and_indices[:k]]


def nearest(prod_attr, user_attr):
    k = 5
    prod_vector = []
    user_vector = []
    for key, dimension in user_attr:
        user_vector.append(dimension)
    for products in prod_attr:
        prod_vector.append(products['size'])
    # the product vector is a list of vectors of dimensions
    # prod_vector = [[12, 23, .., 32], [13, 22, .., 34], .., [15, 25, .., 40]]
    # use_attr = [12, 22, .., 34]
    # 
    k_indices = k_nearest_indices(prod_vector, user_vector, k)
    nearest_products = []
    for index in k_indices:
        nearest_products.append(prod_attr[index])
    # nearest_products = those products which are closest to user in terms of dimension
    return nearest_products

