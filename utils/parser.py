from matplotlib import colors


def sizechart_tshirt(name, size):
    # From Levi's shirt sizechart measurements
    # return format [chest, shoulder width, Front length] in cms
    return {
        'adidas': {
            'S': [100.3, 43.2, 72.4],
            'M': [108, 45.7, 74.9],
            'L': [115.6, 48.3, 77.5],
            'XL': [123.2, 49.5, 80],
            'XXL': [130.8, 52.1, 81.3],
        },
        'levis': {
            'S': [100.3, 43.2, 72.4],
            'M': [108, 45.7, 74.9],
            'L': [115.6, 48.3, 77.5],
            'XL': [123.2, 49.5, 80],
            'XXL': [130.8, 52.1, 81.3],
        },
        'arrow': {
            'S': [100.3, 43.2, 72.4],
            'M': [108, 45.7, 74.9],
            'L': [115.6, 48.3, 77.5],
            'XL': [123.2, 49.5, 80],
            'XXL': [130.8, 52.1, 81.3],
        },
        'hm': {
            'S': [100.3, 43.2, 72.4],
            'M': [108, 45.7, 74.9],
            'L': [115.6, 48.3, 77.5],
            'XL': [123.2, 49.5, 80],
            'XXL': [130.8, 52.1, 81.3],
        },
        'nike': {
            'S': [100.3, 43.2, 72.4],
            'M': [108, 45.7, 74.9],
            'L': [115.6, 48.3, 77.5],
            'XL': [123.2, 49.5, 80],
            'XXL': [130.8, 52.1, 81.3],
        },
    }.get(name, -1).get(size, -1)

def sizechart_shoe(brand, size):
    # Convert shoe size from UK/IN to Foot Length (in cm)
    return {
        'adidas'{
            6: 23.7,
            7: 25.4,
            8: 26.2,
            9: 27.1,
            10: 27.9,
            11: 28.8,
        },
        'nike'{
            6: 23.7,
            7: 25.4,
            8: 26.2,
            9: 27.1,
            10: 27.9,
            11: 28.8,
        },
        'puma'{
            6: 23.7,
            7: 25.4,
            8: 26.2,
            9: 27.1,
            10: 27.9,
            11: 28.8,
        },
        'sketchers'{
            6: 23.7,
            7: 25.4,
            8: 26.2,
            9: 27.1,
            10: 27.9,
            11: 28.8,
        },
        'asics'{
            6: 23.7,
            7: 25.4,
            8: 26.2,
            9: 27.1,
            10: 27.9,
            11: 28.8,
        }
    }.get(brand, -1).get(size, -1)

def sizechart(name, size):
    return {
        'jockey': {
            'XS': [67],
            'S': [77],
            'M': [87],
            'L': [97],
            'XL': [107],
            'XXL': [117],
        },
        'Enamor': {
            'XS': [81],
            'S': [86],
            'M': [91],
            'L': [96],
            'XL': [101],
        },
        'Triumph': {
            'XS': [82],
            'S': [87],
            'M': [92],
            'L': [97],
            'XL': [102],
        },
        'Calvin Klein': {
            'XS': [82],
            'S': [87],
            'M': [92],
            'L': [97],
            'XL': [103],

        },

    }.get(name, -1).get(size, -1)


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
        'puma': 5,
        'sketchers': 6,
        'asics': 7,
    }.get(brand, -1)


def categoryencoding(category):
    return {
        't-shirt': 0,
        'bra': 1,
        'shoe': 2
    }.get(category, -1)


def encode(key, val, brand, name):
    if key == 'name':
        return categoryencoding(val)
    elif key == 'size':
        if name == 't-shirt' or name == 'tshirt':
            return sizechart_tshirt(brand, val)
        elif name == 'shoe':
            return sizechart_shoe(brand, val)
        else:
            return val
    elif key == 'brand':
        return brandencoding(val)
    else:
        return val


def parser(raw_data):
    prod_attr = []
    for data in raw_data:
        dict = {}
        brand = data['brand']
        name = data['name']
        for key, val in data.items():
            dict[key] = encode(key, val, brand , name)
        dict = {**dict, **colourencoding(dict.pop('colour', None))}
        prod_attr.append(dict)
    return prod_attr
