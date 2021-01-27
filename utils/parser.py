from matplotlib import colors


def sizechart(size):
    # From Levi's shirt sizechart measurements
    # return format [chest, shoulder width, Front length] in cms
    return {
        'S': [100.3, 43.2, 72.4],
        'M': [108, 45.7, 74.9],
        'L': [115.6, 48.3, 77.5],
        'XL': [123.2, 49.5, 80],
        'XXL': [130.8, 52.1, 81.3],
    }.get(size, -1)


def colourencoding(colour):
    """
    We will add coding into RGB values thus making more reasonable encoding
    :param colour:
    :return: RGB
    """
    # print(colour)
    return dict(zip(('R', 'G', 'B'), colors.to_rgb(colour)))
    # return {'R': 0, 'B': 255, 'G': 0}


def brandencoding(brand):
    return {
        'adidas': 0,
        'levis': 1,
        'arrow': 2,
        'hm': 3,
        'nike': 4,
    }.get(brand, -1)


def categoryencoding(category):
    return {
        't-shirt': 0,
        'shirt': 1,
    }.get(category, -1)


def encode(key, val):
    if key == 'name':
        return categoryencoding(val)
    elif key == 'size':
        return sizechart(val)
    elif key == 'brand':
        return brandencoding(val)
    else:
        return val


def parser(raw_data):
    prod_attr = []
    for data in raw_data:
        dict = {}
        for key, val in data.items():
            dict[key] = encode(key, val)
        dict = {**dict, **colourencoding(dict.pop('colour', None))}
        prod_attr.append(dict)
    return prod_attr
